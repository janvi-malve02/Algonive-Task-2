import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Netflix Data Dashboard")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

# Movies vs TV Shows
type_counts = df['type'].value_counts().reset_index()
type_counts.columns = ['type', 'count']

fig = px.bar(
    type_counts,
    x='type',
    y='count',
    title="Movies vs TV Shows on Netflix"
)

st.plotly_chart(fig)