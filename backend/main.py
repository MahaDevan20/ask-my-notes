import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from ingest import collection, add_pdf
from agent_scratch import run_agent as ask_agent
from voice import router as voice_router



load_dotenv()                                  # read the .env file

def get_ai():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)

app = FastAPI()

# Allow our React page to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "running", "pieces": collection.count()}

@app.post("/ask")
def ask(q: Question):
    ai = get_ai()
    if ai is None:
        return {"answer": "Server error: GROQ_API_KEY is not configured.", "sources": []}

    # 1. FIND the 4 pieces of your notes that match best
    results = collection.query(query_texts=[q.question], n_results=4)
    documents = results.get("documents", [[]])
    metadatas = results.get("metadatas", [[]])
    if not documents or not documents[0]:
        return {"answer": "Nothing found in your notes. Upload a PDF first.", "sources": []}
    pieces = documents[0]
    sources = metadatas[0]

    # 2. ADD the pieces and the question into one message
    notes = "\n\n".join(pieces)
    prompt = f"""Answer the question using ONLY these notes.
If the answer is not in the notes, say "Not found in your notes."

Notes:
{notes}

Question: {q.question}"""

    reply = ai.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    answer = reply.choices[0].message.content or "No answer generated."
    return {"answer": answer, "sources": sources}


@app.post("/clear")
def clear():
    """Remove all notes from the collection."""
    all_ids = collection.get()["ids"]
    if all_ids:
        collection.delete(ids=all_ids)
    return {"message": f"Cleared {len(all_ids)} pieces."}


@app.post("/upload")
def upload(file: UploadFile):
    name = os.path.basename(file.filename)
    path = os.path.join("docs", name)
    with open(path, "wb") as f:
        f.write(file.file.read())
    count = add_pdf(path)
    return {"message": f"Added {name} ({count} pieces). Ask me!"}

@app.post("/agent")
def agent(q: Question):
    try:
        answer = ask_agent(q.question)
        return {"answer": answer, "steps": []}
    except Exception as e:
        return {"answer": f"Agent error: {e}", "steps": []}


app.include_router(voice_router)
