from fastapi import FastAPI
import requests
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Security updates demo running"}