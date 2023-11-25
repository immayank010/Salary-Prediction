import streamlit as st
import base64
from predict_page1 import show_predict_page1
from explore_page1 import show_explore_page1

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"aiml1.jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
if page == "Predict":
     show_predict_page1()
else:
    show_explore_page1()

add_bg_from_local('aiml1.jpg')  
