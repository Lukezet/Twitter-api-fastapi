
#File: models.py
from models import UserLogin, UserBase, User, Genders
from models import Tweet
# FastAPI
from fastapi import FastAPI

app= FastAPI()



@app.get(path="/")
def home():
    return {"Twitter API":" W o r k i n g ! "}