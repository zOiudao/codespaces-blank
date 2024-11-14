from user_crud import Users
from work_crud import Worker
from driver_crud import Drivers, EntryDrivers

usuarios = Users()
funcionarios = Worker()
motoristas = Drivers()
ent_saida_moto = EntryDrivers()
if __name__ == '__main__':
    # usuarios.create(5)
    # usuarios.read()
    # usuarios.update(3)
    # usuarios.delete(9)
    # funcionarios.create(5)
    # funcionarios.read()
    # funcionarios.update(5)
    # funcionarios.delete(5)
    # motoristas.create(5)
    # motoristas.read()
    # motoristas.update(5)
    # motoristas.delete(5)
    # ent_saida_moto.entry()
    # ent_saida_moto.returns()
    ent_saida_moto.read()
    pass