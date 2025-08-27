from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")  # or "mistral", "codellama", etc.

response = llm.invoke("why switzerland is beautiful?")

with open("result.md","w") as file:
    file.write(response)
print(response)
