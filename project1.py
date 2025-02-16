 
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException

app = FastAPI()


@app.post("/run")
async def run_task(task: str):
    return {"status": "success", "task": task}

@app.get("/read")
async def read_file(path: str):
    if not path.startswith("/data/"):
        raise HTTPException(status_code=400, detail="Access to files outside /data is not allowed.")
    try:
        with open(path, "r") as f:
            content = f.read()
        return JSONResponse(content=content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
