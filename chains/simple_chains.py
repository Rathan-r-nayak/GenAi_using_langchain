from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = OllamaLLM(model="llama3")

prompt = PromptTemplate(
    template = "Generate 2 interesting thing about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic":"switzerland"})

print(result)

chain.get_graph().print_ascii()