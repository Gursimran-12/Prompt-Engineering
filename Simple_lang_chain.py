import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load API key from .env
load_dotenv()

# Initialize Gemini 1.5 Flash
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",  # or "gemini-1.5-pro-latest"
    temperature=0.7
)

# Create a human message
messages = [HumanMessage(content="What is the capital of Italy?")]

# Get a response
response = llm.invoke(messages)

# Print the output
print("Gemini:", response.content)
