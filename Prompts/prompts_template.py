from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system" , "You are a helpful {domain} expert"),
    ("human" , "Explain in simple term what is {topic}")
])

promt = chat_template.invoke({"domain":"cricket", "topic":"batting"})

print(promt)