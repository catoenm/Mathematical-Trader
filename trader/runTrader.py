from yahoo_finance import Share
import matplotlib.pyplot as plt
from collections import deque

yahoo = Share('YHOO')
yahoo.refresh()
data = yahoo.get_historical('2016-01-01', '2017-04-17')

# 0 Volume
# 1	Symbol
# 2 Adj Close
# 3 High
# 4 Low
# 5 Date
# 6 Close
# 7 Open

#print data[0].values()[7]
num_days = 25

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

open_price = float(data[0].values()[6])
close_price = float(data[0].values()[7])
mean_stock = (open_price + close_price)/2
stock_means.insert(0, mean_stock)

index = 1
for day in data[1:num_days]:
	print index
	index+=1
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

	
for i in stock_means:
	print i


#Main Data Processing Loop
for day in data[num_days:]:
	print index
	index+=1
	open_price = float(day.values()[6])
	close_price = float(day.values()[7])
	mean_stock = (open_price + close_price)/2

	print "Open Price ", open_price
	print "Close Price ", close_price
	print "Mean Stock ", mean_stock

	stock_means.insert(0, mean_stock)
	stock_vol.insert(0, stock_means[1] - stock_means[0])
	stock_mom.insert(0, close_price - open_price)



	volatile_stock_total.insert(0, d_volatile_stock)
	momentum_stock_total.insert(0, d_momentum_stock)

	print "Adding ", stock_vol[0], " subtracting ", stock_vol[num_days - 1 - 1]
	d_volatile_stock += stock_vol[0]
	d_volatile_stock -= stock_vol[num_days - 1 - 1]
	d_momentum_stock += stock_mom[0]
	d_momentum_stock -= stock_mom[num_days - 1 - 1]


# plt.plot(volatile_stock_total)
# plt.plot(momentum_stock_total)
# plt.plot(stock_means)
# plt.xlabel('Day')
# plt.ylabel('Stock Value')
# plt.title('Yahoo Stock Over Time')
# plt.show()

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
plt.show()









