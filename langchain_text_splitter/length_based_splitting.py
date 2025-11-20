from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/Ai_Hackathon.pdf")

docs = loader.load()

# print(docs[0].page_content)

splitter = CharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_documents(docs)

for i in result:
    print("-------------------------------------")
    print(i.page_content)