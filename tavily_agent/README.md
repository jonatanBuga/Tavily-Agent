#  RAG Agent using LangGraph, Tavily & OpenAI

This project implements a modular LLM agent using LangGraph. The agent uses Tavily for retrieval (RAG) and OpenAI to generate answers based on real-time context.

##  Goal

Build an agent that:
- Accepts a natural-language question
- Searches relevant documents via Tavily
- Preprocesses the results into a context string
- Sends it to OpenAI (GPT-4.1 mini)
- Returns a structured final answer

##  Tech Stack

- LangGraph
- Tavily API (RAG source)
- OpenAI Chat API
- Python 3.10+
- `.env` file for keys
- [Streamlit](https://streamlit.io) for interactive UI

## How to Run

1. Clone the project  
2. Create `.env` with:  
    OPENAI_API_KEY=your_openai_key

    TAVILY_API_KEY=your_tavily_key
3. Install requirements: 
    pip install -r requirements.txt
4. **Launch the app**  
    ```bash
    streamlit run streamlit_app.py
    ```


##  Sample Queries

```python
"What are the implications of quantum computing on cybersecurity?"
"What are the current challenges of implementing AI in healthcare?"
"How is blockchain technology used to enhance cybersecurity?"
"What are the environmental implications of quantum computing?"
``` 

## Output Example
Final Agent Output:

Question:
What are the implications of quantum computing on cybersecurity?

Context Used:
[Source 1] ...

Answer from LLM:
Quantum computing poses a threat to current encryption...

## File Structure
    tavily_rag_agent/
    │
    ├── agent.py
    ├── streamlit_app.py.py 
    ├── requirements.txt
    ├── nodes/
    │   ├── input_node.py 
    │   ├── tavily_search_node.py
    │   ├── preprocess_node.py
    │   ├── llm_node.py
    │   └── output_node.py 
    │
    ├── utils/ 
    │   ├── tavily_api.py
    │   └── llm_api.py
    │
    ├── README.md
    └── one_pager.md


##  Made by Jonatan Bouganim
