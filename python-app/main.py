from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db2 import db

app = FastAPI(debug=True)

@app.get("/get-wydarzenia")
def get_wydarzenia():
    my_db = db()
    return my_db.get_wydarzenia()

@app.post("/add-wydarzenie")
async def add_wydarzenie(request: Request):
    wydarzenie_data = await request.json()
    ##"""
    ##przykładowy payload:
    ##{
        ##"id_organizatora": 1,
        ##"id_miejsca": 2,
        ##"id_rodzaju": 3,
        ##"nazwa": "Koncert Rockowy",
        ##"data": "2025-12-01",
        ##"godz_zacz": "18:00:00",
        ##"godz_zak": "22:00:00"
    ##}
    ##"""
    my_db = db()
    result = my_db.add_wydarzenie(wydarzenie_data)
    return JSONResponse(status_code=201, content=result)
