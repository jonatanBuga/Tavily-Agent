def input_node(state: dict) -> dict:
    """
        Extracts the question from the initial state and prepares it for downstream nodes.

        Args:
            state (dict): The current state containing the user's input.

        Returns:
            dict: A dictionary with the extracted question.
        """
    return {"question": state["question"]}