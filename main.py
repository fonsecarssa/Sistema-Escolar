from servicos.persistencia import carregar_dados, salvar_dados
from servicos.utils import menu_principal, menu_operacoes
from modulos.estudantes import (
    incluir_estudante,
    listar_estudante,
    atualizar_estudante,
    excluir_estudante
)
def gerenciarEstudantes(dados_estudantes):
    while True:
        operacao = menu_operacoes('ESTUDANTES')

        if operacao == 1:
            dados_estudantes = incluir_estudante(dados_estudantes)
        elif operacao == 2:
            dados_estudantes = listar_estudante(dados_estudantes)
        elif operacao == 3:
            dados_estudantes = atualizar_estudante(dados_estudantes)
        elif operacao == 4:
            dados_estudantes = excluir_estudante(dados_estudantes)
        elif operacao == 5:
            print('Retornando ao menu principal...')
            return dados_estudantes

        return dados_estudantes 
    
dados_estudantes = carregar_dados()


while True:
    opcao = menu_principal()

    if opcao == 1:
        dados_estudantes = gerenciarEstudantes(dados_estudantes)
    elif opcao in [2, 3, 4, 5]:
        print()
        print('Funcionalidade ainda não implementada.')
        print()
        print('Retornando ao menu principal...')  
        print()
    elif opcao == 6:
        print('Saindo do sistema. Até logo!')
        break
