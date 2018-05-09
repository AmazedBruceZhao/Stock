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
    # get history
    res_table = ts.get_hist_data(code, start, end)
    sh_res_table = ts.get_hist_data('sh', start, end)
    print(res_table)
    # string to date
    print(res_table.index.values)
    x_date = [datestr2num(i) for i in res_table.index.values]
    # draw
    fig = plt.figure(figsize=(10, 5))
    # matplotlib doesn't support chinese
    plt.title(u"percentage - date")
    plt.xlabel(u"date")
    plt.ylabel(u"percentage")
    plt.plot_date(x_date, res_table['p_change'], '-', label="change percentage")
    plt.plot_date(x_date, sh_res_table['p_change'], '-', label="change percentage")
    # plt.legend()
    plt.grid(True)
    # fig.savefig('test.png', format='png')
    # plt.show()
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data


def stock_exists(code):
    stock_list = ts.get_stock_basics()
    if code in stock_list.index:
        name = stock_list.ix[code]['name']
        print(name)
        return name
    return False


