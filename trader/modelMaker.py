

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


stock_names = ["YHOO", "BBRY", "GOOG"]
date_1 = '2005-01-17'
date_2 = '2010-01-17'
movo_days = 25
pred_days = 25


vo_stock, mo_stock, me_stock, vo_index, mo_index, me_index = process_stock_data(date_1, date_2, movo_days, stock_names[0])
inc_dec = make_dataset(me_stock, pred_days)


################################################
#
#	Train SVM Predictor
#	Data Format: mom stock, vol stock, mom index, vol index
#	Predictor Call: predictor.predict([1, 2, 3, 4])
#
################################################


samples = np.column_stack((mo_stock, vo_stock, mo_index, vo_index))
predictor = trainSVM(samples, np.asarray(inc_dec))

pickle.dump(predictor, open("myobject", "wb"))