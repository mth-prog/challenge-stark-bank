import starkbank
import random
import os
from datetime import datetime, timedelta
from starkbank import Split
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import time


load_dotenv() 

# Configuração do usuário do StarkBank 
# https://starkbank.com/docs/api#authentication


starkbank.user = starkbank.Project(
    environment="sandbox",
    id=os.getenv("STARKBANK_ID"),
    private_key=os.getenv("STARKBANK_PRIVATE_KEY")
)

clientes = [
    {"name": "João Silva", "tax_id": "012.345.678-90"},
    {"name": "Maria Souza", "tax_id": "012.345.678-90"},
    {"name": "Pedro Oliveira", "tax_id": "012.345.678-90"},
]

def emitir_invoices():
    invoices = []

    for _ in range(random.randint(8, 12)):
        cliente = random.choice(clientes)
        invoice = starkbank.Invoice(
            amount=200,
            tax_id=cliente["tax_id"],
            name=cliente["name"],
        )
        invoices.append(invoice)
    
    created_invoices = starkbank.invoice.create(invoices)
    print(f"Invoices criadas: {[inv.id for inv in created_invoices]}")

# Agendar para rodar por 24 horas a cada 3 horas
for _ in range(8):  # 8 ciclos de 3 horas
    emitir_invoices()
    time.sleep(3 * 60 * 60)  # Esperar 3 horas