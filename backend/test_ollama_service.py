from app.services.ollama_service import get_ollama_response

# Ollama server must be running at http://localhost:11434/api/generate for this test to work.
# To skip this test when the server is not running, comment out the code below.

'''
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
'''
