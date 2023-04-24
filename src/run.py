import uvicorn
from fastapi import FastAPI

from src.apps.bot.routers import router as bot_router

app = FastAPI(title='CommaTg API')

app.include_router(bot_router)

uvicorn.run(app, host="localhost", port=9000)
