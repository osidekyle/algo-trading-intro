import pandas_datareader
import matplotlib.pyplot as plt
import pandas as pd


tickers = ["AAPL", "MSFT", "^GSPC"]

start_date = '2010-01-01'
end_date = '2016-12-31'

panel_data = pandas_datareader.yahoo.daily.YahooDailyReader(symbols=tickers,start=start_date, end=end_date).read()

close = panel_data['Close']

all_weekdays = pd.date_range(start=start_date, end=end_date, freq="B")

close = close.reindex(all_weekdays)

close = close.fillna(method = 'ffill')

msft = close.loc[:, "MSFT"]

short_rolling_msft = msft.ewm(span=13, adjust=False).mean()
long_rolling_msft = msft.ewm(span=48, adjust=False).mean()

short_upper_envelope = short_rolling_msft.map(lambda val: val * 1.1)
short_lower_envelope = short_rolling_msft.map(lambda val: val * 0.9)

fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(msft.index, msft, label="MSFT")
ax.plot(short_rolling_msft.index, short_rolling_msft, label="13 days rolling")
ax.plot(short_upper_envelope.index, short_upper_envelope, label="13 days rolling upper envelope", color="yellow")
ax.plot(short_lower_envelope.index, short_lower_envelope, label="13 days rolling lower envelope", color="yellow")
ax.plot(long_rolling_msft.index, long_rolling_msft, label="48 days rolling")

ax.set_xlabel("Date")
ax.set_ylabel("Adjusted closing price ($)")
ax.legend()

plt.show()

