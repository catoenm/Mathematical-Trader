

################################################
#Main Application File
#
#Author: Mitchell Catoen
################################################

from helpers import process_stock_data
from helpers import plot_figure
import matplotlib.pyplot as plt

movo_days = 20
pred_days = 10 #Note, an extra day is added
vo_stock, mo_stock, me_stock, vo_index, mo_index, me_index = process_stock_data(movo_days)

plot_figure(me_stock, mo_stock, vo_stock, 'Yahoo Stock Over Time')
plot_figure(me_index, mo_index, vo_index, 'NASDAQ Index Over Time')

#Create a data set of Increased/Decreased from means

inc_dec = []
for i in range(pred_days, len(me_stock)):
	inc_dec.append(me_stock[i] > me_stock[i - pred_days])

plt.figure(1)
plt.subplot(211)
plt.plot(me_stock)
plt.xlabel('Day')
plt.ylabel('Value')
plt.title("Yahoo Stock Over Time")

plt.subplot(212)
plt.plot(inc_dec)
plt.xlabel('Day')
plt.ylabel('Value')
plt.title("Increase or Decrease in Last 20")
plt.show()

print "Inc: ", len(inc_dec), "Vol: ", len(vo_stock), "Mom: ", len(mo_stock)








