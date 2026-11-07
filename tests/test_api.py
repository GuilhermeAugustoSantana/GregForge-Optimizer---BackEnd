from fastapi.testclient import TestClient
from app import app


def test_dados_retornados_pelo_calculo_da_API():
    cliente = TestClient(app)
    dados = {
        "metaLingotes": 6,
        "mineriosSelecionados": [
            {"name": "Native copper", "mb_value": 25},
            {"name": "Malachite", "mb_value": 35},
        ],
    }
    resposta = cliente.post("/calcular", json=dados)
    json_resposta = resposta.json()
    assert resposta.status_code == 200
    assert json_resposta["metaLingotes"] == 6
    assert json_resposta["minérios necessários"]["Native copper"] == 1
    assert json_resposta["minérios necessários"]["Malachite"] == 24
    assert json_resposta["desperdício_mb"] == 1


def test_deve_retornar_lista_de_minerios_com_sucesso():
    cliente = TestClient(app)

    resposta = cliente.get("/minerios")
    listaMinerios = resposta.json()

    assert resposta.status_code == 200
    
    assert isinstance(listaMinerios, list)
    assert len(listaMinerios) > 0

    primerioRegistro = listaMinerios[0]

    assert "id" in primerioRegistro
    assert "nome" in primerioRegistro
    assert "mb" in primerioRegistro
