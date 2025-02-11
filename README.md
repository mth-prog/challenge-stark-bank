# challenge-stark-bank

1. Issues 8 to 12 Invoices every 3 hours to random people for 24 hours (our Sandbox
emulation environment will make sure some of those are automatically paid)

3. Receives the webhook callback of the Invoice credit and sends the received amount
(minus eventual fees) to the following account using a Transfer
