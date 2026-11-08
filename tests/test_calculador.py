from src.calculador import calculaQuantidadeMinerioParaLingote


def test_CalculoDeLigoteSimples():
    meta_lingotes = 10
    minerios = [
        {"id": "copper_tetrahedrite_dust_dust", "nome": "Native copper", "mb": 25},
        {"id": "copper_tetrahedrite_dust_small", "nome": "Malachite", "mb": 35},
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
