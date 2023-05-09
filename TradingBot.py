from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta

handler = TA_Handler(
    symbol="USDEUR",
    exchange="FX_IDC",
    screener="forex",
    interval="15m",
    timeout=None
)

analysis = handler.get_analysis()

opening_price = analysis.indicators["open"]
closing_price = analysis.indicators["close"]
rsi = analysis.indicators["RSI"]
macd = analysis.indicators["MACD.macd"]

print(opening_price)
print(closing_price)
print(rsi)
print(macd)