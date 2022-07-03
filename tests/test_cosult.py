import pytest 
from ibge_api.data import *

def test_lis_pes():
    for lis_p in list_pesquisas():
        p = lis_p["nome"]
        assert p
