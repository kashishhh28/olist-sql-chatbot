import sqlite3
import pandas as pd
df=pd.read_csv("olist_final.csv")
conn=sqlite3.connect("olist.db")
df.to_sql(
    "olist_final",
    conn,
    if_exists="replace",
    index=False
)
conn.close()