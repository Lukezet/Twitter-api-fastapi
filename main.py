from fastapi import FastAPI

app= FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API":" W o r k i n g ! "}