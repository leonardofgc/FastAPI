from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    # arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.json() == {'message': 'Olá, mundo'}
    assert response.status_code == HTTPStatus.OK


def test_helloword_deve_retornar_o_html():
    client = TestClient(app)
    response = client.get('/helloworld')
    assert response.text == '<b>Hello World</b>'
