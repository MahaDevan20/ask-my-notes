# Ask My Notes

A RAG-powered study assistant that lets you upload PDF notes and ask questions about them. Includes a React frontend, FastAPI backend, optional voice agent, and LangGraph/LangChain agent options.

## Project Structure

```
ask-my-notes/
├── backend/                 # FastAPI backend
│   ├── main.py              # API entry point
│   ├── ingest.py            # PDF ingestion + ChromaDB
│   ├── tools.py             # Study tools (search, calculate, date, tasks)
│   ├── agent_scratch.py     # Raw Groq tool-calling agent
│   ├── agent_langchain.py   # LangChain agent
│   ├── agent_graph.py       # LangGraph agent
│   ├── live_config.py       # Gemini Live voice config
│   ├── voice_agent.py       # Voice agent (terminal)
│   ├── voice.py             # Voice WebSocket router
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Copy to .env and add your API keys
│   └── docs/                # PDF notes go here
├── frontend/                # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx          # Main chat UI
│   │   ├── Voice.jsx        # Voice interface
│   │   ├── App.css
│   │   └── index.css
│   └── vite.config.js
└── crew/                    # CrewAI integration (experimental)
```

## Getting Started

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd ask-my-notes
```

### 2. Backend setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate.fish   # fish shell
# or
source venv/bin/activate        # bash/zsh

# Install dependencies
pip install -r requirements.txt

# Copy env example and add your keys
cp .env.example .env
# Edit .env and add your GROQ_API_KEY and GEMINI_API_KEY

# Run the server
uvicorn main:app --reload --port 8010
```

### 3. Frontend setup

```bash
cd frontend

# Install dependencies
npm install

# Run dev server
npm run dev
```

Open http://localhost:5173 in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/ask` | Ask a question about your notes |
| POST | `/upload` | Upload a PDF |
| POST | `/clear` | Clear all notes |
| POST | `/agent` | Ask using the agent (tools) |

## Voice Agent (optional)

Run in a terminal for voice conversation:

```bash
cd backend
python voice_agent.py
```

Requires a microphone and speakers/headphones.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Groq API key for text chat |
| `GEMINI_API_KEY` | Gemini API key for voice agent |

Never commit `.env` — it's in `.gitignore`.

## License

MIT