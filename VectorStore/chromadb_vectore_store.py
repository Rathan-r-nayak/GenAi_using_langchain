# Loads documents from folder
# Splits text into chunks
# Generates embeddings
# Stores vectors in ChromaDB

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# 1. Load documents from folder
loader = DirectoryLoader("./data",glob="**/*.txt")
documents = loader.load()
print("document loaded", documents)
print("-----------------------------------------------------------------------------------")


# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20,
    separators=["/n/n", "/n", ".", " ", ""]
)

docs = splitter.split_documents(documents=documents)
print("text splitting",docs)
print("-----------------------------------------------------------------------------------")


# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("embedding generated")
print("-----------------------------------------------------------------------------------")


# 4. Create / store in Chroma vector db
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_store"
)
vectorstore.persist()

print("✅ Successfully stored documents into Chroma vector database!")