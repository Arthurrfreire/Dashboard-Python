import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title='Real-Time Data Science Dashboard',
    page_icon='✅',
    layout='wide'
)

# Dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# Top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

# Creating a single-element container
placeholder = st.empty()

# Dataframe filter
filtered_df = df[df['job'] == job_filter].copy()

# Simulate data update
def update_data(filtered_df):
    filtered_df['age_new'] = filtered_df['age'] * np.random.choice(range(1, 5))
    filtered_df['balance_new'] = filtered_df['balance'] * np.random.choice(range(1, 5))
    return filtered_df

# Update and display data
if st.button('Update Data'):
    filtered_df = update_data(filtered_df)
    
    avg_age = np.mean(filtered_df['age_new'])
    count_married = int(filtered_df[(filtered_df["marital"] == 'married')]['marital'].count())
    balance = np.mean(filtered_df['balance_new'])
    
    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value=count_married, delta=-10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value=f"$ {round(balance, 2)}", delta=-round(balance / count_married))
        
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=filtered_df, y='age_new', x='marital')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=filtered_df, x='age_new')
            st.write(fig2)
        
        st.markdown("### Detailed Data View")
        st.dataframe(filtered_df)
