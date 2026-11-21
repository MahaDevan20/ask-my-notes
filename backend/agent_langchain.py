from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from tools import SYSTEM_PROMPT, search_notes, calculate, today, add_task

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="messages"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])
agent = create_tool_calling_agent(llm, [search_notes, calculate, today, add_task], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[search_notes, calculate, today, add_task])

def ask_agent(question):
    result = agent_executor.invoke({"messages": [{"role": "user", "content": question}]})
    return result.get("output", ""), []
if __name__ == "__main__":
    while True:
        question = input("\nYou: ")
        if question.lower() in ("quit", "exit"):
            break
        answer, steps = ask_agent(question)
        print("  🛠  tools used:", steps or "none")
        print("Agent:", answer)
