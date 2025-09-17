# API Framework
from fastapi import FastAPI

# Manipulação de dados (se necessário)
import pandas as pd

# Para execução da API
import uvicorn

# Utilitários (se necessário)
import json

seus_dados=pd.read_csv('Dataset.csv')

app= FastAPI(title='Minha api extração')

@app.get('/')
def pagina_principal():
    return {
       "projeto": "Minha API",
        "autor": "Andre Franca",
        "descricao": "API para servir dados de Pokemon",
        "total_registros": len(seus_dados)
    }

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='localhost',port=8000)

@app.get("/dados")
def listar_todos():
    
    """
    Endpoint BÁSICO: Retorna TODAS as entradas do dataset
    Este é o endpoint principal que lista todos os dados
    """
    return seus_dados
