import streamlit as st
import sqlite3
import pandas as pd
from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
st.title("🛒 Olist SQL Chatbot")
question = st.text_input(
    "Ask a question about Olist data:"
)
if st.button("Submit"):

    prompt = f"""
    You are an SQLite expert.

    Database Table: olist_final

    Important:
    Revenue = SUM(price)

    Columns:
    customer_state
    customer_city
    price
    payment_type
    delivery_days
    product_category_name
    freight_value
    order_status
    payment_mode
    
    Use meaningful aliases.
    
    Example:
    SELECT SUM(price) AS total_revenue
    FROM olist_final



    Generate ONLY SQLite query.
    Do not use markdown.

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    sql_query = response.text

 # Remove code blocks if Gemini returns them
    sql_query = sql_query.replace(
        "```sqlite", ""
    )
    sql_query = sql_query.replace(
        "```", ""
    ).strip()
    st.subheader("Generated SQL")
    st.code(sql_query)

    # Create database connection
    conn = sqlite3.connect("olist.db")
    df = pd.read_sql(
        sql_query,
        conn

    )

    conn.close()

    st.subheader("Result")
    st.dataframe(df)