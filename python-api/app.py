from fastapi import FastAPI

app = FastAPI()


def minha_funcao(param1, param2):
    resultado = param1 + param2  # Exemplo de operação
    return resultado

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.route('/nome-do-endpoint', methods=['POST'])
def endpoint():
    # 1. Pega os parâmetros
    dados = request.json
    
    # 2. Chama a função
    resultado = minha_funcao(dados['param1'], dados['param2'])
    
    # 3. Retorna a resposta
    return jsonify({"resultado": resultado})