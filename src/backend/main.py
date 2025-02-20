from fastapi import FastAPI
from pydantic import BaseModel
from src.backend.services import retrieve_and_generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/search/")
def search(request: QueryRequest): 
    results = retrieve_and_generate_response(request.query)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)