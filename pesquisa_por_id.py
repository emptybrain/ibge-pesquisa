import requests


"""

api de pesquisa por id: https://servicodados.ibge.gov.br/api/v1/pesquisas/{id}
schema:
    "contexto": "10",
    "descricao": "Perfil dos Municípios Brasileiros - Gestão Pública",
    "id": 1,
    "nome": "MUNIC - Perfil dos Municípios Brasileiros",
    "observacao": "Perfil dos Municípios Brasileiros - Gestão Pública",
    "periodos":

"""


class SearchById(object):
    def __init__(self, search_id=1, json_api=None):
        api = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{search_id}"
        self.json_api = requests.get(api).json()
    
    def api_data(self):
        self.data_api = self.json_api
        return self.data_api

    def get_nome(self):
        self.api_data()
        return self.data_api['nome']

    def get_id(self):
        self.api_data()
        return self.data_api['id']

    def get_observacao(self):
        self.api_data()
        return self.data_api['observacao']

    def get_contexto(self):
        self.api_data()
        return self.data_api['contexto']
    
    def get_descricao(self):
        self.api_data()
        return self.data_api['descricao']
    
    def get_periodos(self):
        self.api_data()
        return self.data_api['periodos']
    
    
