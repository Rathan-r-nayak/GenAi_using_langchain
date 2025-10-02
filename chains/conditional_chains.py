from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal


llm = ChatGroq(model="llama-3.1-8b-instant")

class Feedback(BaseModel):
    sentiment : Literal["positive","negetive"] = Field(description="Give the sentiment of the feedback")
output_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction': output_parser.get_format_instruction()}
)
parser = StrOutputParser()

classifier_chain = prompt1 | llm | parser
