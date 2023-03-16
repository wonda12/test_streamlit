import streamlit as st
from PIL import Image

st.title("タイトル")
st.caption("これはキャプション")

image = Image.open("./data/0112_1.png")
st.image(image, width=200)
