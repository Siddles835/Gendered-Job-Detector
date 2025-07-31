import streamlit as st
from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

st.title("Gendered Job Detector")
st.write("Enter the start of a sentence involving a profession and see how the AI completes it. Is it reinforcing a gender stereotype?")

prompt = st.text_input("Enter a sentence starter (e.g., 'The doctor walked in')")

if prompt:
    result = generator(prompt, max_length=30, num_return_sequences=1)
    st.subheader("AI Completion: ")
    st.write(result[0]['generated_text'])