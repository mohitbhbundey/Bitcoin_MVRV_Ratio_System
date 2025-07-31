import streamlit as st
import pandas as pd
import psycopg2

def load_data():
    conn = psycopg2.connect("dbname=mvrv user=postgres password=admin")
    df = pd.read_sql("SELECT * FROM mvrv_ratio ORDER BY timestamp", conn)
    return df

st.title("Bitcoin MVRV Dashboard")
df = load_data()
st.line_chart(df.set_index("timestamp")["mvrv"])
