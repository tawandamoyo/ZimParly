from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint of API
    """
    return {"message": "Welcome to ZimParli Watch API"}