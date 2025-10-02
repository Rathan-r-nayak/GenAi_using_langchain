from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("data/handson_machine_learning.pdf")

docs = loader.load()


prompt1 = PromptTemplate(
    template = "Write summary for the following content \n\n {content}",
    input_variables = ["content"]
)
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

result = prompt1 | model | parser

print(result.invoke({"content" : docs[30].page_content}))