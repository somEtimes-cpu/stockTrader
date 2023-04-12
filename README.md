# stockTrader
Connects Tradingiew pine script to google function to perform stock trades

Tradingview gives comprehensive stock information while has their own programming language called pine, which allows traders to implement strategies to backtest.

Pine script also also allows to give indicators for buying and selling on real-time market according to the stragy coded.
However, the platform itself does not have the ability to trade on real market.
To go around this restriction, we can use a third-part webhook to listen on the indication from TradingView and use a broker API to perform stock trading.

I'm currently using google function as my webhooker. Am considering in using Flask in the future.

Procedure:
    1. implement the pine script indicator to the desired stock.
    2. Set an alert connection from the indicator to the webhook.
    3. Set up an google function. (currently, I'm using Alpaca as my broker since they grants API access)
    4. implement required module (as indicated in requirements.txt)
    5. Implement the function script.
    6. Deploy the function
    
The Pine script will be constantly updated, I will keep on learning to improve the strategy to make better trade decisions.