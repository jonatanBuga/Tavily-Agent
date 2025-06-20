
def output_node(state:dict)->dict:
    """
        Consolidates the final output including the original question,
        preprocessed context, and LLM answer into a structured response.

        Args:
            state (dict): The current state including question, context, and answer.

        Returns:
            dict: A dictionary under the 'output' key containing the final structured result.
    """
    question = state.get("question","")
    answer = state.get("llm_answer","")
    tavily_context = state.get("context","")

    output = {
        "question": question,
        "context": tavily_context,
        "answer": answer
    }
    return {"output":output}
