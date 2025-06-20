import os
from utils.tavily_api import search_tavily

def tavily_node(state: dict)->dict:
    """
        Sends the user's question to the Tavily API to retrieve relevant web content.

        Args:
            state (dict): The current state, including the user question.

        Returns:
            dict: A dictionary containing the Tavily search results.
    """
    query = state['question']
    contexts = search_tavily(query)
    return {"tavily_results":contexts}