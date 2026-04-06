# 🤖 Aarambh Chatbot — Terminal AI Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/NLP-spaCy-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/API-OpenWeather-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🌟 Project Overview

**Aarambh Chatbot** is an intelligent, terminal-based AI assistant developed using Python that leverages Natural Language Processing (NLP) to understand and respond to user queries in a human-like manner.

The chatbot integrates multiple functionalities into a single unified system, including real-time weather updates, mathematical computations, date and time interpretation, and general knowledge retrieval. By combining NLP techniques with API integration and modular logic design, Aarambh Chatbot is capable of delivering accurate and context-aware responses.

It uses powerful libraries such as spaCy for language processing, SymPy for mathematical evaluation, dateparser for natural date understanding, and Wikipedia API for knowledge retrieval, making it a practical demonstration of real-world AI application in a lightweight terminal environment.

---

### ✨ Capabilities:


* 🌦️ Weather updates
* 🧮 Mathematical calculations
* 📅 Date & time queries
* 📚 General knowledge questions
* 💬 Basic conversations

---

## 🎯 Objective

✔ Build an intelligent terminal-based chatbot

✔ Implement NLP-based intent detection

✔ Integrate real-time APIs (Weather)

✔ Solve mathematical expressions dynamically

✔ Provide human-like interaction experience

---

## 🏗️ Architecture

### 🔍 Architecture Highlights

* 👤 User interacts via **Terminal Interface**
* 🧠 NLP processing using **spaCy**
* 🌐 API calls handled via **requests**
* ⚙ Logic modules handle:

  * 🌦️ Weather
  * 🧮 Math
  * 📅 Date
  * 📚 Knowledge

---

## 📁 Project Structure

```text
aarambh_chatbot/
│
├── aarambh_chatbot.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Tech Stack

| Tool       | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| spaCy      | NLP & Intent Detection    |
| dateparser | Natural Language Dates    |
| SymPy      | Math Computation          |
| Wikipedia  | Knowledge Retrieval       |
| requests   | API Integration           |

---

## 📦 Features Breakdown

### 🌦️ Weather Module

* Fetches real-time weather data
* Uses OpenWeatherMap API
* Supports city-based queries

---

### 🧮 Math Module

* Solves expressions dynamically
* Powered by SymPy
* Handles complex calculations

---

### 📅 Date & Time Module

* Provides current date & time
* Understands natural phrases
  *(e.g., "tomorrow", "day after tomorrow")*

---

### 📚 Knowledge Module

* Fetches answers from Wikipedia
* Handles general knowledge queries

---

### 💬 Conversation Module

* Greetings (Hello, Hi)
* Thank you responses
* Exit commands

---

## 🔄 Workflow

```text
┌──────────────────────┐
│ 👤 User Input (Text) │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 🧠 NLP Processing (spaCy)    │
│ Tokenization & Parsing       │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 🎯 Intent Detection          │
│ (Weather / Math / Date / GK) │
└─────────┬────────────────────┘
          │
          ▼
┌────────────────────────────────────────────┐
│ ⚙️ Processing Modules                     │
│  ├── 🌦️ Weather Module (API Call)         │
│  ├── 🧮 Math Module (SymPy)               │
│  ├── 📅 Date Module (dateparser)          │
│  ├── 📚 Knowledge Module (Wikipedia)      │
│  └── 💬 Chat Module                      │
└─────────┬──────────────────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 📤 Response Generation       │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────┐
│ 💬 Output to User    │
└──────────────────────┘
```

---

## 🚀 Getting Started

### 🔹 Clone Repository

```bash
git clone https://github.com/Chaitanya5068/python_chatbot_Aarambh
cd aarambh_chatbot
```

---

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

### OR (Manual Install)

```bash
pip install spacy wikipedia sympy dateparser requests
```

---

### 🔹 Configure API Key

Open `aarambh_chatbot.py` and add:

```python
WEATHER_API_KEY = "your_api_key_here"
```

---

### 🔹 Run Chatbot

```bash
python aarambh_chatbot.py
```

---

## 💡 Sample Queries

* 🌦️ What's the weather in Pune?
* 🌧️ Will it rain in Mumbai today?
* 🧮 What is 25 * 4 + 2?
* 👑 Who is Rani Lakshmi Bai?
* ⏰ What is the time now?
* 📅 Tell me the date of tomorrow

---

## 📊 Outputs

✔ Weather Information

✔ Mathematical Results

✔ Date & Time Responses

✔ Wikipedia-based Answers

✔ Conversational Replies

---
## 📸 Sample Output
<img width="1918" height="998" alt="Ac6" src="https://github.com/user-attachments/assets/8a838a25-4c84-4bce-886b-890eb3ccb168" />
<img width="1919" height="1013" alt="Ac7" src="https://github.com/user-attachments/assets/a4a205e4-bc12-4f00-9986-35a300af832e" />

---

## 🔐 Best Practices Followed

✅ Modular Logic Design

✅ Clean Code Structure

✅ API Integration

✅ Error Handling

✅ User-Friendly Responses

---

## 🧠 Key Learnings

* NLP using spaCy
* API integration in Python
* Handling natural language inputs
* Building terminal-based AI assistants

---

## 👨‍💻 Author

**Chaitanya Bhosale**

🔗 GitHub: https://github.com/Chaitanya5068

🔗 LinkedIn: https://www.linkedin.com/in/chaitanya-bhosale

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📌 Note

This project is created for **educational purposes** and demonstrates a basic AI chatbot using Python and NLP.
