from sqlalchemy import String, Integer, ForeignKey, Column, create_engine, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import pytz
from datetime import datetime

tmz = pytz.timezone('America/Sao_Paulo')

engine = create_engine('sqlite:///mydb.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(40), nullable=False)
    cpf = Column(String(14), nullable=False)
    work_id = Column(String(16), nullable=False)
    password = Column(String(16), nullable=False)
    create_date = Column(DateTime, default=datetime.now(tmz))
    dr_entry = relationship('DriverEntry', back_populates='user')
    
    def __init__(self, first_name, last_name, cpf, work_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.work_id = work_id
        self.password = password
        
class Work(Base):
    __tablename__ = 'workers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(40), nullable=False)
    work_id = Column(String(16), nullable=False)
    sector = Column(String(16), nullable=False)
    create_date = Column(DateTime, default=datetime.now(tmz))
    dr_entry = relationship('DriverEntry', back_populates='work')
    
    def __init__(self, first_name, last_name, work_id, sector):
        self.first_name = first_name
        self.last_name = last_name
        self.work_id = work_id
        self.sector = sector
        
class Driver(Base):
    __tablename__ = 'drivers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(40), nullable=False)
    cpf = Column(String(14), nullable=False)
    carrier = Column(String(40), nullable=False)
    plate = Column(String(8), nullable=False, unique=True)
    register = Column(Integer, ForeignKey('users.id'))
    create_date = Column(DateTime, default=datetime.now(tmz))
    dr_entry = relationship('DriverEntry', back_populates='driver')
    
    def __init__(self, first_name, last_name, cpf, carrier, plate, register):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.carrier = carrier
        self.plate = plate
        self.register = register
        

class DriverEntry(Base):
    __tablename__ = 'driver_entry'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    work_id = Column(Integer, ForeignKey('workers.id'))
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    entry = Column(DateTime, default=datetime.now(tmz))
    returns = Column(DateTime, nullable=True)
    user = relationship('User', back_populates='dr_entry')
    work = relationship('Work', back_populates='dr_entry')
    driver = relationship('Driver', back_populates='dr_entry')
    
    def __init__(self, user_id, work_id, driver_id):
        self.user_id = user_id
        self.work_id = work_id
        self.driver_id = driver_id

Base.metadata.create_all(engine)
