from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Using SQLite for now
DATABASE_URL = "sqlite:///./jobs.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# SQLAlchemy ORM model
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    position = Column(String)
    status = Column(String)
    date_applied = Column(Date)
    notes = Column(String)

# Call this at startup to create tables
def init_db():
    Base.metadata.create_all(bind=engine)
