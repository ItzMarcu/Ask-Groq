from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data_analysis import analyze_data 
from web_scrape import scrape

app = FastAPI()
origins = ["https://itzmarcu.github.io"]
<<<<<<< HEAD
app.add_middleware(
=======
app.middleware(
>>>>>>> 669adcb (First Layout, no test yet)
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL: str = "https://it.wikipedia.org/wiki/"

# === ROUTES === 
@app.get("/")
def home(): 
    return 200

@app.get("/q")
def ask(parameter: str = None): 
    if not parameter: 
        raise HTTPException(status_code=401, detail="Bad Request, parameter needed")
    
    inner_url = f"{BASE_URL}{parameter}"
    data = scrape(inner_url)

    response = analyze_data(data)
    if type(response) is tuple: 
        return ask(response[0])
    
    return response