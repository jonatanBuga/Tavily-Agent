# One-Pager – LangGraph RAG Agent using Tavily & OpenAI

##  Objective

To build an intelligent LLM agent capable of answering user queries using real-time web data.  
This is done by integrating:
- **Tavily** as a Retrieval-Augmented Generation (RAG) source
- **LangGraph** to model the data flow
- **OpenAI (GPT-4.1 mini)** to generate context-aware answers

---

##  Workflow Summary

The agent is implemented as a **LangGraph** pipeline with the following nodes:

1. **input_node**: receives a natural-language question from the user.
2. **tavily_search_node**: sends the question to Tavily API and receives a list of web search results.
3. **preprocess_node**: selects top 3 results, merges their content into a clean context string.
4. **llm_node**: sends the context + question as a prompt to OpenAI GPT and receives an answer.
5. **output_node**: compiles the final output, including the original question, the LLM's answer, and source URLs.

---

##  Design Decisions & Learning Process

- Used **Tavily API** after experimenting with its query structure and rate limits. Restricted max results to 3 to control token usage.
- Integrated OpenAI via **LangChain's ChatOpenAI**, exploring prompt formatting to maximize answer quality.
- Designed each node to be **stateless and composable**, allowing isolated testing (e.g., `llm_node()` can be tested directly).
- Debugged `llm_answer` loss by learning how LangGraph handles state flow and the importance of routing to `output_node`.

---

## How I Validated the Solution

- Created a `demo.py` script that triggers the full pipeline and prints:
  - the question
  - the retrieved context
  - and the LLM's answer.
- Used `pprint()` and manual state inspection to confirm data integrity between nodes.
- Verified edge cases (empty Tavily results, long context) to ensure graceful failure handling.

---

##  Outcome

The result is a clean, testable, and extendable LangGraph agent that performs real RAG by combining search + LLM reasoning.  
It’s easy to run, clear to analyze, and structured for long-term scale.

