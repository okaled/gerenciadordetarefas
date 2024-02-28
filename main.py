import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

def adicionar_tarefa():
    nova_tarefa = input("Digite a nova tarefa: ")
    with open('tarefas.txt', 'a') as arquivo:
        arquivo.write(nova_tarefa + '\n') 
    print("Tarefa adicionada com sucesso.")
    time.sleep(1.3)

def listar_tarefas():
    print("Lista de Tarefas:")
    try:
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
                    
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")
    input('Pressione ENTER para continuar')

def llistar_tarefas():
    print("Lista de Tarefas:")
    try:
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
                    
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def remover_tarefa():
    try: 
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            
        if not tarefas:
            print("Não há tarefas para remover.")
            time.sleep(1.3)
            return
            
        llistar_tarefas()

        numero_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        
        if 1 <= numero_tarefa <= len(tarefas):
            with open('tarefas.txt', 'w') as arquivo:
                for i, tarefa in enumerate(tarefas, start=1):
                    if i != numero_tarefa:
                        arquivo.write(tarefa)
            print("Tarefa removida com sucesso.")
            time.sleep(1.3)
        else:
            print("Número de tarefa inválido.")
            time.sleep(1.3)
            
    except (ValueError, IndexError):
        print("Número de tarefa inválido.")
        time.sleep(1.3)


def main():
    while True:
        limpar_tela()
        print('------------------------')
        print(' GERENCIADOR DE TAREFAS ')
        print('        BY KALED        ')
        print('------------------------')

        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        print()
        

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '4':
            print("Saindo...")
            time.sleep(1.1)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
