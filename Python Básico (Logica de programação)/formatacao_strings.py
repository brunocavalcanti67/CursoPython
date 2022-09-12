nome = 'Bruno'
idade = 20
altura = 1.80
e_maior = idade > 18
peso = 79
imc = peso/(altura **2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

#usando f

print(f"{nome} tem {idade} anos de idade e seu imc é {imc:.2f}")

#usando .format()

print("{} tem {} anos de idade e seu imc é {}".format(nome, idade, imc))

#ele vai na ordem 0 1 2 mas podemos mudar:

print("{1} tem {0} anos de idade e seu imc é {2}".format(nome, idade, imc))

#da pra colocar nome tbm
print("{n} tem {i} anos de idade e seu imc é {ss}".format(n=nome,i=idade,ss=imc))
