import streamlit as st
import os
import openai
import requests
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import google.generativeai as genai
import PyPDF2 as pdf
import pandas as pd


openai_api = os.getenv("OPENAI_API_KEY")


st.title("Data Visualization using NLP")
st.write("This is a Version 0 of the app")
st.sidebar.title("Data Visualization using NLP")
st.write("________________________________________________")

## the chat layout
input = st.chat_input("Type a message...")
uploaded_file =  st.file_uploader("Upload a dataset or ask the LLM to generate one for you!")

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def csv_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        st.error("No file uploaded!")
        return None

##GeminiPro response
def get_gemini_response(request, data):
    input_text = input_prompt.format(text=request, data=data)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def input_data(uploaded_file):
    # Read the uploaded CSV file with pandas
    df = pd.read_csv(uploaded_file)
    
    # Convert the DataFrame to a string
    text = df.to_string(index=False)
    
    return text

##prompt for the resume
input_prompt = """
    You are a expert data visualization engineer and can analyze data and write python code to visualize the data
    as per it is requested. You have access to the data file and the user request. You have to filter the data, 
    analyze it, and then write a python code that visualizes the data as per the user request.
    This python code format is to be followed strictly. the code should use the python library "streamlit" to visualize the data.

    you will import the necessary libraries like this:
    import streamlit as st
    import pandas as pd
    from app import csv_data
    import plotly.express as px

    Then you will Load the dataset like this:
    uploaded_file = csv_data()
    df = pd.read_csv(uploaded_file)


    request:{text}
    data:{data}"""

# input_prompt = """
#     You are a expert data visualization engineer and can analyze data and write python code to visualize the data
#     as per it is requested. You have access to the data file and the user request. You have to filter the data, 
#     analyze it, and then write a python code that only contains the plotly code that will be passed to a function 
#     as a piece of code


#     request:{text}
#     data:{data}"""

if uploaded_file and input is not None:
    text = input_data(uploaded_file)
    #st.write(text)
    response = get_gemini_response("Visualize the data", text)
    st.write(response)

        # Save the generated code to a file
    with open("data.py", "w") as code_file:
        code_file.write(response)