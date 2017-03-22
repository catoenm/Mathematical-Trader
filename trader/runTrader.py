from yahoo_finance import Share
import matplotlib.pyplot as plt
from collections import deque

nasdaq = Share('^IXIC')
yahoo = Share('YHOO')
nasdaq.refresh()
yahoo.refresh()
index_data = nasdaq.get_historical('2016-01-17', '2017-04-17')
data = yahoo.get_historical('2016-01-17', '2017-04-17')

# 0 Volume
# 1	Symbol
# 2 Adj Close
# 3 High
# 4 Low
# 5 Date
# 6 Close
# 7 Open

print len(index_data)
print len(data)
#print "Index Open", index_data[0].values()[7]

num_days = 25
days_ahead = 20

d_volatile_stock = 0
d_volatile_index = 0
d_momentum_stock = 0
d_momentum_index = 0

volatile_stock_total = []
volatile_index_total = []
momentum_stock_total = []
momentum_index_total = []
stock_means = []
stock_vol = []
stock_mom = []
index_means = []
index_vol = []
index_mom = []

#Stock Loop Priming
open_price = float(data[0].values()[6])
close_price = float(data[0].values()[7])
mean_stock = (open_price + close_price)/2
stock_means.insert(0, mean_stock)

for day in data[1:num_days]:
	#Stock Processing
	open_price = float(day.values()[6])
	close_price = float(day.values()[7])
	mean_stock = (open_price + close_price)/2

	stock_means.insert(0, mean_stock)
	volatile_stock_total.insert(0, 0)
	momentum_stock_total.insert(0, 0)

	stock_vol.insert(0, stock_means[1] - stock_means[0])
	stock_mom.insert(0, close_price - open_price)

	d_volatile_stock += stock_vol[0]
	d_momentum_stock += stock_mom[0]

#Main Data Processing Loop
for day in data[num_days:]:
	open_price = float(day.values()[6])
	close_price = float(day.values()[7])
	mean_stock = (open_price + close_price)/2

	stock_means.insert(0, mean_stock)
	stock_vol.insert(0, stock_means[1] - stock_means[0])
	stock_mom.insert(0, close_price - open_price)

	volatile_stock_total.insert(0, d_volatile_stock)
	momentum_stock_total.insert(0, d_momentum_stock)

	d_volatile_stock += stock_vol[0]
	d_volatile_stock -= stock_vol[num_days - 1 - 1]
	d_momentum_stock += stock_mom[0]
	d_momentum_stock -= stock_mom[num_days - 1 - 1]



#Stock Loop Priming
index_open_price = float(index_data[0].values()[6])
index_close_price = float(index_data[0].values()[7])
mean_index = (index_open_price + index_close_price)/2
index_means.insert(0, mean_index)

for day in index_data[1:num_days]:
	#Index Processing
	index_open_price = float(day.values()[6])
	index_close_price = float(day.values()[7])
	mean_index = (index_open_price + index_close_price)/2

	index_means.insert(0, mean_index)
	volatile_index_total.insert(0, 0)
	momentum_index_total.insert(0, 0)

	index_vol.insert(0, index_means[1] - index_means[0])
	index_mom.insert(0, index_close_price - index_open_price)

	d_volatile_index += index_vol[0]
	d_momentum_index += index_mom[0]

#Main Data Processing Loop
for day in index_data[num_days:]:
	#Index Processing

	index_open_price = float(day.values()[6])
	index_close_price = float(day.values()[7])
	mean_index = (index_open_price + index_close_price)/2

	print mean_index

	index_means.insert(0, mean_index)
	volatile_index_total.insert(0, d_volatile_stock)
	momentum_index_total.insert(0, d_momentum_stock)

	index_vol.insert(0, index_means[1] - index_means[0])
	index_mom.insert(0, index_close_price - index_open_price)

	d_volatile_index += index_vol[0]
	d_volatile_stock -= index_vol[num_days - 1 - 1]
	d_momentum_index += index_mom[0]
	d_momentum_stock -= index_mom[num_days - 1 - 1]



plt.figure(1)
plt.subplot(211)
plt.plot(volatile_stock_total, label='Volatility')
plt.plot(momentum_stock_total, label='Momentum')
plt.title('Volatility and Momentum')
plt.ylabel('Value')
plt.legend()

plt.subplot(212)
plt.plot(stock_means)
plt.xlabel('Day')
plt.ylabel('Stock Value')
plt.title('Yahoo Stock Over Time')
#plt.show()

plt.figure(2)
plt.subplot(211)
plt.plot(volatile_index_total, label='Volatility')
plt.plot(momentum_index_total, label='Momentum')
plt.title('Volatility and Momentum')
plt.ylabel('Value')
plt.legend()

plt.subplot(212)
plt.plot(index_means)
plt.xlabel('Day')
plt.ylabel('Index Value')
plt.title('NASDAQ Over Time')
#plt.show()

#for i in stock_means:










