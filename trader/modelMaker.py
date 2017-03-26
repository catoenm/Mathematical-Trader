

################################################
#	File responsible for creation of SVM models
#
#	Author: Mitchell Catoen
################################################

from helpers import *
import matplotlib.pyplot as plt
import svmpy
import numpy as np
import dill
import pickle


stock_names = ["YHOO", "BBRY", "GOOG", "AAPL", "MSFT"]
date_1 = '2009-01-17'
date_2 = '2014-01-17'
movo_days = 25
pred_days = 25

for i in range(0, len(stock_names)):
	vo_stock, mo_stock, me_stock, vo_index, mo_index, me_index = process_stock_data(date_1, date_2, movo_days, stock_names[i])
	inc_dec = make_dataset(me_stock, pred_days)

	################################################
	#
	#	Train SVM Predictor
	#	Data Format: mom stock, vol stock, mom index, vol index
	#	Predictor Call: predictor.predict([1, 2, 3, 4])
	#
	################################################

	# plot_figure_triple(me_stock, mo_stock, vo_stock, 'Yahoo Stock Over Time', 1)
	# plot_figure_triple(me_index, mo_index, vo_index, 'NASDAQ Index Over Time', 2)
	# plot_figure_double(me_stock, inc_dec, "Yahoo Stock Over Time", 3)


	samples = np.column_stack((mo_stock, vo_stock, mo_index, vo_index))
	predictor = trainSVM(samples, np.asarray(inc_dec))

	pickle.dump(predictor, open("stock_models/" + stock_names[i] + ".bin", "wb"))





	