# Sentiment Analysis API 📝🔍

A simple FastAPI-based sentiment analysis service using **NLTK VADER**.  
The API takes text input and returns whether the sentiment is **positive**, **negative**, or **neutral**.

---

## 🚀 Features
- Analyze sentiment of text (`/analyze`)
- Health check endpoint (`/health`)
- Dockerized for easy deployment

---

## 🛠️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api
```

### 2. Build Docker Image
```bash
docker build -t sentiment-api .
```

### 3. Run Container
```bash
docker run -d -p 8000:8000 sentiment-api
```