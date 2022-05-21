import requests

"""

api de pesquisa: https://servicodados.ibge.gov.br/api/v1/pesquisas
schema:
id:	 integer (int64)
Identificador da pesquisa

descricao:	string
Descrição da pesquisa

contexto:	string (binary)
Contexto que a pesquisa abrange, 

observacao:	string
Observação sobre a pesquisa

periodos:[[]]

"""


class SearchApi(object):
    def __init__(self, json_api=None):
        api = "https://servicodados.ibge.gov.br/api/v1/pesquisas"
        self.json_api = requests.get(api).json()

    def api_data(self):
        self.data_api = self.json_api
        #api = self.data_api
        self.id_ = list(map(lambda dat: dat['id'], self.data_api))
        self.descricao = list(map(lambda dat: dat['descricao'], self.data_api))
        self.contexto = list(map(lambda dat: dat['contexto'], self.data_api))
        self.observacao = list(map(lambda dat: dat['observacao'], self.data_api))
        self.periodos = list(map(lambda dat: dat['periodos'], self.data_api))
        return self.id_, self.descricao, self.contexto, self.observacao, self.periodos

    def get_id(self):
        self.api_data()
        return self.id_

    def get_descricao(self):
        self.api_data()
        return self.descricao

    def get_contexto(self):
        self.api_data()
        return self.contexto

    def get_observacao(self):
        self.api_data()
        return self.observacao

    def get_periodos(self):
        self.api_data()
        return self.periodos


class GetDataSearch():

    pass
