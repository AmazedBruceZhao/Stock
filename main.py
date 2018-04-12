from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawler', methods=['POST'])
def success():
    if request.method == 'POST':
        code = request.form['stock_code']
        from_date = request.form['from_date']
        to_date = request.form['to_date']

if __name__ == '__main__':
    app.run()
