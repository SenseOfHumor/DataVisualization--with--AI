```python
import streamlit as st
import pandas as pd
from app import csv_data
import plotly.express as px

uploaded_file = csv_data()
df = pd.read_csv(uploaded_file)

fig = px.timeline(
    df,
    x_start="Start Time",
    x_end="End Time",
    y="Task",
    color="Task",
)

fig.update_layout(
    title="Timeline of Tasks",
    xaxis_title="Time",
    yaxis_title="Task",
)

st.plotly_chart(fig)
```