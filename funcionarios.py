import random

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def get_salario(self):
        return self.salario

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, idade, horasTrabalhadas, valorHora):
        super().__init__(nome, idade, horasTrabalhadas * valorHora)
        self.horasTrabalhadas = horasTrabalhadas
        self.valorHora = valorHora

class FuncionarioPF(Funcionario):
    def __init__(self, nome, idade, salarioFixo):
        super().__init__(nome, idade, salarioFixo)
        self.salarioFixo = salarioFixo

# Função para gerar nomes aleatórios
def gerar_nome():
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Laura", "Lucas", "Sofia"]
    return random.choice(nomes)

# Criação dos funcionários
funcionario_pj = FuncionarioPJ(gerar_nome(), random.randint(20, 60), random.randint(80, 160), random.randint(20, 50))
funcionario_pf = FuncionarioPF(gerar_nome(), random.randint(20, 60), random.randint(1500, 5000))

# Impressão dos salários
print(f"O salário do funcionário PJ {funcionario_pj.nome} é: R$ {funcionario_pj.get_salario():.2f}")
print(f"O salário do funcionário PF {funcionario_pf.nome} é: R$ {funcionario_pf.get_salario():.2f}")
