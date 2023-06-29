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
        d_coef = random.randint(-10, 10)
        #
        e_coef = random.randint(-10, 10)
        f_coef = random.randint(-10, 10)
        expoenteu = random.randint(0, 6)
        expoentev = random.randint(0, 6)

        
        if operacao == 'positivo':
            funcaoU = a_coef * x**expoenteu + b_coef * x + c_coef
            funcaoV = d_coef * x**expoentev + e_coef * x + f_coef
        else:
            funcaoU = a_coef * x**expoenteu - b_coef * x + c_coef
            funcaoV = d_coef * x**expoentev + e_coef * x + f_coef


        derivadaU = diff(funcaoU, (x))
        derivadaV = diff(funcaoV, (x)) 


        derivada = derivadaU * funcaoV + funcaoU *  derivadaV 
        funcao = funcaoU*funcaoV

                
        listaFuncao.append(funcao)
        listaDerivada.append(derivada)

    if ativoResposta:  
        return listaFuncao, listaDerivada 
    else: 
        return listaFuncao
    
       
                
                
                
                
     
       
        



