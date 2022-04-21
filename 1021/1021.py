def numero_notas(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas =[1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for valorNota in notas:
        numeroNotas = (valor//valorNota)
        print(f"{numeroNotas} nota(s) de R$ {valorNota:.2f}")
        valor -= numeroNotas * valorNota
    
    print("MOEDAS:")
    for valorMoeda in moedas:
        numeroMoedas = (valor//valorMoeda)
        print(f"{numeroMoedas} moeda(s) de R$ {valorMoeda:.2f}")
        valor -= numeroMoedas * valorMoeda
        valor = float('%.2f'% valor)


valor = float(input("valor é: "))
numero_notas(valor)