from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/login/",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@app.post("/submit/")
async def submit(nm:str=Form(...),pwd:str=Form(...)):
    return {"UserName":nm}