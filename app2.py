import streamlit as st
import requests
st.title("Country Information app")
country=st.text_input("enter country name:")
search =st.button("search",use_container_width=True,type="primary")
if search:
    res=requests.get(url = f"https://restcountries.com/v3.1/name/{country}")
    if res.status_code==200:
        data = res.json()
        name=data[0]["name"]["common"]
        capital=data[0]["capital"][0]
        population=data[0]["population"]
        region=data[0]["region"]
        flag=data[0]['flags']['png']
        st.image(flag,width=150)
        st.write("country name:",name)
        st.write("capital:",capital)
        st.write("population:",population)
        st.write("region:",region)
    else:
        st.write("country not found")