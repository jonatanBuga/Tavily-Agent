from agent import app

def run(question: str):
    initial_state = {"question": question}
    final_result = app.invoke(initial_state)

    print("\n🎉 Final Agent Output:\n")

    print("🧠 Question:")
    print(final_result["question"])

    print("\n📚 Retrieved Sources:")
    print(final_result["context"])

    print("\n🤖 Answer from LLM:")
    print(final_result['llm_answer'])



if __name__ == "__main__":
    run(input("Teel me someting you want to know?"))