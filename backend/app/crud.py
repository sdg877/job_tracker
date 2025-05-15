from sqlalchemy.orm import Session
from app.database import SessionLocal, Job as DBJob
from app import models

# Get all job entries
def get_jobs():
    db: Session = SessionLocal()
    jobs = db.query(DBJob).all()
    db.close()
    return jobs

# Add a new job
def add_job(job: models.JobCreate):
    db: Session = SessionLocal()
    db_job = DBJob(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    db.close()
    return db_job
