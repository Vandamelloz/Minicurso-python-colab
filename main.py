from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from utils.calculos import calcular_media, calcular_mediana, calcular_moda, calcular_desvio
from utils.regressao import regressao_linear
from utils.grafico import gerar_grafico

app = FastAPI(title="API de Estatística para Projetos Acadêmicos")

class Dados(BaseModel):
    valores_x: List[float]
    valores_y: List[float] | None = None

@app.post("/estatisticas")
def estatisticas(dados: Dados):
    x = dados.valores_x
    
    return {
        "media": calcular_media(x),
        "mediana": calcular_mediana(x),
        "moda": calcular_moda(x),
        "desvio_padrao": calcular_desvio(x)
    }

@app.post("/regressao")
def regressao(dados: Dados):
    if not dados.valores_y:
        return {"erro": "Envie valores_y para regressão linear"}

    a, b = regressao_linear(dados.valores_x, dados.valores_y)
    return {"coef_angular": a, "coef_linear": b}

@app.post("/grafico")
def grafico(dados: Dados):
    img = gerar_grafico(dados.valores_x)
    return {"grafico_base64": img}
