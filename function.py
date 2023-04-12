import json
import alpaca_trade_api as tradeapi

def broker_handle(ticker:str, action:str):
    # Set your API key and secret
    API_KEY = "API-key"
    API_SECRET = "API-secret"
    BASE_URL = "your API's base URL"

    # Create an Alpaca API connection
    api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

    # Get account information
    account = api.get_account()
   

    if action.lower() == 'buy':
        buying_power = float(account.buying_power)
        trade_amount = buying_power * 0.8
        stock = api.get_latest_trade(ticker)
        price = float(stock.price)
        shares = int(trade_amount / price)
        order = api.submit_order(
            symbol = ticker,
            qty = shares,
            side= 'buy',
            type= 'market',
            time_in_force='gtc'
        )
        print(f"Placed a market order to buy {shares} shares of {ticker} at ${price} per share.")
        print(f"You have ${account.buying_power} left for buying power")
    elif action.lower() == 'sell':
        positions = api.list_positions()
        position_to_sell = None
        for position in positions:
            if position.symbol == ticker:
                position_to_sell = position
                break
        if position_to_sell:
            shares = int(position_to_sell.qty)
            # Place a market order to sell all the shares
            order = api.submit_order(
                symbol=ticker,
                qty=shares,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            print(f"Placed a market order to sell {shares} shares of {ticker}.")
        else:
            print(f"You don't have any shares of {ticker}.")


def webhook_handler(request):
    request_json = request.get_json()
    ticker = request_json['ticker']
    action = request_json['action']
    broker_handle(ticker, action)
    return 'Done'