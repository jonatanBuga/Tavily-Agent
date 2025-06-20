

def preprocess_node(state: dict)->dict:
    """
        Processes the top Tavily search results and builds a clean context string
        for use by the LLM.

        Args:
            state (dict): The current state, including Tavily search results.

        Returns:
            dict: A dictionary containing the concatenated and formatted context string.
    """
    search_contexts =state.get("tavily_results","") or []
    if not search_contexts:
        return {"context": "No relevant context found."}

    top_passages = search_contexts[:3]
    context_parts = []
    for i, result in enumerate(top_passages, 1):
        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        section = f"[Source {i}] {title}\n {content}\n Source: {url}\n"
        context_parts.append(section)

    full_context = "---".join(context_parts)
    return {"context": full_context}