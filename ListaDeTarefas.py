import os

ARQUIVO = "tarefas.txt"

def salvar_tarefas(lista_tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for tarefa in lista_tarefas:
            linha = f"{tarefa['descricao']}|{tarefa['concluida']}\n"
            arquivo.write(linha)

def carregar_tarefas():
    lista = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split("|")
                if len(partes) == 2:
                    descricao = partes[0]
                    concluida = partes[1] == "True"
                    lista.append({"descricao": descricao, "concluida": concluida})
    return lista


lista_tarefas = carregar_tarefas()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Marcar como concluída")
    print("5 - Sair")
    
    resposta = input("Escolha uma opção: ")

    if resposta == "1":
        descricao = input("Digite a tarefa que você deseja adicionar: ")
        tarefa = {"descricao": descricao, "concluida": False}
        lista_tarefas.append(tarefa)
        salvar_tarefas(lista_tarefas)
        print("Tarefa adicionada com sucesso!")

    elif resposta == "2":
        for i, tarefa in enumerate(lista_tarefas):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(f"{i + 1}. {status} {tarefa['descricao']}")
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            removida = lista_tarefas.pop(indice)
            salvar_tarefas(lista_tarefas)
            print(f"Tarefa '{removida['descricao']}' removida!")
        else:
            print("Número inválido.")

    elif resposta == "3":
        print("\n--- SUAS TAREFAS ---")
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(lista_tarefas):
                status = "[x]" if tarefa["concluida"] else "[ ]"
                print(f"{i + 1}. {status} {tarefa['descricao']}")

    elif resposta == "4":
        for i, tarefa in enumerate(lista_tarefas):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(f"{i + 1}. {status} {tarefa['descricao']}")
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            lista_tarefas[indice]["concluida"] = True
            salvar_tarefas(lista_tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")

    elif resposta == "5":
        print("Salvando e saindo do programa...")
        salvar_tarefas(lista_tarefas)
        break

    else:
        print("Opção inválida. Tente novamente.")
