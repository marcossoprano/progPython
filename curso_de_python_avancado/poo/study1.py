#criar classe pra armazenar dados de funcionario

class Funcionarios:

    def __init__(self, nome, idade, cargo, salario= 0.0):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = float(salario)

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Cargo: {self.cargo} | Salário: R$ {self.salario:.2f}")
    

    
    def para_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cargo": self.cargo,
            "salario": self.salario
        }
    
    def dar_aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)
        return self.salario
