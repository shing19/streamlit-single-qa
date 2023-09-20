import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


api_from = st.sidebar.radio(
    "Choose API",
    ["OpenAI", "Azure"]
)

if api_from == "OpenAI":
    chat = ChatOpenAI(
        temperature=0, 
        openai_api_key=st.secrets[api_from]["API_KEY"]
    )
elif api_from == "Azure":
    chat = AzureChatOpenAI(
        openai_api_base=st.secrets[api_from]["BASE_URL"],
        openai_api_version="2023-05-15",
        deployment_name=st.secrets[api_from]["DEPLOYMENT_NAME"],
        openai_api_key=st.secrets[api_from]["API_KEY"],
        openai_api_type="azure",
    )


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