from fastapi import FastAPI
from app.models import TextInput, SentimentOutput
from app.sentiment import analyze_text

app = FastAPI(title="Sentiment Analysis API", version="1.0")

@app.post("/analyze", response_model=SentimentOutput)
def analyze_sentiment(input: TextInput):
    return analyze_text(input.text)

@app.get("/health")
async def health_check():
    return {"status": "ok"}