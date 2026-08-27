server.py
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Telegram MCP Server is running"}

@app.get("/health")
def health():
    return {"ok": True}
