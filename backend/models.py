from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    session_code = Column(String(10), unique=True)
    host_name = Column(String(50))
    chaos_mode = Column(Boolean, default=False)
