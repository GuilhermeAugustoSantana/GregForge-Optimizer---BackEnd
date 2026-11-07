import math, itertools


def calculaQuantidadeMinerioParaLingote(meta_lingotes, minerios):

    MenorSobra = 999999
    melhor_combinacao = ()
    resultado = {}

    if minerios == []:
        resultado = {
            "Não foi possível calcular a quantidade de minérios necessária para atingir a meta de lingotes."
        }
        return resultado

    totalMbLingoteMeta = meta_lingotes * 144
    MbValores = [mineiro["mb"] for mineiro in minerios]

    QuantidadeMaxima = math.ceil(totalMbLingoteMeta / min(MbValores))
    quantidadeMinima = math.ceil(totalMbLingoteMeta / max(MbValores))

    for tamanho_grupo in range(quantidadeMinima, QuantidadeMaxima + 1):
        totalcombinacoes = itertools.combinations_with_replacement(
            MbValores, tamanho_grupo
        )
        for combinacoes in totalcombinacoes:
            total_mb = sum(combinacoes)
            if total_mb >= totalMbLingoteMeta:
                sobra = total_mb - totalMbLingoteMeta
                if sobra < MenorSobra:
                    MenorSobra = sobra
                    melhor_combinacao = combinacoes

    resultado = {"minérios necessários": {}, "desperdício_mb": MenorSobra | 0 }
    resultado["minérios necessários"] = {
        minerio["nome"]: melhor_combinacao.count(minerio["mb"])
        for minerio in minerios
    }

    return resultado
