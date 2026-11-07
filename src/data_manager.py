import json
from pathlib import Path

raizDoProjeto = Path(__file__).resolve().parent.parent
caminhoDoArquivo = raizDoProjeto / "data" / "ores.json"

def CarregarDadosMinerios():
    with open(caminhoDoArquivo, "r") as arquivo:
        minerios = json.load(arquivo)
    return minerios
