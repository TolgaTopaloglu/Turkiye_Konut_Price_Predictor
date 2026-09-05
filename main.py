import pickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app=FastAPI()

templates=Jinja2Templates(directory="templates")

with open("TOKI_price_regression.pkl1", "rb") as file:
    model= pickle.load(file)

class TOKI_features(BaseModel):
    bolge: str
    sehir: str
    proje_tipi: str
    proje_durumu: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(features: TOKI_features):

    input_data= pd.DataFrame([features.model_dump()]) #pydantic den dataframe çeviri

    prediction = model.predict(input_data)[0]

    prediction_h = prediction + 122000
    prediction_l = prediction - 122000

    sonuc= f"{prediction_h:.2f} - {prediction_l:.2f}"

    return {
        "prediction": prediction,
        "prediction_low": prediction_l,
        "prediction_high": prediction_h
    }