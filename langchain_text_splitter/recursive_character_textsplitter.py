from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
India is a vast country with diverse cultures and traditions.
It has 28 states and 8 union territories.
The country is known for its rich history and heritage.

Technology in India has grown rapidly in the last few decades.
Startups and IT industries are booming.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20,
    separators=["/n/n", "/n", ".", " ", ""]
)

chunk = splitter.split_text(text)

for i in chunk:
    print(i)
    print("-------------------------------------------------")