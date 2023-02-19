import datetime
import matplotlib.pyplot as plt
import yfinance as yfin
yfin.pdr_override()

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime.now()

#read data with yahoo finance
sp500 = yfin.Ticker("SPY").history(period='5y')

plt.plot(sp500.index, sp500['Close'])
plt.title('S&P 500 Index from 2012 till Now')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()
