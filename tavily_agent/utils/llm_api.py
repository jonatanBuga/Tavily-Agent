import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def call_openai_llm(prompt: str) -> str:
    llm = ChatOpenAI(model="gpt-4.1-mini")
    message = HumanMessage(content=prompt)
    response = llm.invoke([
        message
    ]).content.strip()
    return response
