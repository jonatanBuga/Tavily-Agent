
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from nodes.input_node import input_node
from nodes.tavily_search_node import tavily_node
from nodes.preprocess_node import preprocess_node
from nodes.llm_node import llm_node
from nodes.output_node import output_node
class StateSchema(TypedDict):
    question:str
    tavily_results: List[str]
    context:str
    llm_answer: str

#graph
graph = StateGraph(StateSchema)

#add our node
graph.add_node("input",input_node)
graph.add_node("search",tavily_node)
graph.add_node("preprocess",preprocess_node)
graph.add_node("llm",llm_node)
graph.add_node("output",output_node)

#Defining transitions between nodes
graph.set_entry_point("input")
graph.add_edge("input","search")
graph.add_edge("search","preprocess")
graph.add_edge("preprocess","llm")
graph.add_edge("llm","output")
graph.add_edge("output",END)


app = graph.compile()


