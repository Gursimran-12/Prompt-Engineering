import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables from .env
load_dotenv()

# Initialize Gemini 1.5 Flash
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    temperature=0.7
)

# Set up DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Initialize the agent with Gemini and DuckDuckGo
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ask a question
question = "What are the latest advancements in AI as of July 2025?"
response = agent.run(question)

print("\n🔍 Gemini Agent Response:\n", response)
