import requests


"""

api de pesquisa por id: https://servicodados.ibge.gov.br/api/v1/pesquisas/{id}
schema:
    "contexto": "10",
    "descricao": "Perfil dos Municípios Brasileiros - Gestão Pública",
    "id": 1,
    "nome": "MUNIC - Perfil dos Municípios Brasileiros",
    "observacao": "Perfil dos Municípios Brasileiros - Gestão Pública",
    "periodos": [{}]

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
    
    def get_data_periodos(self):
        self.api_data()
        return self.data_api['periodos']
    
    def separate_periods(self):
        self.fonte = list(map(lambda dat: dat['fonte'], self.get_data_periodos()))
        self.nota = list(map(lambda dat: dat['nota'], self.get_data_periodos()))
        self.periodo = list(map(lambda dat: dat['periodo'], self.get_data_periodos()))
        self.publicacao = list(map(lambda dat: dat['publicacao'], self.get_data_periodos()))
        self.versao = list(map(lambda dat: dat['versao'], self.get_data_periodos()))
        return self.fonte, self.nota, self.periodo, self.publicacao, self.versao

    def get_period_fonte(self):
        self.separate_periods()
        return self.fonte

    def get_period_nota(self):
        self.separate_periods()
        return self.nota

    def get_period_periodo(self):
        self.separate_periods()
        return self.periodo

    def get_period_publicao(self):
        self.separate_periods()
        return self.publicacao
    
    def get_period_versao(self):
        self.separate_periods()
        return self.versao
        