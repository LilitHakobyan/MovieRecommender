from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Router, Mount
from starlette.staticfiles import StaticFiles

import uvicorn
from fastai.vision import *



app = Starlette()
model_path =  Path('storage/A_MOVIE_RECOMMMENDER/models')
learn = load_learner(model_path)  

@app.route('/')
def index(request):   
    html = 'storage/A_MOVIE_RECOMMMENDER/static/index.html'
    return HTMLResponse(html.open().read())

if __name__ == "__main__":
     uvicorn.run(app, host='0.0.0.0', port=8000)