from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")
prompt = ChatPromptTemplate.from_template("Write 3 facts about {topic}")
parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"topic": "Switzerland"})

print(result)

chain.get_graph().print_ascii()