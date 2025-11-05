from servicos.persistencia import salvar_dados


def menu_principal():
    global opcao_desejada

    while True:
        print('-----MENU PRINCIPAL-----')
        print('''
        [1] ESTUDANTES
        [2] DISCIPLINAS
        [3] PROFESSORES
        [4] TURMAS
        [5] MATRÍCULAS
        [6] SAIR DO SISTEMA
        ''')

        try:
            opcao_desejada = int(input('Informe a opção desejada: '))
            if 1<= opcao_desejada <= 6:
                break
            print('Opção inválida, tente novamente.')
        except ValueError:
            print('Entrada inválida, digite um número.')

    return opcao_desejada

def menu_operacoes(tipo):

    while True:
        print(f'\n---------MENU DE OPERAÇÕES - {tipo.upper()} -----------')
        print('''
                    [1] INCLUIR
                    [2] LISTAR
                    [3] ATUALIZAR
                    [4] EXCLUIR
                    [5] VOLTAR AO MENU PRINCIPAL
                    ''')
        
        try:
            operacao_desejada = int(input('Informe a operação desejada: ')) 
            if 1 <= operacao_desejada <= 5:
                return operacao_desejada
            print('Opção inválida, tente novamente.')

        except ValueError:
            print('Entrada inválida, tente novamente.')
        
        

def validar_cpf(cpf,dados_estudantes,  codigo_atualizacao=None):
    while True:
            
            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF deve conter 11 dígitos numéricos. Tente novamente.')
                cpf = input('CPF: ')
                continue

            cpf_repetido = any(
                estudante['cpf'] == cpf and (codigo_atualizacao is None or estudante['codigo'] != codigo_atualizacao) 
                for estudante in dados_estudantes
            )
            
            if cpf_repetido:
                print('CPF já cadastrado. Tente novamente.')
                cpf = input('CPF: ')
                continue

            return cpf    