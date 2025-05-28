from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Curso FastAPI 2025')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo'}


@app.get('/helloworld', response_class=HTMLResponse)
def hw():
    return """<b>Hello World</b>"""
