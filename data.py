from ibge_api.api import Indicadores


def get_pesquisa():
    data = Indicadores()
    return data.indicadores()


print(get_pesquisa())
