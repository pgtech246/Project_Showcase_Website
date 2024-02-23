import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png")

with col2:
    st.title("Paul Grant")
    about_me = '''
    Hi, I am Paul! I am a Python enthusiast. I have a degree in Biology and I work in the 
    field of education, in particular, in the area of science and technology. 
    I am currently learning Python programming after assisting in the deployment of a "Coding and
    Robotics" programme at my workplace, Erdiston Teachers' Training College. That experience
    with VEX Robotics and block-based coding using Scratch has led me on this journey to hone
    newfound skills in the area of programming. I hope to eventually create or be
    part of a project(s) that can help to improve the lives of others!
    '''
    st.info(about_me)

message1 = '''
Below you can find some of the apps I have built in Python. 
Feel free to contact me!
'''
st.write(message1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])