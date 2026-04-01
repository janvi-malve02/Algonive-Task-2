import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

st.title("🏠 Airbnb NYC 2019 Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(r"C:\Users\Dell\Desktop\SALES DATA ANALYSIS AND FORECASTING\AB_NYC_2019.csv")

# -----------------------------
# DATA CLEANING
# -----------------------------
df.dropna(inplace=True)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filter Data")

neighbourhood = st.sidebar.multiselect(
    "Select Neighbourhood Group",
    options=df["neighbourhood_group"].unique(),
    default=df["neighbourhood_group"].unique()
)

room_type = st.sidebar.multiselect(
    "Select Room Type",
    options=df["room_type"].unique(),
    default=df["room_type"].unique()
)

filtered_df = df[
    (df["neighbourhood_group"].isin(neighbourhood)) &
    (df["room_type"].isin(room_type))
]

# -----------------------------
# KPI METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Listings", len(filtered_df))
col2.metric("Average Price", f"${filtered_df['price'].mean():.2f}")
col3.metric("Total Reviews", int(filtered_df["number_of_reviews"].sum()))

st.divider()

# -----------------------------
# PRICE DISTRIBUTION
# -----------------------------
st.subheader("💰 Price Distribution")

price_chart = px.histogram(
    filtered_df,
    x="price",
    nbins=50,
    title="Price Distribution"
)

st.plotly_chart(price_chart, use_container_width=True)

# -----------------------------
# ROOM TYPE DISTRIBUTION
# -----------------------------
# =============================
# ROOM TYPE DISTRIBUTION
# =============================

room_counts = filtered_df['room_type'].value_counts().reset_index()

room_counts.columns = ['room_type','count']

room_chart = px.bar(
    room_counts,
    x='room_type',
    y='count',
    color='room_type',
    title='Room Type Distribution'
)

st.plotly_chart(room_chart, use_container_width=True)

# -----------------------------
# NEIGHBOURHOOD PRICE ANALYSIS
# -----------------------------
st.subheader("🏙 Average Price by Neighbourhood")

price_neigh = filtered_df.groupby("neighbourhood_group")["price"].mean().reset_index()

neigh_chart = px.bar(
    price_neigh,
    x="neighbourhood_group",
    y="price",
    color="neighbourhood_group",
    title="Average Price by Neighbourhood"
)

st.plotly_chart(neigh_chart, use_container_width=True)

# -----------------------------
# MAP VISUALIZATION
# -----------------------------
st.subheader("🗺 Listings Map")

map_chart = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="price",
    size="price",
    hover_name="name",
    zoom=10,
    mapbox_style="carto-positron"
)

st.plotly_chart(map_chart, use_container_width=True)