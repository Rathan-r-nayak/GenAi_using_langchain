from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Literal,Optional

model = ChatOllama(model="llama3")

class Review(TypedDict):
    genre: Annotated[list[str], "give the genres in the review as a list"]
    summary: Annotated[str, "give a brief summary of the review"]
    sentiments: Annotated[Literal["pos","neg"], "give a sentiment of the review either as pos or neg"]
    pros: Annotated[Optional[list[str]], "give the pros within the review"]
    cons: Annotated[Optional[list[str]], "give the cons within the review"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("""TMKOC was a brilliant concept, a complete family entertainer and a show which can be watched with kids and persons of all age.

Somehow, the show is loosing its appeal as it is being too much dragged and it's like there is no engagging stories left with the makers.

Dilip Joshi is still the strongest pillar of the show but I somehow sense the end of the show is near.

TMKOC was a great entertainer till couple of years back, now it has become somewhat boring.

Having said that, I personally feel still this show is better than all the other craps that are out on Indian Television.""")

print(result)