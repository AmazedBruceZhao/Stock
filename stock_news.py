import tushare as ts
from datetime import datetime
from datetime import timedelta


def get_stock_news(code, start, end):
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')

    res = None
    while start_date <= end_date:
        try:
            temp = ts.get_notices(code, start_date.strftime("%Y-%m-%d"))
        except:
            start_date += timedelta(days=1)
            continue
        print(temp)
        if res is None:
            res = temp
        else:
            res = res.append(temp, ignore_index=True)
        start_date += timedelta(days=1)

    return res


