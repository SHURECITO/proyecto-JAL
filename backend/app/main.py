from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, health
from .db.init_db import init_db
from .db.seed import ensure_seed_admin
from .core.config import settings

app = FastAPI(title="JAL API")

# CORS for local dev and simple deployments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()
    # Seed single admin if not present
    ensure_seed_admin(settings.ADMIN_EMAIL, settings.ADMIN_PASSWORD)

app.include_router(health.router, prefix="/health", tags=["health"]) 
app.include_router(auth.router, prefix="/auth", tags=["auth"])
