from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model = OllamaLLM(model="llama3")

chat_history = [
    SystemMessage("You are a useful Mathematics teacher")
]

while True:
    user_input = input("👤: ")
    if(user_input == "bye"):
        break
    chat_history.append(HumanMessage(user_input))
    result = model.invoke(chat_history)
    print("🤖: ",result)
    chat_history.append(result)

with open("file.txt","w") as f:
    for item in chat_history:
        f.write(str(item))