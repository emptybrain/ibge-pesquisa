import requests


class ApiData:
    def api_pesquisa(self):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/"
        req = requests.get(url)
        try:
            return req.text
        except:
            return req.raise_for_status()


class Identificador:
    def pesquisa(self, pesquisa_id="1"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()


class Indicadores:
    def pesquisa(self, pesquisa_id="-"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def indicadores(self, pesquisa_id="-", posicao=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{posicao}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(self, pesquisa_id="-", periodo=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos_e_indicadores(self, pesquisa_id="-", periodo="", posicao=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{posicao}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()


class Ranking:
    def indicadores(self, pesquisa_id="-", indicador="", queries=None):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{indicador}/ranking?{queries}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(
        self,
        pesquisa_id="-",
        indicador="",
        periodo="",
        queries=None,
    ):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{indicador}/ranking?{queries}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()


class Resultado:
    def indicador(self, pesquisa_id="-", indicador="-", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(self, pesquisa_id="-", periodo="", indicador="", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos_e_indicadores(
        self, pesquisa_id="-", periodo="", indicador="1", localidade=""
    ):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def pesquisa(self, pesquisa_id="-", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()
