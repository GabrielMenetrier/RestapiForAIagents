from flask import Flask, request, jsonify

app = Flask(__name__)

# Função que queremos chamar via API
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    return peso / (altura ** 2)

# Função auxiliar (opcional)
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"


# Endpoint que chama a função
@app.route('/calcular-imc', methods=['POST'])
def endpoint_imc():
    try:
        # Recebe os parâmetros do corpo da requisição (JSON)
        dados = request.json
        peso = float(dados['peso'])
        altura = float(dados['altura'])
        
        # Chama a função
        resultado = calcular_imc(peso, altura)
        
        # Retorna a resposta como JSON
        return jsonify({
            "status": "sucesso",
            "imc": round(resultado, 2),
            "classificacao": classificar_imc(resultado)
        })
    
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)