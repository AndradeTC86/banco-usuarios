from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()
# print(store.bd)

name = 'Thiago'
job = 'Dev'

user = User(name=name, job=job)
# print(user.name)
# print(user.job)

service = ServiceUser()
resultado = service.add_user(name=name, job=job)
print(service.store.bd)
print(resultado)

nome = 'Matheus'

deletar = service.del_user(name=nome)
print(deletar)
