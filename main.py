from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# LOAD DATA
df = pd.read_csv("data_clean.csv")

# Simpan ke memory sebagai list of dict
data = df.to_dict(orient="records")

# GET: tampilkan semua data
@app.get("/")
def get_all_data():
    return {
        "total_data": len(data),
        "data": data
    }

# Ngerun API nya, run di terminal
# uvicorn main:app --reload