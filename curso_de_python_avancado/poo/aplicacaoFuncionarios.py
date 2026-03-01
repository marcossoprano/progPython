import json
import study1

banco_de_dados = []

def salvar_no_json():
    dados_a_serem_salvos = [f.para_dict() for f in banco_de_dados]
    with open ("funcionarios.json", "w") as arquivo:   
        json.dump(dados_a_serem_salvos, arquivo, indent=4) #dump converte dados de estruturas python em json

    
def carregar_do_json():
    try:
        with open("funcionarios.json", "r") as arquivo:
            dados = json.load(arquivo) #faz o inverso do dump, converte de json para estruturas python
            for item in dados:
                # Criamos novos objetos a partir dos dados do arquivo
                novo_f = study1.Funcionarios(item['nome'], item['idade'], item['cargo'], item['salario'])
                banco_de_dados.append(novo_f)
    except FileNotFoundError:
        pass # Se o arquivo não existir ainda, não faz nada    


def menu():
    carregar_do_json() # Tenta ler os dados salvos ao iniciar
    
    while True:
        print("\n=== SISTEMA DE RH 1.0 ===")
        print("1. Cadastrar Funcionário")
        print("2. Exibir Todos os Funcionários")
        print("3. Dar Aumento")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cargo = input("Cargo: ")
            salario = float(input("Salário Inicial: "))
            
            novo_funcionario = study1.Funcionarios(nome, idade, cargo, salario)
            banco_de_dados.append(novo_funcionario)
            salvar_no_json()

        elif opcao == "2":
            if not banco_de_dados:
                print("Nenhum funcionário cadastrado.")
            for f in banco_de_dados:
                f.exibir_dados()

        elif opcao == "3":
            nome_busca = input("Digite o nome do funcionário: ")
            encontrado = False
            for f in banco_de_dados:
                if f.nome.lower() == nome_busca.lower():
                    perc = float(input(f"Qual a porcentagem de aumento para {f.nome}? "))
                    f.salario += f.salario * (perc / 100)
                    salvar_no_json()
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Inicia o programa
if __name__ == "__main__":
    menu()    