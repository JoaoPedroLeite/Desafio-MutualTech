def calcular_tempo_jogo(horaI, minutoI, horaF, minutoF):
    minutoTI = minutoI + horaI * 60
    minutoTF = minutoF + horaF * 60
    tempoJogo = minutoTF - minutoTI

    if tempoJogo <= 0:
        tempoJogo += 1440
    
    return tempoJogo

def converter_tempo(tempoJogo):
    horaJogo = tempoJogo//60
    minutoJogo = tempoJogo%60

    return horaJogo, minutoJogo


horaI, minutoI, horaF, minutoF = (map(int, input("informe a hora inicial, minuto inicial, hora final e minuto final : ").split(" ")))
tempoJogo = calcular_tempo_jogo(horaI, minutoI, horaF, minutoF)
horaJogo, minutoJogo = converter_tempo(tempoJogo)

print(f"O JOGO DUROU {horaJogo} HORA(S) E {minutoJogo} MINUTO(S)")
