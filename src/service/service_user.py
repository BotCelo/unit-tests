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
                    print(x.name)
                    if x.name == name:
                        name_already_exists = True
                        return "usuário inválido, nome já existe"
                if not name_already_exists:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    print(self.store.bd)
                    print([x.name for x in self.store.bd])
                    return "usuario adicionado"
            else:
                print([x.name for x in self.store.bd])
                user = User(name=name, job=job)
                self.store.bd.append(user)
                print(self.store.bd)
                return "Usuário adicionado"
        else:
            return "Usuario invalido"
        print([x.name for x in self.store.bd])

    def remove_user(self, name):
        pass
