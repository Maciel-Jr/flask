from flask import Flask, jsonify, request
from integrais.integralSimples import integraisSimples
from flask_cors import CORS


    
app = Flask(__name__)
CORS(app, origins='*')

@app.route('/Calc', methods=['GET'])
def CalcFy():
    return '<a href="http://127.0.0.1:5000/api/integral/Quantidade=1&ativoResposta=False&AtivoLimite=False"><button>Meu Botão</button></a>'

@app.route('/api/integral/Quantidade=<quantidade>&ativoResposta=<ativoResposta>&AtivoLimite=<AtivoLimite>', methods=['GET'])
def integral(quantidade, ativoResposta=False, AtivoLimite=False):

    quantidade = int(quantidade)
    ativoResposta = ativoResposta.lower() == 'true'
    AtivoLimite = AtivoLimite.lower() == 'true'

   
    resultado = integraisSimples(quantidade, ativoResposta, AtivoLimite)

    if ativoResposta == True:
        if AtivoLimite == True:
            mensagem = {
                'Funcoes': resultado[0],
                'Resultado': resultado[1],
                'Limites Superiores': resultado[2],
                'Limites Inferiores': resultado[3]
            }
        else:
            mensagem = {
                'Funcoes': resultado[0],
                'Resultado': resultado[1]
            }
    else:
        if AtivoLimite == True:
         mensagem = {
                'Funcoes': resultado[0],
                'Limites Superiores': resultado[1],
                'Limites Inferiores': resultado[2]
            }
        else:
            mensagem = {
                'Funcoes': resultado
            }
   

    return jsonify(mensagem)


if __name__ == '__main__':
    app.run(debug=True)
