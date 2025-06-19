import os
from utils.tavily_api import search_tavily

def tavily_node(state: dict)->dict:
    query = state['question']
    contexts = search_tavily(query)
    return {"tavily_results":contexts}