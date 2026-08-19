# 1. Definição das variáveis (Valores de exemplo para teste)
bateria_actual = 10  # Número inteiro de 0 a 100
bola_em_jogo = True  # Valor booleano: True ou False

# 2. Processamento das condições de forma ordenada (If / Elif / Else)
if bateria_actual < 15 and bola_em_jogo == True:
    print(
        "ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação."
    )

elif bateria_actual < 15 and bola_em_jogo == False:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
