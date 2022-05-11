from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello World"}

@app.get('/test')
def test(request: Request):
    return f"Index is at: {request.url_for('index')}"

@app.get('/json')
def json(request: Request):
    return {
        'index': request.url_for('index'),
        'self': request.url_for('json')
    }

@app.get('/redirect')
async def redir(request: Request):
    return RedirectResponse(request.url_for('index'))
