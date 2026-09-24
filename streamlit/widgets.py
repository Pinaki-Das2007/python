import streamlit as st


st.title("Streamlit Text input")
name = st.text_input("Enter your name")

age= st.slider("Select your age", 0, 100, 25)

st.write(f"Your age is {age}")
if name:
    st.write(f"Hello,{name}")


options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Select your favorite programming language", options)
st.write(f"Your favorite programming language is {choice}")