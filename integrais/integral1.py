import random
from sympy import symbols, integrate, limit
from integrais.auxiliar.positivoNegativo import positivoNegativo


#https://www.sympy.org/pt/features.html


def integrais1(quantidade,ativoResposta=False, ativoLimites=False):
    
    operacao = positivoNegativo()

    

    listaFuncao = []
    listaIntegral = []
    listaLimiteA = []
    listaLimiteB = []


    for _ in range(quantidade):
        
        x = symbols('x')

        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        d_coef = random.randint(-10, 10)
        e_coef = random.randint(-10, 10)
        f_coef = random.randint(-10, 10)

        expoente = random.randint(0, 6)

        Limite_a = random.randint(0, 6)
        Limite_b= random.randint(-5, 5)

        if operacao == 'positivo':
            functionU = a_coef * x**expoente + b_coef * x + c_coef
            functionV = d_coef * x**expoente + e_coef * x + f_coef
        else:
            functionU = a_coef * x**expoente + b_coef * x + c_coef
            functionV = d_coef * x**expoente + e_coef * x + f_coef

        integralU = integrate(functionU)
        integralV = integrate(functionV)


       

        function = functionU*functionV
        integralResult = integralU * functionV + functionU * integralV

        integralLimiteA = limit(integralResult, x, Limite_a)
        integralLimiteB = limit(integralResult, x, Limite_b)

        if ativoLimites: integralResult = integralLimiteA - integralLimiteB

        listaFuncao.append(function)
        listaIntegral.append(integralResult)
        listaLimiteA.append(Limite_a)
        listaLimiteB.append(Limite_b)

    if ativoResposta:
        if ativoLimites:
            return listaFuncao, listaIntegral, listaLimiteA, listaLimiteB
        else:
            return listaFuncao, listaIntegral
    else:
        if ativoLimites:
            return listaFuncao, listaLimiteA, listaLimiteB
        else:
            return listaFuncao
  

       
       
        



