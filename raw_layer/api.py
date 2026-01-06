# raw_layer/api.py
"""
raw_layer/api.py
Módulo responsável pela comunicação com a API REST local.
Este módulo fornece funções utilitárias para realizar requisições HTTP
GET a um servidor API executado localmente na porta 8000.
Attributes:
    API_BASE_URL (str): URL base da API local (http://localhost:8000)
Functions:
    fetch(endpoint, params=None): Realiza uma requisição GET à API e retorna
                                   a resposta em formato JSON.
"""
import requests

API_BASE_URL = "http://localhost:8000"

# Faz uma requisição GET à API e retorna a resposta em formato JSON.
def fetch(endpoint, params=None):
    response = requests.get(
        f"{API_BASE_URL}/{endpoint}",
        params=params
    )
    response.raise_for_status()
    return response.json()
