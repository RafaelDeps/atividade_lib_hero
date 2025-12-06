from fastapi import FastAPI
from lib_hero.util.database import init_db
from lib_hero.controller.hero import router as heroes_router
from lib_hero.controller.team import router as teams_router

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

# Inicializa o banco em memória
init_db()

# Registra os routers da sua biblioteca
app.include_router(heroes_router)
app.include_router(teams_router)

@app.get("/")
def health():
    return {"status": "ok"}
