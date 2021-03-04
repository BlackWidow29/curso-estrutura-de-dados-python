a = 'casaco'

#Todas as letras da palavra se transforam em maiusculas
maiuscula = a.upper()
print(maiuscula)

#Todas as letras das palavra se transformam em minusculas
minuscula = maiuscula.lower()
print(minuscula)

#Apenas a primeira letra é transformada em maiuscula
capital = a.capitalize()
print(capital)

#Pega uma parte da palavra
metade_palavra = a[0:4]
print(metade_palavra)

ultimas_letras = a[3:]
print(ultimas_letras)

#Substitui uma parte da palavra ou letra por outra
b = a.replace('aco','inha')
print(b)

c = a.replace('o', 'a')
print(c)

#Retorna a primeira posição que ele encontrar da letra passada
print(c.find('a'))

#Retorna a quantidade de caractres na string, contado inclusive os espaços
e = ' palavra '
print(len(e))

#Remove os espaços no começo e no final da string
f = e.strip()
print(f)
print(len(f))

n1 = 20
n2 = 16

#O f formata uma string e aceita as variaveis dentro dela
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')