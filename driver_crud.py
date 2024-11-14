from data.database import Driver, User, DriverEntry, Work, session
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
transportadora = [
    "Translog Brasil",
    "Carga Rápida",
    "FreteSul",
    "Transportes União",
    "Rápido Express",
    "Transporte Rodocargo",
    "Logística Total",
    "Via Carga",
    "Expressa Cargas",
    "Transporte Nacional"
]

class Drivers:
    def create(self, num):
        for _ in range(num):
            first_name = fake.first_name()
            last_name = fake.last_name()
            cpf = fake.cpf()
            carrier = choice(transportadora)
            plate = fake.license_plate()
            register = choice([i.id for i in session.query(User).all()])
            
            try:
                create = Driver(first_name, last_name, cpf, carrier, plate, register)
                session.add(create)
                print(f'{first_name} Criado com sucesso!')
            except:
                return print(f'Não foi possivel criar o registro de {first_name}')
            
        session.commit()
        return
    
    
    def read(self):
        table = Table(show_lines = True)
        cab = ['id', 'nome', 'cpf', 'transportadora', 'placa', 'hora']
        for i in range(len(cab)):
            table.add_column(cab[i].upper(), no_wrap=True)
        for i in session.query(Driver).all():
            nome = f'{i.first_name} {i.last_name}'
            table.add_row(
                str(i.id).zfill(2),
                nome,
                i.cpf,
                i.carrier,
                i.plate,
                i.create_date.strftime(ftime)
            )
        return print(table)
    
    
    def update(self, _id):
        self.read()
        try:
            up = session.query(Driver).filter_by(id=_id).one()
        except:
            return print('Motorista não encontrado')
        
        if up:
            first_name = str(input(f'Para editar o nome {up.first_name} \n-Digite o novo nome: ')).strip().capitalize()
            if first_name:
                up.first_name = first_name
                up.create_date = datetime.now(tmz)
            last_name = str(input(f'Para editar o sobrenome {up.last_name} \n-Digite novo sobrenome: ')).strip().capitalize()
            if last_name:
                up.last_name = last_name
                up.create_date = datetime.now(tmz)
            carrier = str(input(f'Para editar a transporadora {up.carrier} \n-Digite a nova transportadora: ')).strip().capitalize()
            if carrier:
                up.carrier = carrier
                up.create_date = datetime.now(tmz)
            plate = str(input(f'Para editar a placa {up.plate} \n-Digite a nova placa: ')).strip().upper()
            if plate:
                up.plate = plate
                up.create_date = datetime.now(tmz)
            session.commit()
            
        return print(f'{up.first_name} Editado com sucesso!')
    
    
    def delete(self, _id):
        self.read()
        try:
            d = session.query(Driver).filter_by(id=_id).one()
        except:
            return print('Motorista não encontrado!')
        
        if d:
            res = question(f'Tem certeza que deseja deletar o motorista {d.first_name} {d.last_name}?')
            if res == 'Sim':
                session.delete(d)
                session.commit()
                return print('Motorista deletado com sucesso!')
            else:
                return print('Operação cancelada!')
            

class EntryDrivers:
    def entry(self):
        user_id = choice([i.id for i in session.query(User).all()])
        work_id = choice([i.id for i in session.query(Work).all()])
        driver_id = choice([i.id for i in session.query(Driver).all()])
        entry = DriverEntry(user_id, work_id, driver_id)
        session.add(entry)
        session.commit()
        return print(f'Entrada de {entry.driver.first_name} registrada com sucesso \n-{entry.entry}')
    
    
    def returns(self):
        ret_id = choice([i.id for i in session.query(DriverEntry).all()])
        try:
            r = session.query(DriverEntry).filter_by(id=ret_id).one()
        except:
            return print('Entrada não encontrada!')
        
        if not r.returns:
            r.returns = datetime.now(tmz)
            session.commit()
            return print(f'Saída registrada com sucesso! \n-{r.driver.first_name} {r.returns.strftime(ftime)}')
        else:
            return print(f'Saída de {r.driver.first_name} já estava registrada às {r.returns.strftime(ftime)}')
        
    
    def read(self):
        table = Table(show_lines=True, style='blue')
        cab = [
            'id', 'nome responsavel', 'setor', 'nome motorista', 
            'transportadora', 'placa', 'hora entrada', 'hora saída'
        ]
        for i in range(len(cab)):
            table.add_column(cab[i].upper(), no_wrap = True, style='cyan')
        for i in session.query(DriverEntry).all():
            if i.returns:
                table.add_row(
                    str(i.id).zfill(2),
                    i.work.first_name,
                    i.work.sector,
                    i.driver.first_name,
                    i.driver.carrier,
                    i.driver.plate,
                    i.entry.strftime(ftime),
                    i.returns.strftime(ftime)
                )
            else:
                table.add_row(
                    str(i.id).zfill(2),
                    i.work.first_name,
                    i.work.sector,
                    i.driver.first_name,
                    i.driver.carrier,
                    i.driver.plate,
                    i.entry.strftime(ftime),
                    'Aguardando a saída'
                )
        return print(table)
        