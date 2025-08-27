from langchain_ollama import OllamaLLM
import streamlit as st

model = OllamaLLM(model = "llama3")

st.header("Chat anything")

user_input = st.text_input("Enter your prompt")

if st.button("chat"):
    result = model.invoke(user_input)
    st.write(result)