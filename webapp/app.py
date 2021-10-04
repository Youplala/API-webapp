import streamlit as st
import pandas as pd
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_URL = "https://api-qx6f75jsla-ew.a.run.app/run"
headers = {"Content-Type": "application/json"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=json.dumps(payload))
	return response.json()

# Display form
st.title('Text emotion detector using custom API')
st.subheader('By Elie Brosset & Julien Assuied')

form = st.form(key='my_form')
text = str(form.text_input(label='Enter some text'))
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    output = query({"api_key": str(os.getenv('API_KEY')),"input": text})
    st.subheader('Sentiment and score')
    try:
        output = output[0]
        label = output["label"]
        score = output["score"]
        st.write(f"{label} {score}")
    except:
        status = output["status"]
        st.write(status)
