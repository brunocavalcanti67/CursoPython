"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa;
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Bruno'
idade = 20
altura = 1.80
peso = 79.1
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso/(altura **2)

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}Kgs.\nO IMC de {nome} é {imc:.2f}.\n{nome} nasceu em {ano_nasc}.')