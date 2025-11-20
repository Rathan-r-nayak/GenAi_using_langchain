from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class FakeLLM:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
        print("LLM initialized ✅")

    def predict(self, prompt: str):
        # Pass as chat messages
        response = self.llm.invoke([
            ("system", "You are a helpful assistant."),
            ("human", prompt)
        ])
        return {"response": response.content}

if __name__ == "__main__":
    llm = FakeLLM()
    print(llm.predict("Tell me 3 facts about Switzerland."))
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=0
)

chunks = splitter.split_text(text=text)

print(len(chunks))
for i in chunks:
    print("--------------------------------------")
    print(i)
