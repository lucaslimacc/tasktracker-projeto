# TaskTracker

Gerenciador de tarefas via linha de comando (CLI), desenvolvido em Python como projeto cumulativo da disciplina **Bootcamp II**.

O TaskTracker centraliza o registro e a consulta das tarefas do dia a dia em um único lugar, com regras claras de preenchimento: toda tarefa precisa de um título e de uma prioridade válida, e a listagem já mostra o que deve ser feito primeiro.

## Funcionalidades

- **Cadastrar tarefas** com título, descrição, prioridade e data limite
- **Visualizar as tarefas cadastradas**, ordenadas por prioridade (Alta → Média → Baixa) e, em caso de empate, pela data limite mais próxima
- **Validar os dados no momento da digitação**, pedindo a informação de novo quando ela é inválida
- Aviso claro quando ainda não há nenhuma tarefa cadastrada

## Regras de negócio

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas. |
| Descrição | Opcional, texto livre. |
| Prioridade | Aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas de minúsculas. |
| Data limite | Formato `DD/MM/AAAA`, e precisa ser uma data que existe no calendário. |
| Status | Definido automaticamente como `Pendente` no cadastro. |

## Tecnologias utilizadas

- **Python 3** (somente a biblioteca padrão, sem dependências externas)
- **Git** para versionamento
- **GitHub** para hospedagem do repositório

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico da Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação
```

## Instalação

1. Tenha o **Python 3.8 ou superior** instalado. Para verificar:

   ```bash
   python --version
   ```

2. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/lucaslimacc/tasktracker-projeto.git
   cd tasktracker-projeto
   ```

Não é preciso instalar nenhuma biblioteca adicional.

## Como executar

Na pasta raiz do projeto:

```bash
python src/main.py
```

> No Linux e no macOS, use `python3` no lugar de `python`.

## Exemplo de uso

```
============================================================
              TASKTRACKER - Gerenciador de Tarefas
============================================================
  [1] Cadastrar nova tarefa
  [2] Visualizar tarefas cadastradas
  [3] Sair da aplicação
============================================================
Escolha uma opção: 1

--- CADASTRAR NOVA TAREFA ---

Título:
Erro: o título da tarefa não pode ficar vazio. Tente novamente.

Título: Estudar comandos Git
Descrição (opcional): Revisar add, commit e push
Prioridade (Alta / Média / Baixa): urgente
Erro: prioridade inválida. Use Alta, Média ou Baixa.

Prioridade (Alta / Média / Baixa): alta
Data limite (DD/MM/AAAA): 20/10/2026

Tarefa "Estudar comandos Git" cadastrada com sucesso! (ID 1)
```

## Roteiro do projeto

| Fase | Entrega | Situação |
|---|---|---|
| 1 | Planejamento lógico e algoritmo em português | Concluída |
| 2 | Repositório no GitHub e implementação em Python | Atual |
| 3 | Containerização com Docker, testes e deploy | Próxima |

## Autor

**Lucas Cerqueira Lima**
Ciência de Dados e Machine Learning · Bootcamp II
