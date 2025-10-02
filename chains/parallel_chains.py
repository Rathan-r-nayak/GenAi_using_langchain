from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

promt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text \n {text}",
    input_variable = ["text"]
)
llama1 = OllamaLLM(model="llama3")

promt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=["text"]
)
llama2 = ChatGroq(model="llama-3.1-8b-instant")

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes" : promt1 | llama1 | parser,
    "quiz" : promt2 | llama2 | parser
})
merge_chain = prompt3 | llama1 | parser

chain = parallel_chain | merge_chain

with open("/home/rathan-r-nayak/Rathan/Machine Learning/machine-leaning/langchain_models/chains/content.txt" , "r", encoding='utf-8') as file:
    text = file.read()

result = chain.invoke({"text" : text})

print(result)

with open("/home/rathan-r-nayak/Rathan/Machine Learning/machine-leaning/langchain_models/chains/result.md", "w", encoding='utf-8') as file:
    file.write(result)

chain.get_graph().print_ascii()