# 🛒 Olist SQL Chatbot

An AI-powered Text-to-SQL chatbot that converts plain English 
questions into SQL queries using Google Gemini API and executes 
them on the Olist Brazilian E-Commerce database.

## Demo
![Chatbot Demo](demo.png)

## How It Works
1. User types a business question in plain English
2. Gemini API generates a SQLite query automatically
3. Query executes on Olist SQLite database
4. Results displayed instantly on Streamlit

## Example Questions
- "Most preferred payment method"
- "Which state generates highest revenue?"
- "Top 5 product categories by sales"
- "Average delivery days by state"
- "How many orders were delivered late?"
- "Total revenue by city"

## Tools Used
- Python
- Google Gemini API (gemini-2.5-flash)
- SQLite
- Pandas
- Streamlit
- Prompt Engineering
- Text-to-SQL Generation

## Project Structure
