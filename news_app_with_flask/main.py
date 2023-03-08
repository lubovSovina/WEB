from flask import Flask

from data import db_session, news_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()