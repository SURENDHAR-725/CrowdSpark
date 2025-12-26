from fastapi import FastAPI
import random, string

from database import engine, SessionLocal
from models import Base, Session

app = FastAPI()
Base.metadata.create_all(bind=engine)


def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


@app.post("/crowdspark/session/create")
def create_session(host_name: str):
    db = SessionLocal()

    code = generate_code()
    session = Session(session_code=code, host_name=host_name)

    db.add(session)
    db.commit()
    db.close()

    return {"session_code": code}
