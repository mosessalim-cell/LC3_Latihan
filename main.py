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

@app.delete("/data/{item_id}")
def delete_data(item_id: int):
    global data

    for i, item in enumerate(data):
        if item["id"] == item_id:
            deleted = data.pop(i)
            return {
                "message": "Data berhasil dihapus",
                "deleted_data": deleted
            }

    raise HTTPException(status_code=404, detail="Data tidak ditemukan")

# Ngerun API nya, run di terminal
# uvicorn main:app --reload