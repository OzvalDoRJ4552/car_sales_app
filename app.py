import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')  

# Page config
st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Filters")
make = st.sidebar.selectbox("Select Make", df['model'].unique())
min_price, max_price = st.sidebar.slider("Price Range", int(df['price'].min()), int(df['price'].max()), (5000, 30000))

# Filtered data
filtered_df = df[
    (df['model'] == make) & 
    (df['price'] >= min_price) & 
    (df['price'] <= max_price)
]

# Main content
st.title("🚗 Car Sales Dashboard")
st.markdown("Use the filters on the left to explore car listings data.")

# Tabs to organize views
tab1, tab2, tab3 = st.tabs(["Summary", "Visuals", "Raw Data"])

with tab1:
    st.subheader("Summary Stats")
    st.metric("Average Price", f"${filtered_df['price'].mean():,.0f}")
    st.metric("Total Listings", filtered_df.shape[0])

with tab2:
    st.subheader("Interactive Charts")
    fig = px.scatter(filtered_df, x="odometer", y="price", color="condition", title="Price vs Odometer")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Raw Data Table")
    st.dataframe(filtered_df)
