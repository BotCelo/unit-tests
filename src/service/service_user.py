from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name and job and isinstance(name, str) and isinstance(job, str):
            name_already_exists = False
            if self.store.bd:
                for x in self.store.bd:
                    if x.name == name:
                        name_already_exists = True
                        return "usuário inválido, nome já existe"
                if not name_already_exists:
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
        pass
