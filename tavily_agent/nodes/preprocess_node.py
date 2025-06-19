

def preprocess_node(state: dict)->dict:
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