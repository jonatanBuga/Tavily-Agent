import os
import requests
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_tavily(query: str, search_depth: str = "advanced", max_results: int = 5) -> list:
    """Sending a query from the user to the tavily API to obtain a list of relevant contexts"""
    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": search_depth,
        "max_results": max_results
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data.get("results", [])

