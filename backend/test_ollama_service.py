from app.services.ollama_service import get_ollama_response

# # Try with a basic query
# query = "Suggest a casual outfit for summer."

# response = get_ollama_response(query)

# print("Response from Ollama:\n")
# print(response)

questions = [
    "What is Artificial Intelligence?",
    "Tell me a joke.",
    "Who is the President of India?",
    "What are the uses of a neural network?",
    "Explain blockchain in simple terms."
]

for q in questions:
    print(f"Q: {q}")
    print("A:", get_ollama_response(q))
    print("\n" + "="*40 + "\n")
