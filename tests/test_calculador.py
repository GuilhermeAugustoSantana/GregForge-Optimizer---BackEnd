from src.calculador import calculaQuantidadeMinerioParaLingote


def test_CalculoDeLigoteSimples():
    meta_lingotes = 10
    minerios = [
        {"name": "Native copper", "mb_value": 25},
        {"name": "Malachite", "mb_value": 35},
    ]

    resultado = calculaQuantidadeMinerioParaLingote(meta_lingotes, minerios)

    assert resultado["minérios necessários"]["Native copper"] == 3
    assert resultado["minérios necessários"]["Malachite"] == 39

    assert resultado["desperdício_mb"] == 0

def test_ResultadoNãoConseguiuCalcularQuantidade():
    meta_lingotes = 1
    minerios = []

    resultado = calculaQuantidadeMinerioParaLingote(meta_lingotes, minerios)

    assert resultado == {
        "Não foi possível calcular a quantidade de minérios necessária para atingir a meta de lingotes."
    }
