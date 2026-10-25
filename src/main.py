"""
TaskTracker - Gerenciador de tarefas via linha de comando (CLI).

Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Lucas Cerqueira Lima

Implementa a "receita lógica" planejada na Fase 1:
menu principal, cadastro de tarefas e visualização das tarefas cadastradas.
"""

from datetime import datetime

# Prioridades aceitas (regra R2). A chave é o que o usuário pode digitar
# (sem diferenciar maiúsculas/minúsculas); o valor é a forma padronizada salva.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

# Ordem de exibição das prioridades na listagem (regra R8).
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}

FORMATO_DATA = "%d/%m/%Y"

LINHA = "=" * 60
SEPARADOR = "-" * 60


def exibir_menu():
    """Mostra as opções disponíveis no menu principal."""
    print()
    print(LINHA)
    print("              TASKTRACKER - Gerenciador de Tarefas")
    print(LINHA)
    print("  [1] Cadastrar nova tarefa")
    print("  [2] Visualizar tarefas cadastradas")
    print("  [3] Sair da aplicação")
    print(LINHA)


# ---------------------------------------------------------------------------
# Validações das regras de negócio
# ---------------------------------------------------------------------------

def validar_titulo(texto):
    """Regra R1: o título não pode ser vazio nem composto só por espaços."""
    return texto.strip() != ""


def validar_prioridade(texto):
    """
    Regra R2: aceita apenas Alta, Média (ou Media) e Baixa.
    Retorna a prioridade padronizada, ou None se for inválida.
    """
    return PRIORIDADES_VALIDAS.get(texto.strip().lower())


def validar_data(texto):
    """Regra R6: a data deve estar no formato DD/MM/AAAA e existir no calendário."""
    try:
        datetime.strptime(texto.strip(), FORMATO_DATA)
        return True
    except ValueError:
        return False


def ler_titulo():
    """Pede o título até que um valor válido seja informado."""
    while True:
        titulo = input("Título: ").strip()
        if validar_titulo(titulo):
            return titulo
        print("Erro: o título da tarefa não pode ficar vazio. Tente novamente.\n")


def ler_prioridade():
    """Pede a prioridade até que uma das opções aceitas seja informada."""
    while True:
        prioridade = validar_prioridade(input("Prioridade (Alta / Média / Baixa): "))
        if prioridade:
            return prioridade
        print("Erro: prioridade inválida. Use Alta, Média ou Baixa.\n")


def ler_data_limite():
    """Pede a data limite até que uma data válida no formato DD/MM/AAAA seja informada."""
    while True:
        data = input("Data limite (DD/MM/AAAA): ").strip()
        if validar_data(data):
            return data
        print("Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 25/10/2026).\n")


# ---------------------------------------------------------------------------
# Funcionalidades do sistema
# ---------------------------------------------------------------------------

def pausar():
    """Aguarda o usuário pressionar Enter antes de voltar ao menu."""
    input("\nPressione Enter para voltar ao menu...")


def cadastrar_tarefa(tarefas, proximo_id):
    """
    Passo a passo do cadastro (Fase 1, seção 3.1).
    Pede os dados, monta a tarefa como dicionário e a salva na lista.
    Retorna o próximo identificador disponível.
    """
    print("\n--- CADASTRAR NOVA TAREFA ---\n")

    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # toda tarefa nasce pendente (regra R4)
    }
    tarefas.append(tarefa)

    print(f'\nTarefa "{titulo}" cadastrada com sucesso! (ID {proximo_id})')
    return proximo_id + 1


def chave_ordenacao(tarefa):
    """
    Regra R8: ordena por prioridade (Alta -> Média -> Baixa) e,
    em caso de empate, pela data limite mais próxima.
    """
    data = datetime.strptime(tarefa["data_limite"], FORMATO_DATA)
    return (ORDEM_PRIORIDADE[tarefa["prioridade"]], data)


def exibir_tarefa(tarefa):
    """Mostra todas as propriedades de uma tarefa de forma legível."""
    descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descrição)"
    print(SEPARADOR)
    print(f"[#{tarefa['id']}] {tarefa['titulo']}")
    print(f"     Descrição  : {descricao}")
    print(f"     Prioridade : {tarefa['prioridade']}")
    print(f"     Data limite: {tarefa['data_limite']}")
    print(f"     Status     : {tarefa['status']}")


def visualizar_tarefas(tarefas):
    """Passo a passo da visualização (Fase 1, seção 3.2)."""
    print("\n--- TAREFAS CADASTRADAS ---\n")

    if not tarefas:
        print("Nenhuma tarefa cadastrada até o momento.")
        return

    for tarefa in sorted(tarefas, key=chave_ordenacao):
        exibir_tarefa(tarefa)
    print(SEPARADOR)
    print(f"Total: {len(tarefas)} tarefa(s), ordenadas por prioridade e data limite.")


def main():
    """Fluxo principal (Fase 1, seção 3.0): repete o menu até o usuário sair."""
    tarefas = []      # lista vazia para armazenar as tarefas
    proximo_id = 1    # contador de identificadores começando em 1

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(tarefas, proximo_id)
            pausar()
        elif opcao == "2":
            visualizar_tarefas(tarefas)
            pausar()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nEncerrando o TaskTracker. Até logo!")
