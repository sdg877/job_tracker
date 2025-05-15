from pydantic import BaseModel
from datetime import date

# Base model for reuse
class JobBase(BaseModel):
    company_name: str
    position: str
    status: str  # e.g., "Applied", "Interview", etc.
    date_applied: date
    notes: str = ""

# For creating a job (client request)
class JobCreate(JobBase):
    pass

# For returning a job (includes ID)
class Job(JobBase):
    id: int

    class Config:
        orm_mode = True
