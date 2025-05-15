from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, crud, database

app = FastAPI()

# CORS setup to allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    database.init_db()

@app.get("/jobs")
def get_all_jobs():
    return crud.get_jobs()

@app.post("/jobs")
def create_job(job: models.JobCreate):
    return crud.add_job(job)
