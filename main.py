from flask import Flask, render_template, request, session
import os
import uuid
from logging.handlers import RotatingFileHandler
import logging
from stock_main import get_stock_plot
from stock_news import get_stock_news

app = Flask(__name__)
# secure the cookied session
app.config['SECRET_KEY'] = os.urandom(24)


@app.before_request
def before_request():
    # close session after close browser
    session.permanent = False


@app.route('/')
def index():
    # session.permanent = False
    if 'my_id' not in session:
        session['my_id'] = str(uuid.uuid1())
    app.logger.info('%s visited!' % (session['my_id']))
    return render_template('index.html')


@app.route('/crawler', methods=['POST'])
def success():

    if request.method == 'POST':
        stock_code = request.form['stock_code']
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        plot_pic_data = get_stock_plot(stock_code, from_date, to_date)
        res = get_stock_news(stock_code, from_date, to_date)
        stock_news = []
        if res is not None:
            for index, news in res.iterrows():
                stock_news.append({
                    'type': str(news['type']),
                    'title': str(news['title']),
                    'date': str(news['date']),
                    'url': str(news['url'])
                })

        return render_template('index.html', stock_news=stock_news, plot_pic_data=plot_pic_data, stock_code=stock_code, from_date=from_date, to_date=to_date)


if __name__ == '__main__':
    # add logger
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run()
