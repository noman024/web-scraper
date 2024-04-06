# main.py
from fastapi import FastAPI
from api import routes

app = FastAPI()

# Including API routes
app.include_router(routes.router)