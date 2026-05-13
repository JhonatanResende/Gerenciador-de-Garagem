import json
from tabulate import tabulate

def ler_carros_arquivo():
    try:
        with open("carros.json", "r") as arquivo_json:
            lista_convertida = json.load(arquivo_json)
            return lista_convertida
    except FileNotFoundError:
        print("Primeira execução. Arquivo vazio.")

        lista_convertida = []
        return lista_convertida
    except json.decoder.JSONDecodeError:
        print("Conteúdo do arquivo não pode ser convertido.")

        lista_convertida = []
        return lista_convertida
        
def salvar_carros():
    with open("carros.json", "w") as arquivo_json:
        json.dump(carros, arquivo_json, indent=2)

carros = ler_carros_arquivo()

def encontrar_carro_por_placa(placa):
    carro_encontrado = None

    for carro in carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro 
            break

    return carro_encontrado

def cadastrar_carro():
    print("\n=============== CADASTRO DE VEÍCULO ===============")
    placa = input("Digite a placa do veículo: ").strip()

    if len(placa) == 0:
        print("A placa não pode ser vazia. Por favor, tente novamente.")
        return

    carro_existente = encontrar_carro_por_placa(placa)
    if carro_existente != None:
        print("Já existe um veículo cadastrado com essa placa. Por favor, escolha uma placa diferente.")
        return

    modelo = input("Digite o modelo do veículo: ").strip()

    if len(modelo) == 0:
        print("O modelo não pode ser vazio. Por favor, tente novamente.")
        return

    try:
        ano = int(input("Digite o ano do veículo: "))
    except ValueError:
        print("Ano inválido. Por favor, digite um ano válido.")
        return

    cor = input("Digite a cor do veículo: ").strip()

    if len(cor) == 0:
        print("A cor não pode ser vazia. Por favor, tente novamente.")
        return

    carro = {
        "placa": placa,
        "modelo": modelo,
        "ano": ano,
        "cor": cor
    }

    carros.append(carro)
    salvar_carros()
    print("Veículo cadastrado com sucesso!")

def exibir_carros_lista():
    if len(carros) == 0:
        print("\nNenhum veículo cadastrado no momento.")
        return

    print("\n=============== LISTA DE VEÍCULOS ===============")
    for carro in carros:
        print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Ano: {carro['ano']} | Cor: {carro['cor']}")

    print("=================================================")

def exibir_carros_tabela():
    if len(carros) == 0:
        print("\nNenhum veículo cadastrado no momento.")
        return
    
    print("\n=============== TABELA DE VEÍCULOS ===============")

    tabela = tabulate(carros, headers="keys", tablefmt="fancy_grid")
    print(tabela)

def editar_carro():
    placa = input("Digite a placa do veículo que deseja editar: ").strip()
    
    carro_existente = encontrar_carro_por_placa(placa)

    if carro_existente == None:
        print("\nVeículo não encontrado. Verifique a placa e tente novamente.")
        return
    
    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "modelo": carro_existente["modelo"],
        "ano": carro_existente["ano"],
        "cor": carro_existente["cor"]
    }

    print("\nDigite os novos detalhes do veículo (aperte Enter ou deixe em branco para manter o valor atual):")

    nova_placa = input(f"Nova placa (placa atual: {carro_existente['placa']}): ").strip()

    if len(nova_placa) > 0 and (nova_placa.lower() != carro_existente["placa"].lower()):
        if encontrar_carro_por_placa(nova_placa) != None:
            print("Já existe um veículo cadastrado com essa placa. Por favor, escolha uma placa diferente.")
            return
        
        dicionario_atualizacao["placa"] = nova_placa

    novo_modelo = input(f"Novo modelo (modelo atual: {carro_existente['modelo']}): ").strip()
    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano = input(f"Novo ano (ano atual: {carro_existente['ano']}): ")
    if len(novo_ano) > 0:
        try:
            dicionario_atualizacao["ano"] = int(novo_ano)
        except ValueError:
            print("Ano inválido. Por favor, digite um ano válido.")
            return

    nova_cor = input(f"Nova cor (cor atual: {carro_existente['cor']}): ").strip()
    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]

    salvar_carros()

    print("Veículo atualizado com sucesso!")

def deletar_carro():
    placa = input("Digite a placa do veículo que deseja deletar: ").strip()
    carro_encontrado = encontrar_carro_por_placa(placa)

    if carro_encontrado == None:
        print("\nVeículo não encontrado. Verifique a placa e tente novamente.")
        return
    
    carros.remove(carro_encontrado)
    salvar_carros()
    print("Veículo deletado com sucesso!")

def exibir_menu():
    print("\n ====== GERENCIADOR DE GARAGEM ======")
    print("1. Cadastrar veículo")
    print("2. Exibir veículos cadastrados (em formato de lista)")
    print("3. Exibir veículos cadastrados (em formato de tabela)")
    print("4 - Editar detalhes de um veículo")
    print("5. Deletar um veículo")
    print("6. Sair")

while True:
    exibir_menu()
    opcao_escolhida = input("Escolha uma opção: ").strip()

    if opcao_escolhida == "1":
        print("\nOpção 1 selecionada: Cadastrar veículo")
        cadastrar_carro()
    elif opcao_escolhida == "2":
        print("\nOpção 2 selecionada: Exibir veículos cadastrados (em formato de lista)")
        exibir_carros_lista()
    elif opcao_escolhida == "3":
        print("\nOpção 3 selecionada: Exibir veículos cadastrados (em formato de tabela)")
        exibir_carros_tabela()
    elif opcao_escolhida == "4":
        print("\nOpção 4 selecionada: Editar detalhes de um veículo")
        editar_carro()
    elif opcao_escolhida == "5":
        print("\nOpção 5 selecionada: Deletar um veículo")
        deletar_carro()
    elif opcao_escolhida == "6":
        print("\nSaindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")




