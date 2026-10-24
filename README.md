# CityInformation

Aplicação web em **Flask** que consulta a API da [OpenWeatherMap](https://openweathermap.org/api) e mostra o clima atual de qualquer cidade.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8490808b-b620-4c03-a73a-4473bc236391" />

## Funcionalidades

- Busca do clima por nome de cidade
- Temperatura, sensação térmica, umidade e velocidade do vento (km/h)
- Cidade padrão (Campina Grande) quando a busca vem vazia
- Condição do tempo reconhecidas: céu limpo, nublado, chuva, tempestade, neve ou noite.

## Tecnologias

- **Back-end:** Python 3, Flask e Waitress (servidor WSGI)
- **Consumo de API:** Requests, com a API da OpenWeatherMap
- **Configuração:** python-dotenv, para guardar a chave da API em variáveis de ambiente
- **Front-end:** HTML e CSS, sem frameworks

## Estrutura do projeto

```
CityInformation/
├── clima.py            # integração com a API da OpenWeatherMap
├── server.py           # rotas
├── requirements.txt    
├── static/
│   └── styles/
│       └── style.css   # estilos e temas de fundo
└── templates/
    ├── index.html      # página inicial com o formulário de busca
    └── clima.html      # página com o resultado do clima
```

O arquivo `.env`, que guarda a chave da API, **não é versionado**.

## Como executar

### Pré-requisitos

- Python 3.10 ou superior
- Uma chave gratuita da OpenWeatherMap (veja abaixo)

### Instalação

```bash
git clone https://github.com/carlosarthurns/CityInformation.git
cd CityInformation

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### Configuração da chave da API

1. Crie uma conta em [openweathermap.org](https://openweathermap.org/api) e gere uma chave de API.
2. Na raiz do projeto, crie um arquivo `.env` com o conteúdo:

```
OPENWEATHER_API_KEY=sua_chave_aqui
```

### Execução

```bash
python3 server.py
```

Abra [localhost:8000](http://localhost:8000) no navegador.

O servidor executa em todas as interfaces (`0.0.0.0`) na porta `8000`, então também fica acessível a outros dispositivos da sua rede local!! 
Para parar, use `Ctrl+C`. 

## Rotas

| Rota | Descrição |
|---|---|
| `/` e `/index` | Página inicial com o formulário de busca |
| `/clima` | Resultado do clima da cidade informada |

## Como funciona

1. O formulário envia a cidade por GET para `/clima`.
2. `server.py` lê o parâmetro `cidade` (usando Campina Grande se vier vazio) e chama `obter_clima_atual`, em `clima.py`.
3. `clima.py` consulta a API
4. `server.py` escolhe o tema visual pelo código da condição climática e pelo ícone (dia ou noite), e renderiza `clima.html`.

## Próximos passos

- Testes automatizados com `pytest`, simulando a API
- Previsão para as próximas horas e dias
- Qualidade do ar e horários de nascer e pôr do sol
- Informações da cidade, como população (possivelmente restritas a cidades brasileiras, usando a API do IBGE)
- Busca por mapa: clicar em um ponto e consultar o clima pelas coordenadas

## Observação

Projeto desenvolvido para estudo de aplicações web. Os dados de clima pertencem à [OpenWeatherMap](https://openweathermap.org/).

### Limitações até o momento

- **Tratamento de erros:** apenas o erro 404 (NotFound) tem tratamento específico.
- **Servidor:** `host="0.0.0.0"` (no `server.py`) deixa a aplicação acessível na rede local. Para uso apenas local, altere para `host="127.0.0.1"`.
- **Tempo de resposta:** a API responde em cerca de 0,5 s por IPv4. Nos meus testes, a conexão por IPv6 com a API não respondeu e cada consulta ganhava alguns segundos de espera. Ainda não identifiquei se a falha está na minha rede ou no lado da OpenWeather.
