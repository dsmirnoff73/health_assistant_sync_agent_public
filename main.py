from fastapi import FastAPI
from sync_agent import run_sync

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Health Sync Agent is running."}

@app.post("/sync")
def trigger_sync():
    run_sync()
    return {"status": "ok", "message": "Sync triggered"}