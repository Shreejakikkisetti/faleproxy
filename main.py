from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Faleproxy"}

@app.get("/proxy")
async def proxy(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text
            }
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))
