import streamlit as st
from transformers import pipeline

st.title("AI Word Meaning Generator")

word = st.text_input("Enter a word:", placeholder="e.g., 'happiness' or 'journey'")

if st.button("Generate Meaning"):
    if word.strip() == "":
        st.warning("Please enter a word.")
    else:
        st.info("Generating meaning...")
        generator = pipeline("text-generation", model="gpt2")
        prompt = f"The meaning of {word} is..."

        result = generator(prompt,max_length=100,num_return_sequences=1,temperature=0.7,top_k=50)
        meaning = result[0]['generated_text'].replace(prompt, "").strip()

        st.subheader(f"Meaning of '{word}'")
        st.write(meaning)
