from .api_pesquisa import *
import json

UF = []  # TODO add ids for each sigla uf

def quedries():
    queries = []  # TODO add url queries values for endpoints options


def list_pesquisas():
    data = ApiData().api_pesquisa()
    json_data = json.loads(str(data))
    return json_data


def get_pesquisa(id_=""):
    data = Identificador().pesquisa(id_)
    json_data = json.loads(str(data))
    return json_data


def list_indicadores(id_=""):
    data = Indicadores().pesquisa(id_)
    json_data = json.loads(str(data))
    return json_data


def get_indicadores(id_="", indicador=""):
    data = Indicadores().indicadores(id_, indicador)
    json_data = json.loads(str(data))
    return json_data


def list_indicadores_periodos(id_="", periodo=""):
    data = Indicadores().periodos(id_, periodo)
    json_data = json.loads(str(data))
    return json_data


def get_indicadores_periodos(id_="", periodo="", indicador=""):
    data = Indicadores().periodos_e_indicadores(id_, periodo, indicador)
    json_data = json.loads(str(data))
    return json_data


def list_ranking(id_="", indicador="", queries=None):
    data = Ranking().indicadores(id_, indicador, queries)
    json_data = json.loads(str(data))
    return json_data


def get_periodo_ranking(
    id_="", indicador="", periodo="", queries=None
):
    data = Ranking().periodos(id_, indicador, periodo, queries)
    json_data = json.loads(str(data))
    return json_data


def list_resultado(id_="", localidade=""):
    data = Resultado().pesquisa(id_, localidade)
    json_data = json.loads(str(data))
    return json_data


def get_indicadores_resultado(id_="", indicador="", localidade=""):
    data = Resultado().indicador(id_, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data


def get_periodo_resultado(id_="", periodo="", indicador="", localidade=""):
    data = Resultado().periodos(id_, periodo, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data


def get_periodo_indicadores_resultado(
    id_="", periodo="", indicador="", localidade=""
):
    data = Resultado().periodos_e_indicadores(id_, periodo, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data

