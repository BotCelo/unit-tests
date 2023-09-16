import unittest

from src.service.service_user import ServiceUser


class TestServiceUser(unittest.TestCase):
    def test_add_user_com_sucesso(self):
        resposta_esperada = "Usuario adicionado"
        service = ServiceUser()
        resposta = service.add_user("Fabricio", "Eng")
        assert resposta == resposta_esperada
