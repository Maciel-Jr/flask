import random
from sympy import symbols, diff
from Derivadas.auxiliar.positivoNegativo import positivoNegativo

#https://www.sympy.org/pt/features.html
# Defina os limites do intervalo de integração
def positivoNegativo():
    operacao = random.choice(['positivo', 'negativo'])
    return operacao

def derivadasSimples(quantidade,ativoResposta=False):
    
    operacao = positivoNegativo()

    listaFuncao = []
    listaDerivada = []


    # Gere cálculos de integrais aleatórias
    for _ in range(quantidade):
        # Gere uma função aleatória
        x = symbols('x')
        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        expoente = random.randint(0, 6)
        
        if operacao == 'positivo':
            function = a_coef * x**expoente + b_coef * x + c_coef
        else:
            function = a_coef * x**expoente - b_coef * x + c_coef


        derivada = diff(function, (x))
        listaFuncao.append(function)
        listaDerivada.append(derivada)

        
    if ativoResposta:
        return listaFuncao, listaDerivada
    else:
        return listaFuncao
       
       
        


