# my app for car sales 
print("Hello world!")
# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("your_dataset.csv")

# Page header
st.header("Used Car Price Explorer")

# Histogram with optional log scale
if st.checkbox("Show log scale for price histogram"):
    fig1 = px.histogram(df, x="price", nbins=50, title="Car Price Distribution (Log Scale)")
    fig1.update_xaxes(type="log")
else:
    fig1 = px.histogram(df, x="price", nbins=50, title="Car Price Distribution")

st.plotly_chart(fig1)

# Scatterplot
fig2 = px.scatter(df, x="odometer", y="price", color="condition",
                  title="Price vs Odometer Colored by Condition")
st.plotly_chart(fig2)
