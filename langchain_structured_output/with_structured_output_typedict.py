from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Literal,Optional

model = ChatOllama(model="llama3")

class Review(TypedDict):
    key_themes: Annotated[list[str], "give the keys in the review as a list"]
    summary: Annotated[str, "give a brief summary of the review"]
    sentiments: Annotated[Literal["pos","neg"], "give a sentiment of the review either as pos or neg"]
    pros: Annotated[Optional[list[str]], "give the pros within the review"]
    cons: Annotated[Optional[list[str]], "give the cons within the review"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, i's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful""")

print(result)