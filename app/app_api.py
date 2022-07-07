from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import get_car_type
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_engine")
async def get_engine():
    return {"car_type": get_car_type()}
