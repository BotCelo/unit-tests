from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name and job and isinstance(name, str) and isinstance(job, str):
            if self.store.bd:
                for x in self.store.bd:
                    if x.name == name:
                        return "usuário inválido, nome já existe"
                user = User(name=name, job=job)
                self.store.bd.append(user)
                return "usuario adicionado"
            else:
                user = User(name=name, job=job)
                self.store.bd.append(user)
                print(self.store.bd)
                return "Usuário adicionado"
        else:
            return "Usuario invalido"
    def remove_user(self, name):
        if name and isinstance(name, str):
            list_all_names = [x.name for x in self.store.bd]
            if name not in list_all_names:
                return 'usuário não existe'
            index = list_all_names.index(name)
            self.store.bd.pop(index)
            return 'usuário excluído'
        else:
            return "usuário inválido"
