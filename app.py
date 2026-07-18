import streamlit as st
import sqlite3
import pandas as pd
from google import genai
from dotenv import load_dotenv
import os
import json

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🛒 Olist SQL Chatbot")
if "history" not in st.session_state:

    if os.path.exists("history.json"):

        with open("history.json", "r") as file:
            st.session_state.history = json.load(file)

    else:
        st.session_state.history = []

question = st.text_input("Ask a question about Olist data:")

# -----------------------------
# SQL Validation Function
# -----------------------------
def validate_sql(sql_query):

    # Convert query to lowercase and remove extra spaces
    query = sql_query.lower().strip()

    # Allow only SELECT queries
    if not query.startswith("select"):
        return False

    # Dangerous SQL keywords
    forbidden = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate",
        "create"
    ]

    # Check if any forbidden keyword exists
    for word in forbidden:
        if word in query:
            return False

    # Query is safe
    return True


# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit"):

    prompt = f"""
    You are an SQLite expert.

    Database Table: olist_final

    Important Business Definitions:
    - Revenue = SUM(price)
    - Shipping Cost = freight_value

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

    Rules:
    1. Use only the above columns.
    2. Use meaningful aliases.
    3. Generate ONLY SQLite query.
    4. Do NOT use markdown.
    5. Do NOT explain anything.
    6. Return only SQL.

    Example:
    SELECT SUM(price) AS total_revenue
    FROM olist_final;

    Question:
    {question}
    """

    # Generate SQL
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    sql_query = response.text

    # Remove markdown if Gemini returns it
    sql_query = sql_query.replace("```sqlite", "")
    sql_query = sql_query.replace("```", "").strip()

    # -----------------------------
    # Validate SQL
    # -----------------------------
    if validate_sql(sql_query):

        try:

            # Execute SQL
            with sqlite3.connect("olist.db") as conn:
                 df = pd.read_sql(sql_query, conn)
            st.session_state.current_df = df
            st.session_state.current_sql = sql_query

            
            st.session_state.history.append(
                {
                    "question": question,
                    "sql": sql_query,
                    "result": df.to_dict(orient="records")
                    }
            
            )
            with open("history.json", "w") as file:
                json.dump(st.session_state.history, file, indent=4)

        except Exception as e:
            st.error(f"Database Error: {e}")

    else:
        st.error("❌ Unsafe SQL query detected! Only SELECT queries are allowed.")
if "current_sql" in st.session_state:
    st.subheader("Generated SQL")
    st.code(st.session_state.current_sql, language="sql")
if "current_df" in st.session_state:

    st.subheader("Result")
    st.dataframe(st.session_state.current_df)

    if len(st.session_state.current_df.columns) >= 2:

        st.subheader("📊 Visualization")

        chart_type = st.selectbox(
            "Choose Chart Type",
            ["Bar Chart", "Line Chart", "Area Chart"]
        )

        chart_data = st.session_state.current_df.set_index(
            st.session_state.current_df.columns[0]
        )

        if chart_type == "Bar Chart":
            st.bar_chart(chart_data)

        elif chart_type == "Line Chart":
            st.line_chart(chart_data)

        elif chart_type == "Area Chart":
            st.area_chart(chart_data)

    else:
        st.info("Visualization is available only when the query returns at least two columns.")
st.divider()


if st.session_state.history:

    st.header("📝 Chat History")

    for chat in st.session_state.history:

        st.write("### 👤 You")
        st.write(chat["question"])

        st.write("### 🤖 Generated SQL")
        st.code(chat["sql"], language="sql")

        st.write("### 📊 Result")
        history_df = pd.DataFrame(chat["result"])
        st.dataframe(history_df)

        st.divider()

if st.button("🗑️ Clear Chat History"):

    st.session_state.history = []

    if "current_df" in st.session_state:
        del st.session_state.current_df

    if "current_sql" in st.session_state:
        del st.session_state.current_sql

    with open("history.json", "w") as file:
        json.dump([], file)

    st.rerun()

