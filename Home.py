import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col1, col2 = st.columns([0.5, 0.1, 2.5])

with col1:
    st.header("")
    st.image("images/photo.png")

with col2:
    st.title("Paul Grant")
    about_me = '''
    Hi, I am Paul! I am a Python enthusiast. I have a degree in Biology and I work in the 
    field of education, in particular, in the area of science and technology. 
    I am currently learning Python programming after assisting in the deployment of a "Coding and
    Robotics" programme at my workplace, Erdiston Teachers' Training College. Working
    with VEX Robots and block-based coding using Scratch has led me on this journey to hone
    newfound skills in the area of programming. I hope to eventually create or be
    part of a project(s) that can help to improve the lives of others!
    '''
    st.info(about_me)

message1 = '''
Below you can find some of the apps I have built(or plan to build) in Python. 
Feel free to contact me!
'''
st.subheader(" ")  # create spacing
st.write(message1)
st.subheader(" ")  # create spacing

col3, empty_col2, col4 = st.columns([1.5, 0.2, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
