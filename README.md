# challenge-stark-bank

1. Issues 8 to 12 Invoices every 3 hours to random people for 24 hours (our Sandbox
emulation environment will make sure some of those are automatically paid)
----
3. Receives the webhook callback of the Invoice credit and sends the received amount
(minus eventual fees) to the following account using a Transfer

## Setup
1. Coloque as variaveis de ambientes necessarias, confira atraves desse link: [autenticação](https://starkbank.com/docs/api#authentication)
2. Instale dependências: `pip install -r requirements.txt`
3. Execute o servidor: `flask --app webhook run`
4. (Necessario o ngrok instalado) Em outro terminal, execute o comando `ngrok http 5000` para inserir o endpoint em integrações -> webhook, confira nesse link: [webhook](https://challenge-mateus-pereira.sandbox.starkbank.com/integrations/webhooks) 
5. Para gerar os invoices entre na pasta `starkbank` e execute o comando `python invoices.py`
