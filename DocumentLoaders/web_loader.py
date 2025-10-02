from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/google-pixel-9-porcelain-256-gb/p/itm5364256d5efe2?pid=MOBH2HJG3HNTSRYT&lid=LSTMOBH2HJG3HNTSRYTUHOV85&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=93f2cb72-2786-42d6-a6dc-5fda1d0eef97.MOBH2HJG3HNTSRYT.SEARCH&ppt=browse&ppn=browse&ssid=nrvjg9989s0000001758816254590"
loader = WebBaseLoader(url)
content = loader.load()[0].page_content


print("giving content to AI")
prompt = PromptTemplate(
    template = "Give the specification of this particular product \n\n{product}",
    input_variables = ["product"]
)
llm = ChatGroq(model="llama-3.1-8b-instant")
output = StrOutputParser()

chain = prompt | llm | output
result = chain.invoke({"product" : content})
print(result)

# print(loader.load()[0].page_content)
# with open("flipkart.md", "w") as f:
#     f.write(loader.load()[0].page_content)
print("Saving to file")
with open("flipkart.md", "w") as f:
    f.write(result)