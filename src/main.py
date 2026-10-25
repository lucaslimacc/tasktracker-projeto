"""
TaskTracker - Gerenciador de tarefas via linha de comando (CLI).

Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Lucas Cerqueira Lima

Implementa a "receita lógica" planejada na Fase 1:
menu principal, cadastro de tarefas e visualização das tarefas cadastradas.
"""

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

    titulo = input("Título: ").strip()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

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

    for tarefa in tarefas:
        exibir_tarefa(tarefa)
    print(SEPARADOR)
    print(f"Total: {len(tarefas)} tarefa(s).")


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
