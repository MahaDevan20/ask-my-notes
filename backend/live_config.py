# live_config.py
# Shared Gemini Live API configuration

import os
import asyncio

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import search_notes


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your backend/.env file."
    )


# Initialize Gemini client (single instance, v1beta for Live API)
gemini = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1beta"}
)


# Gemini Live model (native audio).
# If this returns 404 later, list available models with
# client.models.list() and pick one that supports bidiGenerateContent.
MODEL = "gemini-2.5-flash-native-audio-preview-12-2025"


# Define search_notes function
search_notes_tool = {
    "name": "search_notes",
    "description": (
        "Search the student's PDF notes for a topic. "
        "Use this tool whenever the student asks about their notes."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query": {
                "type": "STRING",
                "description": "Topic or keyword to search in the PDF notes."
            }
        },
        "required": ["query"]
    }
}


# Gemini Live configuration
CONFIG = {
    "response_modalities": ["AUDIO"],

    "system_instruction": (
        "You are Study Buddy, a friendly voice tutor. "
        "Help the student understand academic topics in simple words. "
        "Keep answers short and conversational. "
        "When the student asks about their uploaded notes, "
        "use the search_notes tool. "
        "Never pretend to have searched notes if you haven't. "
        "Mention which file the information came from when available."
    ),

    "tools": [
        {
            "function_declarations": [
                search_notes_tool
            ]
        }
    ],

    "input_audio_transcription": {},

    "output_audio_transcription": {}
}


# Handle Gemini tool calls
async def answer_tool_call(session, tool_call):

    replies = []

    for fc in tool_call.function_calls:

        print(f"\n🛠 Tool called: {fc.name}")
        print(f"Arguments: {fc.args}")

        if fc.name == "search_notes":

            try:
                result = await asyncio.to_thread(
                    search_notes,
                    **(fc.args or {})
                )

            except Exception as error:
                result = f"Error searching notes: {error}"

        else:
            result = "Unknown tool requested."

        replies.append(
            types.FunctionResponse(
                id=fc.id,
                name=fc.name,
                response={
                    "result": result
                }
            )
        )

    # Send tool results back to Gemini
    await session.send_tool_response(
        function_responses=replies
    )
