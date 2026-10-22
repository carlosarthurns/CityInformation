from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def obter_clima_atual(cidade="Campina Grande"):
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "appid": os.getenv("OPENWEATHER_API_KEY"),
                "q": cidade,
                "units": "metric",
                "lang": "pt_br",
            },
            timeout=5,
        )
    except requests.RequestException:
        return None

    return response.json()


if __name__ == "__main__":
    print("\n*** Consulta de Clima ***\n")

    cidade = input("\nDigite o nome de uma cidade: ").strip() or "Campina Grande"

    dados_clima = obter_clima_atual(cidade)

    print("\n")
    if dados_clima['cod'] == '404':
        print(f"Não foi possível obter o clima de {cidade}. Verifique o nome da cidade.")
    else:
        pprint(dados_clima)
