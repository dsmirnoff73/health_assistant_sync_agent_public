from fastapi import FastAPI
from sync_agent import run_sync
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Health Sync Agent is running."}

@app.post("/sync")
def trigger_sync():
    run_sync()
    return {"status": "ok", "message": "Sync triggered"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
