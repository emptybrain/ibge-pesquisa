import pytest
from ibge_api.data import DataPesquisa, DataIndicadores, DataIndicadoresPeriodos
from ibge_api.data import DataRaking, DataResultado


# @pytest.mark.skip("Pesquisa skip")
class TestConsultPesquisa:
    def test_lis_pes(self):
        pesquisa = DataPesquisa()
        for lis_p in pesquisa.list_pesquisas():
            p = lis_p["nome"]
            assert p

    def test_get_pes(self):
        pesquisa = DataPesquisa()
        name = pesquisa.get_pesquisa("13")
        assert name["nome"]


# @pytest.mark.skip("Indicadores skip")
class TestConsultIndicadores:
    def test_lis_ind(self):
        indicadores = DataIndicadores()
        for lista in indicadores.list_indicadores("13"):
            name = lista["indicador"]
            assert name

    def test_get_ind(self):
        indicadores = DataIndicadores()
        name = indicadores.get_indicadores("13", "78118")
        assert name[0]["indicador"]


# @pytest.mark.skip("Indicaore e Periodos skip")
class TestIndicadoresPeriodos:
    def test_lis_pe_ind(self):
        periodos = DataIndicadoresPeriodos()
        for lista in periodos.list_indicadores_periodos("13", "2020"):
            id_ = lista["id"]
            assert id_

    def test_get_pe_ind(self):
        periodos = DataIndicadoresPeriodos()
        name = periodos.get_indicadores_periodos("13", "2020", "78118")
        assert name[0]["indicador"]


# @pytest.mark.skip("Ranking skip")
class TestRanking:
    def test_lis_ran(self):
        ranking = DataRaking()
        for lista in ranking.list_ranking("13", "1", queries=None):
            lis = lista["unidade"]
            assert lis

    def test_get_ran_pe(self):
        ranking = DataRaking()
        ran = ranking.get_periodo_ranking("13", "1", "2020", queries=None)
        assert ran[0]["periodo"]


class TestResultado:
    def test_lis_re(self):
        resultado = DataResultado()
        for lista in resultado.list_resultado("13", "11"):
            re = ["localidade"]
            assert re

    def test_get_re_ind(self):
        resultado = DataResultado()
        re = resultado.get_indicadores_resultado("13", "1", "11")
        assert re[0]["res"]
