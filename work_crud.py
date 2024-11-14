from data.database import Work, session
from question import question
from rich import print
from rich.table import Table
from faker import Faker
from random import randint, choice
import pytz
from datetime import datetime

tmz = pytz.timezone('America/Sao_Paulo')

fake = Faker('pt_BR')
ftime = '%d/%m/%Y %H:%M:%S'
sectors = ['TKL', 'ADM', 'CQ', 'PRODUÇÃO', 'MANUTENÇÃO']

class Worker:        
    def create(self, num):
        for _ in range(num):
            first_name = fake.first_name()
            last_name = fake.last_name()
            work_id = f'TOY-{randint(1500, 1899)}'
            sector = choice(sectors)
            try:
                create = Work(first_name, last_name, work_id, sector)
                session.add(create)
                print(f'{create.first_name} Cadastrado com sucesso!')
            except:
                return print('Não foi possível realizar o cadastro!')
            
            session.commit()
        return


    def read(self):
        table = Table(show_lines=True)
        cab = ['id', 'nome', 'funcional', 'setor', 'hora']
        for i in range(len(cab)):
            table.add_column(cab[i].upper(), no_wrap=True)
        for i in session.query(Work).all():
            nome = f'{i.first_name} {i.last_name}'
            table.add_row(
                str(i.id).zfill(2),
                nome,
                i.work_id,
                i.sector,
                i.create_date.strftime(ftime)
            )
        return print(table)


    def update(self, _id):
        self.read()
        try:
            up = session.query(Work).filter_by(id=_id).one()
        except:
            return print('Funcionário não encontrado')
            
        if up:
            first_name = str(input('Digite o primeiro nome: ')).capitalize().strip()
            if first_name:
                up.first_name = first_name
                up.create_date = datetime.now(tmz)
            last_name = str(input('Digite sobrenome: ')).capitalize().strip()
            if last_name:
                up.last_name = last_name    
                up.create_date = datetime.now(tmz)        
        else:
            return print('Funcionário não encontrado')
        
        session.commit()
        return print(f'{up.first_name} -Atualizado com sucesso!')
    
    
    def delete(self, _id):
        self.read()
        try:
            d = session.query(Work).filter_by(id=_id).one()
        except:
            return print('Funcionário não encontrado')
        
        if d:
            conf = question(f'Tem certeza que deseja deletar o cadastro de {d.first_name}?')
            if conf == 'Sim':
                session.delete(d)
                session.commit()
                return print('Funcionário deletado com sucesso!')
            else:
                return print('Operação cancelada!')
        
            