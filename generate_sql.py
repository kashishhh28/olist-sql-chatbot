from google import genai
import sqlite3
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
questions=input("Ask you question:")
prompt=f"""
You are an Sqlite Expert.
Database Table: olist_final

Important Business Definitions:
- Revenue = SUM(price)
- Shipping Cost = freight_value

columns:
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

Generate only a sqlite query.

Rules:
1. Do NOT use markdown.
2. Do NOT use ```sql or ```sqlite.
3. Return only pure SQL text.
Questions:
{questions}"""                            #This means the prompt changes according to what the user types.


#Generate sql
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
sql_query=response.text
print("\nGenerated SQL:")
print(sql_query)


#execute sql
conn=sqlite3.connect("olist.db")
df=pd.read_sql(sql_query,conn)
print("\nResult:")
print(df)
conn.close()
