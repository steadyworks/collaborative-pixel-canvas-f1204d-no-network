import asyncio
import json
import os
from datetime import datetime, timezone

import aiosqlite
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
<<<<<< HEAD
allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
======
DB_PATH = os.getenv("DB_PATH", "/tmp/canvas.db")


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS placements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                x INTEGER NOT NULL,
                y INTEGER NOT NULL,
                color TEXT NOT NULL,

class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast(self, message: dict):
        text = json.dumps(message)
        dead = []
        for ws in list(self.active):
            try:
                await ws.send_text(text)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)


manager = ConnectionManager()


@app.on_event("startup")
async def startup():
    await init_db()


@app.get("/api/canvas")
async def get_canvas():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT x, y, color, placer, placed_at
            FROM placements p1
            WHERE id = (
                SELECT MAX(id) FROMsdddddas db:
        await db.execute(
            "INSERT INTO placements (x, y, color, placer, placed_at) VALUES (?, ?, ?, ?, ?)",
            (data.x, data.y, data.color, data.placer, placed_at),
        )
        await db.commit()

    pixel = {
        "type": "pixel",
>>>>>> HEAD