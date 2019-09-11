from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Router, Mount
from starlette.staticfiles import StaticFiles

import uvicorn
from fastai.vision import *
path = Path(__file__).parent


app = Starlette()
app.mount('/static', StaticFiles(directory='app/static')

@app.route('/')
def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())


if __name__ == "__main__":
    if 'serve' in sys.argv: uvicorn.run(app, host='0.0.0.0', port=8080)
