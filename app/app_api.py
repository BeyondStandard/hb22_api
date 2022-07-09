from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import random

#

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_car_type() -> str:
    return random.choice(["electric", "gasoline", "diesel"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_engine")
async def get_engine():
    return {"car_type": get_car_type()}
