from InquirerPy import prompt
from os import system

def question(msg):
    questions = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Sim', 'Não'],
            'name': 'sim_ou_nao'
        },
    ]

    resposta = prompt(questions)
    print(f"Resposta: {resposta['sim_ou_nao']}")
    return resposta['sim_ou_nao']

def menu_return():
    question = [
        {
            'type': 'list',
            'message': 'Returnar ao menu principal?',
            'choices': ['Retornar', 'Sair'],
            'name': 'sim_ou_nao'
        }
    ]
    
    page = prompt(question)
    if page['sim_ou_nao'] == 'Retornar':
        system('clear')
        return menu_app()        
    else:
        system('clear')
        return print('Sistema encerrado')

def menu_user(msg='Menu Usuários'):
    from .user_crud import Users
    usuarios = Users()
    
    question = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'users'
        },
    ]
    
    page = prompt(question)
    usuarios.create() if page['users'] == 'Cadastrar' else ...
    usuarios.read() if page['users'] == 'Exibir' else ...
    usuarios.update() if page['users'] == 'Editar' else ...
    usuarios.delete() if page['users'] == 'Deletar' else ...
    menu_return () if page['users'] == 'Retornar' else ...
        
def menu_work(msg='Menu Funcionários'):
    from .work_crud import Worker
    funcionarios = Worker()
    
    question = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'work'
        },
    ]
    
    page = prompt(question)
    funcionarios.create() if page['work'] == 'Cadastrar' else ...
    funcionarios.read() if page['work'] == 'Exibir' else ...
    funcionarios.update() if page['work'] == 'Editar' else ...
    funcionarios.delete() if page['work'] == 'Deletar' else ...
    menu_return () if page['work'] == 'Retornar' else ...
    
def menu_driver(msg='Menu Motoristas'):
    from .driver_crud import Drivers
    motoristas = Drivers()
    
    question = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'driver'
        },
    ]
    
    page = prompt(question)
    motoristas.create() if page['driver'] == 'Cadastrar' else ...
    motoristas.read() if page['driver'] == 'Exibir' else ...
    motoristas.update() if page['driver'] == 'Editar' else ...
    motoristas.delete() if page['driver'] == 'Deletar' else ...
    menu_return () if page['driver'] == 'Retornar' else ...
    
def menu_app(msg='Menu principal'):
    from .driver_crud import Drivers
    motoristas = Drivers()
    
    question = [
        {
            'type': 'list',
            'message': msg,
            'choices': ['Usuários', 'Funcionários', 'Motoristas', 'Sair'],
            'name': 'cadastro'
        },
    ]
    
    page = prompt(question)
    if page['cadastro'] == 'Usuários':
        menu_user()
        return menu_return()
    elif page['cadastro'] == 'Funcionários':
        menu_work()
        return menu_return() 
    elif page['cadastro'] == 'Motoristas':
        menu_driver()
        return menu_return()
    else:
        return print('Sistema encerrado')
    
