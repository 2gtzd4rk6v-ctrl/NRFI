from fastapi import FastAPI
from fastapi.responses import FileResponse
import json, os, datetime
from .edge import edge_for_nrfi

app=FastAPI(title="NRFI + Kalshi")

@app.get("/api/health")
def health(): return {"ok":True}

@app.get("/api/games")
def games():
    p="data/today.json"
    if not os.path.exists(p): return {"games":[]}
    data=json.load(open(p))
    for g in data.get("games",[]):
        g["edge"]=edge_for_nrfi(g["probability"],g.get("kalshi_yes_bid"),g.get("kalshi_no_bid"))
    return data

@app.get("/")
def home(): return FileResponse("public/index.html")
