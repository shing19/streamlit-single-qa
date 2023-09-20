import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0, openai_api_key=st.secrets['openai_api_key'])


def generate_response(input_text):
    
    messages = [
        SystemMessage(
            content="You're a helpful bot"
        ),
        HumanMessage(
            content=input_text
        ),
    ]
    st.info(chat(messages).content)


with st.form('my_form'):
    text = st.text_area('Enter text:', 'Say something...')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)