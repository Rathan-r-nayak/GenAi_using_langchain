from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

template = PromptTemplate(
    template="Who invented {topic}",
    input_variables=["topic"]

)
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

template2 = PromptTemplate(
    template="Tell about {person}",
    input_variables=["person"]
)

chain = RunnableSequence(template,model,parser,template2,model,parser)
print(chain.invoke({"topic" : "Television"}))