from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/solve")
async def solve(query: str = Query(...)):
    solution = f"Technician short fix for: {query}\n1) Check logs\n2) Verify services\n3) Networking/firewall\n4) Restart if needed."
    sources = ["https://stackoverflow.com/", "https://serverfault.com/"]
    return {"solution": solution, "sources": sources}

@app.get("/")
async def root():
    return {"message": "FastAPI backend running. Use /api/solve?query=your_issue"}

