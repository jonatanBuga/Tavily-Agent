from utils.llm_api import call_openai_llm


def llm_node(state: dict) -> dict:
    question = state.get("question", "")
    context = state.get("context", "")
    prompt = (
        f"You are given the following context extracted from search results:\n\n"
        f"{context}\n\n"
        f"Based on the above context, answer the following question:\n"
        f"{question}\n"
    )
    response = call_openai_llm(prompt)
    return {"llm_answer": response}
