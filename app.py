from flask import Flask, request, jsonify
import GoogleNews as GoogleNews

app = Flask(__name__)

@app.route('/teste', methods=['GET'])
def teste():
    return jsonify({"status": "ok", "mensagem": "API funcionando!"})

def buscar_noticias(tema, lang='pt', region='BR', period='1d', max_results=10):
    """
    Busca notícias sobre um tema usando GoogleNews.
    """
    noticias = GoogleNews.GoogleNews(lang=lang, region=region, period=period)
    noticias.get_news(tema)
    resultados = noticias.results()[:max_results]
    return resultados


# Endpoint que chama a função
@app.route('/notícias', methods=['POST'])

def get_news():
    try:
        dados = request.json
        tema = dados.get('tema')
        lang = dados.get('lang', 'pt')
        region = dados.get('region', 'BR')
        period = dados.get('period', '1d')
        max_results = int(dados.get('max_results', 50))

        if not tema:
            return jsonify({"status": "erro", "mensagem": "Parâmetro 'tema' é obrigatório."}), 400

        noticias = buscar_noticias(tema, lang, region, period, max_results)
        return jsonify({"status": "sucesso", "noticias": noticias})

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 400



if __name__ == '__main__':
    