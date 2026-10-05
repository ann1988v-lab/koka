import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from bot import run_bot

load_dotenv()

app = FastAPI(title="SAKURA Bot")


@app.get("/")
async def root():
    return {"status": "ok", "service": "sakura-bot"}


@app.get("/health")
async def health():
    return {"status": "ok"}


async def web():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "3000"))
    config = uvicorn.Config(app, host=host, port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    # Telegram-админка работает полностью внутри бота.
    # Веб-сервер оставлен только как простой health endpoint для BotHost.
    await asyncio.gather(run_bot(), web())


if __name__ == "__main__":
    asyncio.run(main())
