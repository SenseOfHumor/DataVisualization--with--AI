## import the necessary libraries
import streamlit as st
import pandas as pd
from app import csv_data
import plotly.express as px

# Load the dataset
uploaded_file = csv_data()
df = pd.read_csv(uploaded_file)

# Visualizing the data
fig = px.timeline(df, x_start="Start Time", x_end="End Time", y="Task", color="Task")
fig.update_yaxes(autorange="reversed")
fig.update_layout(height=700, title="Daily Schedule")
st.plotly_chart(fig)