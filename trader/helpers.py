

################################################
#Helper Functions Designed to Abstract
#Interface with Yahoo Finance Application
#
#Author: Mitchell Catoen
################################################

import svmpy
import logging
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools
import argh

def make_dataset(me, pred_days):
	inc_dec = []
	for i in range(0, len(me) - pred_days):
		if (me[i] < me[i + pred_days]):
			inc_dec.append(-1.0)
		else:
			inc_dec.append(1.0)
	return inc_dec

def run_test(num_days, predictor, inc_dec, mo_stock, vo_stock, mo_index, vo_index):
	hit = 0
	for i in range (0, len(inc_dec) - 1):
		prediction = predictor.predict([mo_stock[i], vo_stock[i], mo_index[i], vo_index[i]])
		if prediction == inc_dec[i]:
			hit = hit + 1
	print "Hit Percentage: ", float(hit)/len(inc_dec)*100.0, "%"


def process_stock_data(date_1, date_2, num_days):
	from yahoo_finance import Share

	nasdaq = Share('^IXIC')
	yahoo = Share('BBRY')
	nasdaq.refresh()
	yahoo.refresh()
	index_data = nasdaq.get_historical(date_1, date_2)
	data = yahoo.get_historical(date_1, date_2)

	# 0 Volume
	# 1	Symbol
	# 2 Adj Close
	# 3 High
	# 4 Low
	# 5 Date
	# 6 Close
	# 7 Open

	#print len(index_data)
	#print len(data)
	#print "Index Open", index_data[0].values()[7]

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
		#volatile_stock_total.insert(0, 0)
		#momentum_stock_total.insert(0, 0)

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
		#volatile_index_total.insert(0, 0)
		#momentum_index_total.insert(0, 0)

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

		index_means.insert(0, mean_index)
		volatile_index_total.insert(0, d_volatile_stock)
		momentum_index_total.insert(0, d_momentum_stock)

		index_vol.insert(0, index_means[1] - index_means[0])
		index_mom.insert(0, index_close_price - index_open_price)

		d_volatile_index += index_vol[0]
		d_volatile_stock -= index_vol[num_days - 1 - 1]
		d_momentum_index += index_mom[0]
		d_momentum_stock -= index_mom[num_days - 1 - 1]

	return volatile_stock_total, momentum_stock_total, stock_means, volatile_index_total, momentum_index_total, index_means

def plot_figure_triple(me, mo, vo, title):
	import matplotlib.pyplot as plt

	plt.figure(1)
	plt.subplot(211)
	plt.plot(vo, label='Volatility')
	plt.plot(mo, label='Momentum')
	plt.title('Volatility and Momentum')
	plt.ylabel('Value')
	plt.legend()

	plt.subplot(212)
	plt.plot(me)
	plt.xlabel('Day')
	plt.ylabel('Value')
	plt.title(title)
	plt.show()

def plot_figure_double(me, inc, title):
	plt.figure(1)
	plt.subplot(211)
	plt.plot(me)
	plt.xlabel('Day')
	plt.ylabel('Value')
	plt.title(title)

	plt.subplot(212)
	plt.plot(inc)
	plt.xlabel('Day')
	plt.ylabel('Value')
	plt.title("Increase or Decrease in Last 20")
	plt.show()

def trainSVM(feature_samples, label_samples):

    num_samples=41
    num_features=4
    grid_size=20

    samples = feature_samples
    labels = label_samples

    trainer = svmpy.SVMTrainer(svmpy.Kernel.linear(), 0.01)
    predictor = trainer.train(samples, labels)
    #plot(predictor, samples, labels, grid_size, filename)

    return predictor








