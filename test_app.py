import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    resposta = client.get('/')
    assert resposta.status_code == 200

def test_home_mensagem(client):
    resposta = client.get('/')
    dados = resposta.get_json()
    assert dados['mensagem'] == "Bem-vindo a API FastOrder!"

# =====================================================
# MISSÃO 6.1
def test_soma(client):
    resposta = client.get('/api/resultado?a=10&b=5')
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados['resultado'] == 15