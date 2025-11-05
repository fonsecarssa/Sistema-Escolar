# - Sistema de Gerenciamento Escolar Básico

Este é um sistema CRUD (Create, Read, Update, Delete) desenvolvido em Python para gerenciar informações básicas de uma instituição escolar. O projeto utiliza uma arquitetura modular para organizar as funcionalidades e persistir os dados em arquivos JSON.

---

## - Funcionalidades Atuais

O sistema possui um Menu Principal com várias entidades, sendo a funcionalidade de **Estudantes** a única totalmente implementada.

### Módulo Estudantes

*  **INCLUIR:** Cadastra novos estudantes com validação de nome e CPF (unicidade e formato).
*  **LISTAR:** Exibe todos os estudantes cadastrados (Código, Nome e CPF).
*  **ATUALIZAR:** Permite buscar um estudante pelo Código e modificar o Nome e/ou CPF.
*  **EXCLUIR:** Permite remover um estudante pelo Código após confirmação.

### Persistência de Dados

* Os dados são salvos e carregados automaticamente do arquivo `dados/estudantes.json`.
* O sistema trata erros de arquivo não encontrado (`FileNotFoundError`) ou de JSON corrompido, iniciando com uma lista vazia, se necessário.

---

## - Como Rodar o Projeto

### Pré-requisitos

* Python 3.12 instalado.

### Estrutura do Projeto

O projeto é modular e está organizado nas seguintes pastas:

```text
SistemaEscolar/
├── dados/            # Armazenamento de arquivos JSON
├── servicos/         # Funções de utilidade (Menus, Validação, Persistência de dados)
├── modulos/          # Lógica de negócio (CRUD de Estudantes)
└── main.py           # Ponto de entrada e Menu Principal
```

### Execução

Para garantir que as importações modulares (`servicos` e `modulos`) funcionem corretamente, o projeto deve ser executado a partir do terminal na pasta raiz (`SistemaEscolar`).

1.  Abra o terminal na pasta `SistemaEscolar/`.
2.  Execute o arquivo principal:

    ```bash
    python main.py
    ```
---

## - Próximos Passos (To Do)

As seguintes funcionalidades estão prontas para serem implementadas, seguindo o padrão modular já estabelecido:

* [ ] Implementar CRUD completo para **Disciplinas** (`modulos/disciplinas.py`).
* [ ] Implementar CRUD completo para **Professores** (`modulos/professores.py`).
* [ ] Implementar CRUD completo para **Turmas**.
* [ ] Implementar **Matrículas** (Relacionamento entre Estudantes, Disciplinas e Turmas).

---

## 🧑‍💻 Desenvolvedor(a)

* Desenvolvido por: fonsecarssa
