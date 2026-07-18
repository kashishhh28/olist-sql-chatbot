# 🛒 Olist SQL Chatbot using Gemini AI

An AI-powered SQL chatbot that converts natural language questions into SQL queries using **Google Gemini AI**, executes them on an **SQLite** database, and displays interactive results with data visualizations.

---

## 🎥 Demo

> Add your demo video here after uploading it to GitHub.

---

## 📸 Screenshots

### 🏠 Home Page

![Home](images/home.png)

---

### 📊 Query Result & Visualization

![Visualization](images/res-vis.png)

---

### 📝 Chat History

![History](images/history.png)

---

### 🗑️ Clear Chat History

![Clear History](images/clearchat.png)

---

## ✨ Features

- 🤖 Natural Language to SQL using Google Gemini AI
- 🔒 SQL Validation (Only SELECT queries are allowed)
- 🗄️ SQLite database integration
- 📊 Interactive data visualization
  - Bar Chart
  - Line Chart
  - Area Chart
- 📑 Displays generated SQL query
- 📋 Displays query results in tabular format
- 📝 Persistent chat history using JSON
- 🗑️ Clear chat history option
- ⚡ Built with Streamlit for an interactive web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- Pandas
- JSON
- python-dotenv

---

## 🏗️ Project Architecture

```
User Question
      │
      ▼
 Google Gemini AI
      │
      ▼
 Generated SQL
      │
      ▼
 SQL Validation
      │
      ▼
 SQLite Database
      │
      ▼
 Pandas DataFrame
      │
      ▼
 Streamlit Dashboard
      │
      ├── Result Table
      ├── Charts
      └── Chat History
```

---

## 📂 Project Structure

```
olist-sql-chatbot/
│
├── app.py
├── generate_sql.py
├── requirements.txt
├── history.json
├── olist.db
├── .env
├── .gitignore
├── images/
│   ├── home.png
│   ├── res-vis.png
│   ├── history.png
│   └── clearchat.png
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/kashishhh28/olist-sql-chatbot.git
```

### 2. Navigate to the project

```bash
cd olist-sql-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

Try asking:

- What is the total revenue?
- Show monthly sales.
- Top 10 product categories by revenue.
- Average delivery days.
- Revenue by customer state.
- Most used payment methods.
- Top cities by total sales.
- Average shipping cost by state.

---

## 🔒 SQL Validation

The chatbot only executes **safe SELECT queries**.

Blocked SQL operations include:

- DROP
- DELETE
- UPDATE
- INSERT
- ALTER
- TRUNCATE
- CREATE

This helps protect the database from unwanted modifications.

---

## 📈 Future Improvements

- Smart chart recommendations
- Download query results as CSV
- Export charts as images
- User authentication
- Multiple database support
- Query history search
- Dashboard analytics

---

## 👩‍💻 Author

**Kashish Rajput**

GitHub: https://github.com/kashishhh28

---

## ⭐ If you found this project useful, consider giving it a star!