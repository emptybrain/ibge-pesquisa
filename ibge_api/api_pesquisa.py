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
    def pesquisa(self, pesquisa_id="36"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def indicadores(self, pesquisa_id="36", posicao="1"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{posicao}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(self, pesquisa_id="36", periodo="1"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos_e_indicadores(self, pesquisa_id="36", periodo="1", posicao="1"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{posicao}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()


class Ranking:
    def indicadores(self, pesquisa_id="10096", indicador="84043", queries=None):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{indicador}/ranking?{queries}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(
        self,
        pesquisa_id="10096",
        indicador="84043",
        periodo="20200701-20200715",
        queries=None,
    ):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{indicador}/ranking?{queries}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()


class Resultado:
    def indicadores(self, indicador="", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/-/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos(self, periodo="", indicador="84043", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/-/periodos/{periodo}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def pesquisa(self, pesquisa_id="13", indicador="1", localidade=""):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    def periodos_e_indicadores(
        self, pesquisa_id="13", periodo="", indicador="1", localidade=""
    ):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/periodos/{periodo}/indicadores/{indicador}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()

    # https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa}/resultados/{localidades}
    def pesquisa_e_indicadores(self, pesquisa_id="13", localidade="13"):
        url = f"https://servicodados.ibge.gov.br/api/v1/pesquisas/{pesquisa_id}/resultados/{localidade}"
        req = requests.get(url)
        try:
            return req.text
        except:
            req.raise_for_status()
