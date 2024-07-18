## import the necessary libraries
import streamlit as st
import pandas as pd
from app import csv_data
import plotly.express as px

# Load the dataset
uploaded_file = csv_data()
st.write(uploaded_file)