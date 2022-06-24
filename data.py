from ibge_api.api_pesquisa import *
import json

UF = []  # TODO add ids for each sigla uf


def Queries():
    queries = []  # TODO add url queries values for endpoints options


def ListPesquisas():
    data = ApiData().api_pesquisa()
    json_data = json.loads(str(data))
    return json_data


def GetPesquisa(id_="36"):
    data = Identificador().pesquisa(id_)
    json_data = json.loads(str(data))
    return json_data


def ListIndicadores(id_="36"):
    data = Indicadores().pesquisa(id_)
    json_data = json.loads(str(data))
    return json_data


def GetIndicadores(id_="13", indicador="1"):
    data = Indicadores().indicadores(id_, indicador)
    json_data = json.loads(str(data))
    return json_data


def ListIndicadoresPeriodos(id_="13", periodo=""):
    data = Indicadores().periodos(id_, periodo)
    json_data = json.loads(str(data))
    return json_data


def GetIndicadoresPeriodos(id_="13", periodo="2019", indicador="1"):
    data = Indicadores().periodos_e_indicadores(id_, periodo, indicador)
    json_data = json.loads(str(data))
    return json_data


def ListRanking(id_="10096", indicador="84043", queries=None):
    data = Ranking().indicadores(id_, indicador, queries)
    json_data = json.loads(str(data))
    return json_data


def GetPeriodoRanking(
    id_="10096", indicador="84043", periodo="20200701-20200715", queries=None
):
    data = Ranking().periodos(id_, indicador, periodo, queries)
    json_data = json.loads(str(data))
    return json_data


def ListResultado(id_="13", localidade="11|12"):
    data = Resultado().pesquisa(id_, localidade)
    json_data = json.loads(str(data))
    return json_data


def GetIndicadoresResultado(id_="13", indicador="1", localidade="11|12"):
    data = Resultado().indicador(id_, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data


def GetPeriodoResultado(id_="13", periodo="2020", indicador="1", localidade="11|12"):
    data = Resultado().periodos(id_, periodo, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data


def GetPeriodoIndicadoresResultado(
    id_="13", periodo="2020", indicador="1", localidade="11|12"
):
    data = Resultado().periodos_e_indicadores(id_, periodo, indicador, localidade)
    json_data = json.loads(str(data))
    return json_data

