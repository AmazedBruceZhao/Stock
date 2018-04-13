# -*- coding: utf-8 -*-
import re
import tushare as ts
import matplotlib
# keep the figure window from popping out
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pylab import datestr2num
from io import BytesIO
import base64


def get_stock_plot(code, start, end, session_id=''):
    # get stock name
    if re.match(r'\d{6}', code):
        stock_list = ts.get_stock_basics()
        if code in stock_list.index:
            name = stock_list.ix[code]['name']
            print(name)

            # get history
            res_table = ts.get_k_data(code, start, end)
            print(res_table)
            # string to date
            print(res_table['date'])
            x_date = [datestr2num(i) for i in res_table['date']]

            # draw
            fig = plt.figure(figsize=(10, 5))

            # matplotlib doesn't support chinese
            plt.title(u"close - date")
            plt.xlabel(u"date")
            plt.ylabel(u"price")
            plt.plot_date(x_date, res_table['close'], '-', label="stock at closing time")
            # plt.legend()
            plt.grid(True)

            # fig.savefig('test.png', format='png')
            # plt.show()
            sio = BytesIO()
            fig.savefig(sio, format='png')
            data = base64.encodebytes(sio.getvalue()).decode()
            return data

