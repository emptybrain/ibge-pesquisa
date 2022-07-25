from .api_pesquisa import *
import json

UF = [{
        "RO": 11,
        "AC": 12,
        "AM": 13,
        "RR": 14,
        "PA": 15,
        "AP": 16,
        "TO": 17,
        "MA": 21,
        "PI": 22,
        "CE": 23,
        "RN": 24,
        "PB": 25,
        "PE": 26,
        "AL": 27,
        "SE": 28,
        "BA": 29,
        "MG": 31,
        "ES": 32,
        "RJ": 33,
        "SP": 35,
        "PR": 41,
        "SC": 42,
        "RS": 43,
        "MS": 50,
        "MT": 51,
        "GO": 52,
        "DF": 53,
        }] 


class DataPesquisa(object):
    def list_pesquisas(self):
        data = ApiData().api_pesquisa()
        json_data = json.loads(str(data))
        return json_data
    
    
    def get_pesquisa(self, id_=""):
        data = Identificador().pesquisa(id_)
        json_data = json.loads(str(data))
        return json_data

class DataIndicadores(object):
    def list_indicadores(self, id_=""):
        data = Indicadores().pesquisa(id_)
        json_data = json.loads(str(data))
        return json_data


    def get_indicadores(self, id_="", indicador=""):
        data = Indicadores().indicadores(id_, indicador)
        json_data = json.loads(str(data))
        return json_data

class DataIndicadoresPeriodos(object):
    def list_indicadores_periodos(self, id_="", periodo=""):
        data = Indicadores().periodos_e_indicadores(id_, periodo)
        json_data = json.loads(str(data))
        return json_data


    def get_indicadores_periodos(self, id_="", periodo="", indicador=""):
        data = Indicadores().periodos_e_indicadores(id_, periodo, indicador)
        json_data = json.loads(str(data))
        return json_data

class DataRaking(object):
    def list_ranking(self, id_="", indicador="", queries=None):
        data = Ranking().indicadores(id_, indicador, queries)
        json_data = json.loads(str(data))
        return json_data


    def get_periodo_ranking(self,
        id_="", indicador="", periodo="", queries=None
    ):
        data = Ranking().periodos(id_, indicador, periodo, queries)
        json_data = json.loads(str(data))
        return json_data

class DataResultado(object):
    def list_resultado(self, id_="", localidade=""):
        data = Resultado().pesquisa(id_, localidade)
        json_data = json.loads(str(data))
        return json_data


    def get_indicadores_resultado(self, id_="", indicador="", localidade=""):
        data = Resultado().indicador(id_, indicador, localidade)
        json_data = json.loads(str(data))
        return json_data


    def get_periodo_resultado(self, id_="", periodo="", indicador="", localidade=""):
        data = Resultado().periodos(id_, periodo, indicador, localidade)
        json_data = json.loads(str(data))
        return json_data


    def get_periodo_indicadores_resultado(self,
        id_="", periodo="", indicador="", localidade=""
    ):
        data = Resultado().periodos_e_indicadores(id_, periodo, indicador, localidade)
        json_data = json.loads(str(data))
        return json_data

