from utils.llm_api import call_openai_llm


def llm_node(state: dict) -> dict:
    """
        Constructs a prompt using the retrieved context and user question,
        then queries the LLM to generate an answer.

        Args:
            state (dict): The current state, including the question and preprocessed context.

        Returns:
            dict: A dictionary containing the LLM's generated answer.
    """
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
