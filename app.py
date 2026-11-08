from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.calculador import calculaQuantidadeMinerioParaLingote
from src.mapear_lista_minerios import mapearListaMinerios

app = FastAPI()
UrlsPermitidas = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=UrlsPermitidas,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calcular")
def calcular_quantidade_minerio(dados: dict):
    metaLingotes = dados.get("metaLingotes")
    mineriosSelecionados = dados.get("mineriosSelecionados")

    resultado = calculaQuantidadeMinerioParaLingote(metaLingotes, mineriosSelecionados)

    return {
        "metaLingotes": metaLingotes,
        "minérios necessários": resultado["minérios necessários"],
        "desperdicio_mb": resultado["desperdício_mb"],
    }


@app.get("/minerios")
def mostrar_minerios_disponiveis():
    minerios = mapearListaMinerios()

    return minerios
