
import asyncio
import pyaudio

from google.genai import types

from live_config import (
    gemini,
    MODEL,
    CONFIG,
    answer_tool_call
)


# ==========================================
# AUDIO CONFIGURATION
# ==========================================

FORMAT = pyaudio.paInt16
CHANNELS = 1

MIC_RATE = 16000
SPEAKER_RATE = 24000

CHUNK = 1024

pya = pyaudio.PyAudio()

speaker_queue = asyncio.Queue()


# ==========================================
# MICROPHONE: USER -> GEMINI
# ==========================================

async def listen(session):

    print("🎤 Microphone started.")

    mic = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=MIC_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    try:

        while True:

            data = await asyncio.to_thread(
                mic.read,
                CHUNK,
                exception_on_overflow=False
            )

            await session.send_realtime_input(
                audio=types.Blob(
                    data=data,
                    mime_type="audio/pcm;rate=16000"
                )
            )

    finally:

        await asyncio.to_thread(mic.stop_stream)
        await asyncio.to_thread(mic.close)

        print("🎤 Microphone stopped.")


# ==========================================
# RECEIVE: GEMINI -> APPLICATION
# ==========================================

async def receive(session):

    print("📡 Receiving Gemini responses.")

    # session.receive() ends after each turn_complete,
    # so the outer loop restarts it for the next turn.
    while True:

        async for response in session.receive():

            # Handle tool calls
            if response.tool_call:

                await answer_tool_call(
                    session,
                    response.tool_call
                )

            content = response.server_content

            if not content:
                continue

            # Handle interruption: drop queued audio
            if content.interrupted:

                while not speaker_queue.empty():

                    try:
                        speaker_queue.get_nowait()
                        speaker_queue.task_done()

                    except asyncio.QueueEmpty:
                        break

            # Receive generated audio
            if content.model_turn:

                for part in content.model_turn.parts:

                    if part.inline_data:

                        speaker_queue.put_nowait(
                            part.inline_data.data
                        )

            # Display Gemini's spoken response
            if (
                content.output_transcription
                and content.output_transcription.text
            ):

                print(
                    content.output_transcription.text,
                    end="",
                    flush=True
                )

            # End of response
            if content.turn_complete:

                print("\n")


# ==========================================
# SPEAKER: GEMINI -> USER
# ==========================================

async def speak():

    print("🔊 Speaker started.")

    speaker = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=SPEAKER_RATE,
        output=True
    )

    try:

        while True:

            data = await speaker_queue.get()

            try:

                await asyncio.to_thread(
                    speaker.write,
                    data
                )

            finally:

                speaker_queue.task_done()

    finally:

        await asyncio.to_thread(speaker.stop_stream)
        await asyncio.to_thread(speaker.close)

        print("🔊 Speaker stopped.")


# ==========================================
# MAIN APPLICATION
# ==========================================

async def main():

    print("\n================================")
    print("       ASK MY NOTES")
    print("       GEMINI VOICE AGENT")
    print("================================\n")

    print(f"Connecting to Gemini model: {MODEL}")

    async with gemini.aio.live.connect(
        model=MODEL,
        config=CONFIG
    ) as session:

        print("\n✅ Gemini connected successfully!")
        print("🎙 Start speaking.")
        print("🎧 Use headphones for better audio.")
        print("Press Ctrl+C to stop.\n")

        async with asyncio.TaskGroup() as tg:

            tg.create_task(listen(session))

            tg.create_task(receive(session))

            tg.create_task(speak())


# ==========================================
# APPLICATION ENTRY POINT
# ==========================================

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        print("\n\n👋 Voice assistant stopped.")

    except Exception as error:

        print(f"\n❌ Application error: {error}")

    finally:

        pya.terminate()
