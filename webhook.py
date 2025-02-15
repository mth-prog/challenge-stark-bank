from flask import Flask, request, jsonify
import starkbank
from dotenv import load_dotenv
import os
load_dotenv() 

# Configuração do usuário do StarkBank 
# https://starkbank.com/docs/api#authentication


starkbank.user = starkbank.Project(
    environment="sandbox",
    id=os.getenv("STARKBANK_ID"),
    private_key=os.getenv("STARKBANK_PRIVATE_KEY")
)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.content_type != "application/json":
        return jsonify({"error": "Unsupported Media Type"}), 415
    
    try:
        event = request.get_json()
        if not event:
            return jsonify({"error": "Invalid JSON"}), 400
        
        if event.get("subscription") == "invoice":
            invoice = event["log"]["invoice"]
            if invoice["status"] == "paid":
                processar_pagamento(invoice)
                
        return jsonify({"status": "received"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def processar_pagamento(invoice):
    amount_received = invoice["amount"] 
    fees = 500  # Simulação de taxa de R$ 5,00
    transferir_valor(amount_received - fees)

def transferir_valor(valor):
    transfer = starkbank.Transfer(
        amount=valor,
        bank_code="20018183",
        branch_code="0001",
        account_number="6341320293482496",
        account_type="payment",
        name="Stark Bank S.A.",
        tax_id="20.018.183/0001-80"
    )
    starkbank.transfer.create([transfer])
    print(f"Transferência de R${valor / 100:.2f} realizada com sucesso!")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

    