from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user('marcelo','test')
resposta = service.add_user('marcelo2','test')
resposta = service.add_user('marcelo','test')


print(resposta)
