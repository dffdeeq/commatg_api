import uvicorn
from fastapi import FastAPI

from src.bot.router import router as bot_router

app = FastAPI(title='CommaTg API')

app.include_router(bot_router)

uvicorn.run(app, host="0.0.0.0", port=9000)
