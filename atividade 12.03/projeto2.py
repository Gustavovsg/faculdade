## importações para aplicação ##
import tkinter as tk
import json

## funções para o calculo ##
def calcular_soma(numero1, numero2):
    return numero1 + numero2

def calcular_subtracao(numero1, numero2):
    return numero1 - numero2

def calcular_multiplicacao(numero1, numero2):
    return numero1 * numero2

def calcular_divisao(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "Erro: escolha outro número diferente de 0."

## função chamada ao clicar em cada botão ##
def calcular(operacao):
    n1 = float(entry_num1.get())
    n2 = float(entry_num2.get())

    if operacao == 'Soma':
        resultado = calcular_soma(n1, n2)
    elif operacao == 'Subtração':
        resultado = calcular_subtracao(n1, n2)
    elif operacao == 'Multiplicação':
        resultado = calcular_multiplicacao(n1, n2)
    elif operacao == 'Divisão':
        resultado = calcular_divisao(n1, n2)

    label_resultado.config(text=f"Resultado: {resultado}")

    ## salva no arquivo json ##
    with open('resultado.json', 'a') as arquivo_json:
        arquivo_json.write(json.dumps({'resultado': resultado}) + '\n')

## cria a janela ##
root = tk.Tk()
root.title("Calculadora Minimalista")

## escolha dos números ##
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

## botão para cada operação ##
tk.Button(root, text="Soma", command=lambda: calcular('Soma')).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Subtração", command=lambda: calcular('Subtração')).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Multiplicação", command=lambda: calcular('Multiplicação')).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Divisão", command=lambda: calcular('Divisão')).grid(row=3, column=1, padx=5, pady=5)

## aba do resultado ##
label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()