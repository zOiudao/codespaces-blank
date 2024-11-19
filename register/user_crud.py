from data.database import User, session
from register.question import question
from rich import print
from rich.table import Table
from faker import Faker
from random import randint
import pytz
from datetime import datetime

tmz = pytz.timezone('America/Sao_Paulo')

fake = Faker('pt_BR')
ftime = '%d/%m/%Y %H:%M:%S'

class Users:
    def create(self, num):
        for _ in range(num):
            first_name = fake.first_name()
            last_name = fake.last_name()
            cpf = fake.cpf()
            work_id = f'TOY-{randint(1500, 1899)}'
            password = fake.password()
            
            try:
                create_user = User(first_name, last_name, cpf, work_id, password)
                session.add(create_user)
                print(f'Cadastro realizado com sucesso! {create_user.first_name}')
            except Exception as e:
                print(e)

        session.commit()
        

    def read(self):
        table = Table(show_lines=True, style='blue')
        cab = ['ID', 'nome', 'cpf', 'hora']
        for i in range(len(cab)):
            table.add_column(cab[i].upper(), no_wrap = True, style='cyan')
        for i in session.query(User).all():
            name = f'{i.first_name} {i.last_name}'
            table.add_row(
                str(i.id).zfill(2),
                name,
                i.cpf,
                i.create_date.strftime(ftime)    
            )
        return print(table)


    def update(self):
        self.read()
        _id = int(input('Digite o ID que deseja editar: '))
        try:
            up = session.query(User).filter_by(id=_id).one()
        except:
            return print('ID não encontrado!')
            
        if up:
            first_name = str(input('Primeiro nome: ')).strip().capitalize()
            if first_name:
                up.first_name = first_name
                up.create_date = datetime.now(tmz)
            last_name = str(input('Sobrenome: ')).strip().capitalize()
            if last_name:
                up.last_name = last_name
                up.create_date = datetime.now(tmz)
        else:
            return print('Usuário não encontrado!')
        
        session.commit()
        return print(f'{up.first_name} \n-Editado com sucesso!')


    def delete(self):
        self.read()
        _id = int(input('Digite o ID que deseja deletar: '))
        try:
            _delete = session.query(User).filter_by(id=_id).one()
        except:
            return print('Usuário não encontrado!')
            
        if _delete:
            conf = question(f'Tem certeza que deseja deletar o cadastro {_delete.first_name}?')
            if conf == 'Sim':
                session.delete(_delete)
                session.commit()
                return print('Usuário deletado com sucesso!')
            else:
                return print('Operação cancelada')
        else:
            return print('Usuário não encontrado!')