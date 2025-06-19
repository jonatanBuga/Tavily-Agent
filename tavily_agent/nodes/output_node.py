
def output_node(state:dict)->dict:
    question = state.get("question","")
    answer = state.get("llm_answer","")
    tavily_context = state.get("context","")

    output = {
        "question": question,
        "context": tavily_context,
        "answer": answer
    }
    return {"output":output}
