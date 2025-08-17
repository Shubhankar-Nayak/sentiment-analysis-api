from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    sentiment: str
    score: float
