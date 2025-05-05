

def numeroPiramide(num):
    for i in range(1,num + 1, ):
        print(f"{i} " * i)

def printNome(nome):
    print(f"Nome: {nome}")

def piramide2(num2):
    for x in range(1,num2+1,):
        for y in range(1,x + 1):
            print(x, end = " ")
        print( )

def vogais(texto):
    novText = texto.lower()
    contVogais = 0
    for i in novText:
        if i in "aeiou":
            contVogais += 1

    print(f"Tem {contVogais} vogais")


def produto(nomeP, qntdP, valorP):
    calculo = qntdP * valorP
    return f"O valor total de {nomeP} no seu estoque é R${calculo}"

