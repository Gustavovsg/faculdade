## importando a biblioteca que será utilizada ##
import json

## funções para cada operação ##
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

## entrada dos números e escolha da operação ##    
numero1 = float(input('escolha um número: '))
numero2 = float(input('escolha outro número: '))
operacao = input('escolha o número referente a operação a ser realizada:\n[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n')

## resultado em json ##
resultado = ""

if operacao == '1':
    resultado = calcular_soma(numero1, numero2)
elif operacao == '2':
    resultado = calcular_subtracao(numero1, numero2)
elif operacao == '3':
    resultado = calcular_multiplicacao(numero1, numero2)
elif operacao == '4':
    resultado = calcular_divisao(numero1, numero2)
else:
    resultado = "Operação inválida. Por favor, escolha um número entre 1 e 4."

## salva o resultado na variavel e mostra na tela ##
resultado_em_json = json.dumps({'resultado': resultado})
print(resultado_em_json)

## adiciona o resultado a um arquivo json ##
with open('resultado.json', 'a') as arquivo_json:
    json.dump({'resultado': resultado}, arquivo_json)
    arquivo_json.write('\n')