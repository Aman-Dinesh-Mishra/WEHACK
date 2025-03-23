from fastapi import FastAPI
from backend.database import engine, Base  
from backend.routers import location, emergency, auth  

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(location.router)
app.include_router(emergency.router)
app.include_router(auth.router) 

@app.get("/")
def read_root():
    return {"message": "Welcome to Women Safety API!"}
