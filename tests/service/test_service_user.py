##import unittest

from src.service.service_user import ServiceUser


class TestServiceUser:
    def test_add_user_com_sucesso(self):
        resposta_esperada = "Usuario adicionado"
        service = ServiceUser()
        resposta = service.add_user("Fabricio", "Eng")
        assert resposta == resposta_esperada
    def test_add_user_with_invalid_name(self):
        resposta_esperada = "Usuario invalido"
        service = ServiceUser()
        resposta = service.add_user(55, "Eng")
        assert resposta_esperada == resposta
    def test_user_that_already_exists_in_db(self):
        resposta_esperada = "usuário inválido, nome já existe"
        service = ServiceUser()
        service.add_user("macmf", "astronauta")
        resposta = service.add_user("macmf", "astronauta")
        assert resposta_esperada == resposta
