import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WAY_DADOS = os.path.join(BASE_DIR, "dados", "estudantes.json")
ARQUIVO_ESTUDANTES = WAY_DADOS
def carregar_dados():
    try:
        with open(ARQUIVO_ESTUDANTES, "r", encoding='utf-8') as arquivo:
            dados_estudantes = json.load(arquivo)
        print('Dados carregados com sucesso!')
        return dados_estudantes
    except FileNotFoundError:
        print('Arquivo não encontrado. Buscando lista vazia...')
        return []
        dados_estudantes = []
    except json.JSONDecodeError:
        print("Erro na formatação do JSON. Buscando lista vazia...")
        return []

def salvar_dados(dados_estudantes):
    try:
        with open(ARQUIVO_ESTUDANTES, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_estudantes, arquivo, indent=2, ensure_ascii = False)
            print('Dados salvos com sucesso!')
    except Exception as exc:
        print(f'Erro ao salvar: {exc}')

