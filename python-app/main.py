from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import db

app = FastAPI(debug=True)
#do wydarzen
@app.get("/get-wydarzenia")
def get_wydarzenia():
    my_db = db()
    return my_db.get_wydarzenia()

@app.post("/wydarzenie")
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
@app.put("/update_wydarzenie")
async def update_wydarzenie(request: Request):
    wydarzenie_data = await request.json()
    # """
    # Przykładowy payload:
    # {
    #     "ID": 1,
    #     "id_organizatora": 1,
    #     "id_miejsca": 2,
    #     "id_rodzaju": 3,
    #     "nazwa": "Koncert Jazzowy",
    #     "data": "2025-12-15",
    #     "godz_zacz": "19:00:00",
    #     "godz_zak": "23:00:00"
    # }
    # """
    my_db = db()
    result = my_db.update_wydarzenie(wydarzenie_data)
    return JSONResponse(status_code=200, content=result)
@app.delete("/wydarzenie/{id}")
async def delete_wydarzenie(id):
    my_db = db()
    result = my_db.delete_wydarzenie(id)
    return JSONResponse(status_code=200, content=result)
#do miejsc 
@app.get("/get-miejsca")
def get_miejsca():
    my_db = db()
    return my_db.get_miejsca()
@app.post("/miejsce")
async def add_miejsce(request: Request):
    miejsce_data = await request.json()
    ##"""
    ##przykładowy payload:
    ##{
        ##"adres": Szkolna 121,
        ##"miasto": Cyganka,
    ##}
    ##"""
    my_db = db()
    result = my_db.add_miejsce(miejsce_data)
    return JSONResponse(status_code=201, content=result)
@app.put("/update_miejsce/{id}")
async def update_miejsce(id, request: Request):
    miejsce_data = await request.json()
    # """
    # Przykładowy payload:
    # {
    #     "ID": 1,
    #     "adres": Nowa 45,
    #     "miasto": Cyganka
    # }
    # """
    my_db = db()
    result = my_db.update_miejsce(id, miejsce_data)
    return JSONResponse(status_code=200, content=result)
@app.delete("/miejsce/{id}")
async def delete_miejsce(id):
    my_db = db()
    result = my_db.delete_miejsce(id)
    return JSONResponse(status_code=200, content=result)