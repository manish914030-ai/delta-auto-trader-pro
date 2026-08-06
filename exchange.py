import ccxt
from config import API_KEY, API_SECRET, TESTNET

def get_exchange():
    exchange = ccxt.delta({
        "apiKey": API_KEY,
        "secret": API_SECRET,
        "enableRateLimit": True,
    })

    if TESTNET:
        exchange.set_sandbox_mode(True)

    return exchange
