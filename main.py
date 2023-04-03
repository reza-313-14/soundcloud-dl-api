from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from router import scd


app = FastAPI()
app.include_router(scd.router)

app.mount("/files", StaticFiles(directory="files"), name="files")

@app.middleware('http')
async def add_middle_ware(request: Request, call_next):
    ip = request.client.host
    base_url = request.base_url
    port = request.client.port
    print(f"ip : {ip}\nport : {port}\nurl : {base_url}")
    response = await call_next(request)
    return response
