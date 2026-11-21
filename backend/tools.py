import datetime
from ingest import collection

SYSTEM_PROMPT = """You are Study Buddy, a friendly study agent.
Use your tools when they help:
- search_notes for anything about the student's notes
- calculate for any maths
- today for today's date
- add_task to save a to-do for the student
Answer in simple words. Say which file and page you used."""


def search_notes(query: str) -> str:
    """Search the student's PDF notes and return the best matches."""
    results = collection.query(query_texts=[query], n_results=3)
    documents = results.get("documents", [[]])
    metadatas = results.get("metadatas", [[]])
    if not documents or not documents[0]:
        return "Nothing found in the notes."
    found = []
    for text, info in zip(documents[0], metadatas[0]):
        found.append(f"[{info['source']} p.{info['page']}] {text}")
    return "\n\n".join(found)


def calculate(expression: str) -> str:
    """Do maths, for example: (72 + 85 + 90) / 3"""
    import re
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expression):
        return "I can only use numbers, + - * / and brackets."
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(round(result, 4))
    except Exception:
        return "That maths has a mistake in it."


def today() -> str:
    """Get today's date and the day of the week."""
    return datetime.date.today().strftime("%A, %d %B %Y")


def add_task(task: str, due: str) -> str:
    """Save a study task with its due date to the to-do list."""
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(f"- {task} (due: {due})\n")
    return f"Saved: {task} (due: {due})"
