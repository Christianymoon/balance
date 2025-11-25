from typing import Union
from fastapi import FastAPI
import requests
import os
import dotenv

dotenv.load_dotenv()


# APITUBE API 

app = FastAPI()
endpoint = "https://api.apitube.io/v1/news/everything"

params = {
    "api_key": os.getenv("API_KEY"),
    "category.id": "medtop:20000344",
    "location.name": "Mexico",
    "language.code": "es",
    "topic.id": "industry.financial_news",
    "sort.by": "published_at",
}

@app.get("/news")
def get_news():
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data['results'] # return a list of news articles dict format
