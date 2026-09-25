import streamlit as st
import pandas as pd

st.title("Streamlit Text input")
name = st.text_input("Enter your name")

age= st.slider("Select your age", 0, 100, 25)

st.write(f"Your age is {age}")
if name:
    st.write(f"Hello,{name}")


options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Select your favorite programming language", options)
st.write(f"Your favorite programming language is {choice}") 


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

df.to_csv("sample_data.csv")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write(df)