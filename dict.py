import streamlit as st
import requests

st.title("DICTIONARY MEANING APP")

word = st.text_input("Enter a word:")
search = st.button("Search", use_container_width=True, type="primary")

if search:
    res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if res.status_code == 200:
        data = res.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        part_of_speech = data[0]["meanings"][0]["partOfSpeech"]
        st.write("Word:", word)
        st.write("Part of Speech:", part_of_speech)
        st.write("Meaning:", meaning)
    else:
        st.write("Word not found in dictionary")