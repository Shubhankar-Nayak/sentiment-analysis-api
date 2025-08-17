from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_text(text: str):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    sentiment = "positive" if compound > 0.05 else "negative" if compound < -0.05 else "neutral"
    return {"sentiment": sentiment, "score": compound}
