# -*- coding: utf-8 -*-
import re
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib.pylab import datestr2num

code = '600606'
#get stock name
if re.match(r'\d{6}', code):
    stock_list = ts.get_stock_basics()
    if code in stock_list.index:
        name = stock_list.ix[code]['name']
        print(name)

        # get history
        res_table = ts.get_k_data(code, '2018-01-01', '2018-01-05')
        print(res_table)
        #string to date
        print(res_table['date'])
        #x_date = [datestr2num(i) for i in res_table['date']]
        #draw
        plt.figure(figsize=(10, 5))
        #matplotlib doesn't support chinese
        plt.title(u"close - date")
        plt.xlabel(u"date")
        plt.ylabel(u"price")
        plt.plot_date(res_table['date'], res_table['close'], '-', label=u"stock at closing time")

        plt.legend()
        plt.grid(True)
        plt.show()


