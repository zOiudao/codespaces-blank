from InquirerPy import prompt

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
