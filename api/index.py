from fastapi import FastAPI
from .config import models, database
from .routes import exp_routes, user_routes, skills_routes
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

routers = [
    exp_routes.router,
    user_routes.router,
    skills_routes.router
]

for router in routers:
    app.include_router(router)
    
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
