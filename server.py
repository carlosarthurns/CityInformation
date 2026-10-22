from flask import Flask, render_template, request
from waitress import serve

from clima import obter_clima_atual

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/clima')
def obter_clima():
    cidade = request.args.get('cidade', '').strip() or "Campina Grande"

    dados_clima = obter_clima_atual(cidade)

    if dados_clima['cod'] == '404':
        erro = f"Não encontramos: '{cidade}'. Confira o nome da cidade e tente de novo."
        return render_template('index.html', erro=erro), 404

    condicao = dados_clima["weather"][0]

    return render_template(
        'clima.html',
        cidade=dados_clima["name"],
        descricao=condicao["description"].capitalize(),
        icone=condicao["icon"],
        tema=escolher_tema(condicao['id'], condicao['icon']),
        temperatura=f"{dados_clima['main']['temp']:.1f}",
        sensacao=f"{dados_clima['main']['feels_like']:.1f}",
        umidade=dados_clima["main"]["humidity"],
        vento=f"{dados_clima['wind']['speed'] * 3.6:.1f}",
    )

def escolher_tema(id, icon):
    if id in (800, 801, 802):
        if icon.endswith("n"):
            return "noite"
        return "limpo" if id == 800 else "parcial"
    if id in (803, 804) or 700 <= id < 800:
        return "nublado"
    if 200 <= id < 300:
        return "tempestade"
    if 300 <= id < 600:
        return "chuva"
    if 600 <= id < 700:
        return "neve"
    return "neutro"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)