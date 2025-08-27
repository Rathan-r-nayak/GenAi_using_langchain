from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Oracle Java is the #1 programming language and development platform. Java reduces costs, shortens development timeframes, drives innovation, and improves application services. Java continues to be the development platform of choice for enterprises and developers.",
    "Python is one of the most popular programming languages. Although python is a general-purpose language, it is used in various areas of applications such as Machine Learning, Artificial Intelligence, web development, IoT, and more.",
    "JavaScript is a programming language used to create dynamic content for websites. javascript is a lightweight, cross-platform, and single-threaded programming language. It's an interpreted language that executes code line by line, providing more flexibility.",
    "C is known for its structured programming approach, which allows developers to write modular and maintainable code. C provides fine-grained control over hardware through pointers and low-level operations, making it ideal for system programming.",
    "R is a programming language and software environment for statistical analysis, graphics representation and reporting. R was created by Ross Ihaka and Robert Gentleman at the University of Auckland, New Zealand, and is currently developed by the R Development Core Team."
]

query = input("Enter the question: ")

doc_vector = embeddings.embed_documents(documents)
query_vector =embeddings.embed_query(query)

scores = cosine_similarity([query_vector], doc_vector)[0]

index, score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]

print(f"<|USER|> : {query}")
print(f"<|AI|> : {documents[index]}")