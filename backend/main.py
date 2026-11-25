from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent.parent
WEB_DIR = BASE_DIR / "web"
app = FastAPI(title="Separador Pro Corel", version="1.0.0")
app.mount("/static", StaticFiles(directory=str(WEB_DIR)), name="static")

@app.get("/")
def home():
    return FileResponse(WEB_DIR / "index.html")

@app.get("/api/health")
def health():
    return {"status": "ok", "app": "Separador Pro Corel", "mode": "manual-crop"}
