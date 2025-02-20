from fastapi import FastAPI
from src.backend.services import retrieve_relevant_docs

app = FastAPI()

@app.post("/search/")
def search(query: str):
    results = retrieve_relevant_docs(query)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)