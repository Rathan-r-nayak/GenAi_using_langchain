from langchain_ollama import OllamaLLM
import streamlit as st

model = OllamaLLM(model="llama3")

st.title("Chat with Ollama LLaMA3")

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = {
        "user": [],
        "ai": []
    }

# Display previous conversation
for i in range(len(st.session_state.history["ai"])):
    st.write("👤 **User:** " + st.session_state.history["user"][i])
    st.write("🤖 **AI:** " + st.session_state.history["ai"][i])

# Input field with a unique key
user_input = st.text_input("Enter your prompt", key="chat_input")

# Button to send the message
if st.button("Chat"):
    if user_input.strip().lower() == "bye":
        st.write("👋 Bye!")
        st.stop()

    if user_input.strip() != "":
        response = model.invoke(user_input)

        # Append to history
        st.session_state.history["user"].append(user_input)
        st.session_state.history["ai"].append(response)

        # Rerun the app to display new message
        st.experimental_rerun()
