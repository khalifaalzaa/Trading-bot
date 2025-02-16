import ccxt

# إعداد الاتصال بمنصة Binance
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
    'options': {'defaultType': 'future'},
})

# إعداد استراتيجية تداول بسيطة
def trade():
    market = 'BTC/USDT'
    ticker = exchange.fetch_ticker(market)
    price = ticker['last']

    if price > 50000:
        order = exchange.create_market_sell_order(market, 0.01)
        print(f'Sold at {price}')
    elif price < 45000:
        order = exchange.create_market_buy_order(market, 0.01)
        print(f'Bought at {price}')

# تنفيذ التداول
trade()
