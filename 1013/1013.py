def maiorAB(a,b):
    a = int(a)
    b = int(b)
    maior = (a+b+abs(a-b))/2
    return maior

a, b, c = input('informe 3 numeros: ').split(" ")
primeiroMaior = maiorAB(a,b)
segundoMaior = maiorAB(primeiroMaior,c)
print (f"{segundoMaior:.0f} eh o maior")
