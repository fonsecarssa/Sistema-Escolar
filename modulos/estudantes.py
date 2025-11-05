from servicos.persistencia import salvar_dados
from servicos.utils import validar_cpf

def incluir_estudante(dados_estudantes):
    print('==========INCLUSÃO=========')
    nome_estudante = str(input('Nome do estudante: ')).strip()

    while not nome_estudante or any(char.isdigit() for char in nome_estudante):
        print('Nome inválido (não pode ser vazio e conter números).Tente novamente')
        nome_estudante = input('Nome do estudante: ').strip()

    cpf_estudante = input('CPF do estudante: ')
    cpf_estudante = validar_cpf(cpf_estudante, dados_estudantes)
    
    codigo_estudante = len(dados_estudantes) + 1
    info_estudantes = {'codigo': codigo_estudante, 'nome': nome_estudante, 'cpf': cpf_estudante}

    dados_estudantes.append(info_estudantes)
    salvar_dados(dados_estudantes)
    print('Estudante inserido com sucesso!')
    input('Pressione ENTER para continuar... ')
    return dados_estudantes


def listar_estudante(dados_estudantes):
    print('========LISTAGEM==========')
      
    if not dados_estudantes:
        print('Nenhum estudante cadastrado.')
    else:
        print('Estudantes cadastrados:')

        for est in dados_estudantes:
            print(f"Código: {est['codigo']}, Nome: {est['nome']}, CPF: {est['cpf']} ")

    input('Pressione ENTER para continuar...')
    return dados_estudantes

def atualizar_estudante(dados_estudantes):
    print('Você escolheu a operação ATUALIZAR')
    print('========ATUALIZAÇÃO========')

    if not dados_estudantes:
        print('Nenhum estudante para atualizar.')
        return dados_estudantes
    
    while True:
        try:
            codigo_estudante = int(input('Código para atualizar: '))
            if 1 <= codigo_estudante <= len(dados_estudantes):
                break
            print('Código inválido')
        except ValueError:
            print('Digite um número válido')

    est = next((e for e in dados_estudantes if e['codigo'] == codigo_estudante), None)
    if not est:
        print('Estudante não encontrado.')
        return
    
    print(f'Atualizando: {est['nome']} (CPF: {est['cpf']})')

    nome = input('Digite o novo nome (ENTER PARA MANTER): ').strip()
    if nome and not any(char.isdigit() for char in nome):
        est['nome'] = nome
    else:
        if nome:
            print('Nome inválido. Mantendo atual...')

    cpf_novo = input('Novo CPF (ENTER PARA MANTER): ').strip()
    if cpf_novo:
        cpf_valido = validar_cpf(cpf_novo,codigo_estudante)
        est['cpf'] = cpf_valido

    salvar_dados(dados_estudantes)
    print('Estudante atualizado com sucesso!')
    input('Pressione ENTER para continuar...')
    return dados_estudantes
                    


def excluir_estudante(dados_estudantes):
    print('Você escolheu a operação EXCLUIR')
    print('========EXCLUSÃO========')

    if not dados_estudantes:
        print(f'Nenhum estudante para excluir.')
        return
    
    while True:
        try:
            codigo_estudante = int(input('Codigo para excluir: '))
            if 1<= codigo_estudante <= len(dados_estudantes):
                break
            print('Código inválido.')
        except ValueError:
            print('Digite um número válido.')

    est = next((e for e in dados_estudantes if e['codigo'] == codigo_estudante), None)
    if not est:
        print('Estudante não encontrado.')
        return
    
    confirm = input(f"Excluir {est['nome']} (CPF: {est['cpf']})? (s/n): ").lower()
    if confirm == 's':
        dados_estudantes.remove(est)
        salvar_dados()
        print('Estudante excluído com sucesso!')
    else:
        print('Exclusão cancelada.')
    
    input("Pressione Enter para continuar...")