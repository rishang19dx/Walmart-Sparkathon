from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

# You can change the model name to any model you have pulled with Ollama (e.g., 'llama2', 'mistral', etc.)
OLLAMA_MODEL = "llama2"

# Basic prompt template for style queries
def get_style_prompt(query: str) -> str:
    template = PromptTemplate(
        input_variables=["query"],
        template="You are a helpful fashion assistant. {query}"
    )
    return template.format(query=query)


def get_ollama_response(query: str, model: str = OLLAMA_MODEL) -> str:
    llm = Ollama(model=model)
    prompt = get_style_prompt(query)
    response = llm(prompt)
    return response