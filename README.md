# 💬 WhatsApp Chat Intelligence Dashboard

A modern data analytics web app built with **Streamlit** that analyzes WhatsApp chat exports and transforms them into meaningful insights using data science techniques.

It goes beyond basic stats and provides **behavioral, linguistic, and activity intelligence** about conversations.


### 📊 Core Analytics
- Total messages, words, media files, and links
- User-wise message contribution analysis
- Activity intensity over time

### 📈 Time-Based Insights
- Monthly message trends
- Daily activity trends
- Hour-wise peak activity detection
- Weekly behavioral heatmaps

### 👥 User Intelligence
- Most active users ranking
- Percentage contribution per user
- Group vs individual behavior comparison

### 🧠 Text Intelligence
- Word frequency analysis
- Most common words extraction
- WordCloud visualization

### 😀 Emoji & Emotion Signals
- Emoji frequency analysis
- Emoji distribution pie chart

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit ⚡
- Pandas 📊
- Matplotlib 📉
- Seaborn 📈
- WordCloud ☁️
- Regex (text processing)
- URLExtract (link detection)
- Emoji library

---

## 📂 Project Structure

whatsapp-chat-analyzer/
│
├── app.py # Streamlit UI (Dashboard)
├── helper.py # Analytics engine
├── preprocessor.py # Chat parsing & cleaning
├── stop_hinglish.txt # Stopwords file
└── README.md

---

## ⚙️ How It Works

1. Upload WhatsApp chat export (.txt file)
2. Preprocessing module parses:
   - timestamps
   - users
   - messages
3. Feature engineering creates:
   - date/time features
   - periods (hour ranges)
4. Helper functions compute:
   - statistics
   - trends
   - user behavior metrics
5. Streamlit renders interactive dashboard

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py

📊 Example Insights You Can Get
Who is the most active user in the group?
What time is the group most active?
How does conversation flow over time?
Which words dominate conversations?
What emojis are most frequently used?
🧠 Key Concepts Used
Data preprocessing & cleaning
Regex-based text parsing
Feature engineering
Exploratory Data Analysis (EDA)
Data visualization
Basic NLP techniques

📸 Screenshots

<img width="947" height="377" alt="image" src="https://github.com/user-attachments/assets/6d41ef59-35a5-4320-8ea6-fec881b7f790" />
<img width="944" height="439" alt="image" src="https://github.com/user-attachments/assets/e9251fa9-604d-4f96-8f56-c2ca9135ab9a" />
<img width="935" height="416" alt="image" src="https://github.com/user-attachments/assets/1ecadf1e-b291-457e-a6fe-9b7b938929c1" />
<img width="930" height="424" alt="image" src="https://github.com/user-attachments/assets/646fe77e-d5e0-4e39-9a94-77a7fb75f333" />

🚀 Future Improvements
Sentiment analysis of messages
User interaction network graph
AI-based chat summarization
Topic modeling (LDA)
Real-time chat analysis
Deployment on Streamlit Cloud
👨‍💻 Author

Habib Rehman Janwiri

Computer Systems Engineering Student
AI & Machine Learning Enthusiast

📜 License

This project is for educational and learning purposes only.
