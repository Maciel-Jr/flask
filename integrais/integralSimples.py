import random
from sympy import symbols, integrate
from integrais.auxiliar.positivoNegativo import positivoNegativo


#https://www.sympy.org/pt/features.html  


def integraisSimples(quantidade,ativoResposta=False, ativoLimites=False):
    
    listaFuncao = []
    listaIntegral = []
    listaLimiteA = []
    listaLimiteB = []
    operacao = positivoNegativo()
    # Gere cálculos de integrais aleatórias
    for _ in range(quantidade):
        # Gere uma função aleatória
        
        Limite_a = random.randint(-5, 6)
        Limite_b= random.randint(-5, 6)


        if Limite_b > Limite_a: Limite_a, Limite_b = Limite_b, Limite_a


        x = symbols('x')
        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        expoente = random.randint(0, 6)


        if operacao == 'positivo':
            function = a_coef * x**expoente + b_coef * x + c_coef
        else:
            function = a_coef * x**expoente - b_coef * x + c_coef
        

        integrate(function, (x))
        integral = integrate(function, (x))

        if ativoLimites: integral = integrate(function, (x, Limite_a, Limite_b))

        if ativoLimites and integral < 0: integral*(-1)
    
        listaFuncao.append(str(function))
        listaIntegral.append(str(integral))
        listaLimiteA.append(str(Limite_a))
        listaLimiteB.append(str(Limite_b))

        

   
    
    
    if ativoResposta == True:
        if ativoLimites == True:
            return listaFuncao, listaIntegral, listaLimiteA, listaLimiteB
        else:
            return listaFuncao, listaIntegral
    else:
        if ativoLimites == True:
            return listaFuncao,listaLimiteA, listaLimiteB
        else:
            return listaFuncao


    



       
       
        


