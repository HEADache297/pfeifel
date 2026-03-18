from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from app.agent.agent import create_agent
from fastapi import FastAPI, Depends
from sqlmodel import Session
from .db.database import init_db, get_session
from .db.vector_store import init_qdrant

load_dotenv()

model = init_chat_model("claude-3-haiku-20240307", temperature=0)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()
    init_qdrant()

@app.get("/status")
def read_status(session: Session = Depends(get_session)):
    return {"status": "Database & Vector Store Connected!"}

@app.post('/')
def chat(message: str):
    agent = create_agent()
    agent.invoke({"messages": [("user", message)]}) 
    return {"response": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)