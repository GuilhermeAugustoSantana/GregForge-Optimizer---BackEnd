import math, itertools


def calculaQuantidadeMinerioParaLingote(meta_lingotes, minerios):

    resultado = {}

    if minerios == []:
        resultado = {
            "Não foi possível calcular a quantidade de minérios necessária para atingir a meta de lingotes."
        }
        return resultado

    totalMbLingoteMeta = meta_lingotes * 144

    MaiorMb = max([minerio["mb"] for minerio in minerios])
    tamanhoTabela = totalMbLingoteMeta + MaiorMb + 1

    dp = [
        (float("inf"), {minerio["id"]: 0 for minerio in minerios})
        for _ in range(tamanhoTabela)
    ]
    dp[0] = (0, {mineiro["id"]: 0 for mineiro in minerios})

    for valor in range(tamanhoTabela):
        desperdicioAtual, mineriosUsados = dp[valor]
        if desperdicioAtual == float("inf"):
            continue

        for minerio in minerios:
            mId = minerio["id"]
            mMb = minerio["mb"]
            proximoValor = valor + mMb

            if proximoValor < tamanhoTabela:
                novoDesperdicio = 0
        
                if proximoValor < totalMbLingoteMeta:
                    novoDesperdicio = totalMbLingoteMeta - proximoValor
                else:
                    novoDesperdicio = proximoValor - totalMbLingoteMeta

                if novoDesperdicio < dp[proximoValor][0]:
                    novaQuantidade = mineriosUsados.copy()
                    novaQuantidade[mId] = novaQuantidade.get(mId, 0) + 1
                    dp[proximoValor] = (novoDesperdicio, novaQuantidade)

    melhorValor = totalMbLingoteMeta
    menorDesperdicioFinal = float("inf")

    for valor in range(totalMbLingoteMeta, tamanhoTabela):
        desperdicioDesseValor, _ = dp[valor]

        if desperdicioDesseValor < menorDesperdicioFinal:
            menorDesperdicioFinal = desperdicioDesseValor
            melhorValor = valor

    desperdicioReal = melhorValor - totalMbLingoteMeta
    mineriosFinaisContagem = dp[melhorValor][1]

    mineriosNecessarios = {}
    for minerio in minerios:
        quantidade = mineriosFinaisContagem.get(minerio["id"], 0)
        if quantidade > 0:
            mineriosNecessarios[minerio["nome"]] = quantidade

    resultado = {"minérios necessários": {}, "desperdício_mb": desperdicioReal}
    resultado["minérios necessários"] = mineriosNecessarios

    return resultado
