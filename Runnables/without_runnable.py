from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# prompt = PromptTemplate(
#     template = "Generate 2 interesting thing about {topic}",
#     input_variables = ['topic']
# )

parser = StrOutputParser()
print(parser.invoke(model.invoke("how are you")))




# chain = prompt | model

# result = chain.invoke({"topic":"switzerland"})
# print(result)
