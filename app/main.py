from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API FastAPI está rodando via Coolify!"}
