from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings


from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

chunker = SemanticChunker(embedding_model)

text = """
Artificial Intelligence is changing the world. 
Machine learning allows computers to learn from data. 
Neural networks are used for image and speech recognition. 
Meanwhile, renewable energy is becoming essential.
Solar and wind energy are growing fast.
Governments are investing heavily in green technologies.Jaguar cars are known for their luxury, performance, and innovative design.Switzerland,[d] officially the Swiss Confederation,[e] is a landlocked country located at the intersection of Central, Western, and Southern Europe.
"""

chunks = chunker.create_documents([text])

for i,chunk in enumerate(chunks, 1) :
    print(f"\n--- Chunk {i} ---\n{chunk.page_content}")
    print("---------------------------------------------")
