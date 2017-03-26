

################################################
#	Main Application File
#
#	Author: Mitchell Catoen
################################################

from helpers import *
import matplotlib.pyplot as plt
import svmpy
import numpy as np

movo_days = 25
pred_days = 25 #Note, an extra day is added

################################################
#
#	Make DataSet and Sample Set
#
################################################
# date_1 = '2010-01-17'
# date_2 = '2014-01-17'
date_1 = '2005-01-17'
date_2 = '2010-01-17'
vo_stock, mo_stock, me_stock, vo_index, mo_index, me_index = process_stock_data(date_1, date_2, movo_days)
inc_dec = make_dataset(me_stock, pred_days)

################################################
#
#	Plot Graphs
#
################################################


plot_figure_triple(me_stock, mo_stock, vo_stock, 'Yahoo Stock Over Time')
plot_figure_triple(me_index, mo_index, vo_index, 'NASDAQ Index Over Time')
plot_figure_double(me_stock, inc_dec, "Yahoo Stock Over Time")


################################################
#
#	Train SVM Predictor
#	Data Format: mom stock, vol stock, mom index, vol index
#	Predictor Call: predictor.predict([1, 2, 3, 4])
#
################################################


samples = np.column_stack((mo_stock, vo_stock, mo_index, vo_index))
predictor = trainSVM(samples, np.asarray(inc_dec))

################################################
#
#	Set New Dates and reprocess data
#
################################################

date_1 = '2010-01-17'
date_2 = '2017-01-17'
vo_stock, mo_stock, me_stock, vo_index, mo_index, me_index = process_stock_data(date_1, date_2, movo_days)
inc_dec = make_dataset(me_stock, pred_days)

################################################
#
#	Plot Graphs
#
################################################

plot_figure_triple(me_stock, mo_stock, vo_stock, 'Yahoo Stock Over Time')
plot_figure_triple(me_index, mo_index, vo_index, 'NASDAQ Index Over Time')
plot_figure_double(me_stock, inc_dec, "Yahoo Stock Over Time")

run_test(pred_days, predictor, inc_dec, mo_stock, vo_stock, mo_index, vo_index)






