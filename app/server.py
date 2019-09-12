from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Router, Mount
from starlette.staticfiles import StaticFiles
import os
import uvicorn
from fastai.vision import *
path = Path(__file__).parent


app = Starlette()
app.mount('/static', StaticFiles(directory='app/static')
          
model_path = os.path.join(path,'models')
learn = load_learner(model_path)  
          
@app.route('/')
def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())


if __name__ == "__main__":
    if 'serve' in sys.argv: uvicorn.run(app, host='0.0.0.0', port=8080)
