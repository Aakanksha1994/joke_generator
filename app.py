from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from joke_generator import JokeGenerator
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
joke_generator = JokeGenerator()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/joke")
async def get_joke():
    joke = joke_generator.get_joke()
    return {"joke": joke if joke else "Failed to fetch joke. Please try again."}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
