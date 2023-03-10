from flask import Flask, render_template

app = Flask(__name__)


# работа с параметрами и передача их в шаблон
@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['title'] = 'Домашняя страница'
    params['username'] = 'Ученик Лицея Академии Яндекса'
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
