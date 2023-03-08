import json

from flask import Flask, render_template, redirect

from login_form import LoginForm

app = Flask(__name__)


# если число чётное - сообщение одно, когда нечётное - другое
@app.route('/odd_even')
def odd_even():
    return render_template('02_1_odd_even.html', num=3)


# список перебирается в шаблоне и автоматически перебирается
@app.route('/news')
def news():
    with open('news.json', 'rt', encoding='utf8') as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('02_2_news.html', news=news_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
