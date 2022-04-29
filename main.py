from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str

        
sentiment_detection = pipeline("sentiment-analysis", 
                               "blanchefort/rubert-base-cased-sentiment")


app = FastAPI()
sentiment_detection = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello UrFU"}


print(sentiment_detection("Привет! Как дела?"))
print(sentiment_detection("Привет! Я не люблю машинное обучение!"))
print(sentiment_detection("Привет! Я люблю машинное обучение!"))


@app.post("/predict/") 
def predict(item: Item):
    if item.text != "":
        return sentiment_detection(item.text)[0]
    else: 
        return {"message": "Введите текст"}
