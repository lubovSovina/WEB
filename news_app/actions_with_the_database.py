import datetime

from news_app.data.news import News
from news_app.data.users import User


def add_users(db_sess):
    user = User()
    user.name = "Пользователь 1"
    user.about = "Биография пользователя 1"
    user.email = "email1@em.ru"
    db_sess.add(user)
    user = User()
    user.name = "Пользователь 2"
    user.about = "Биография пользователя 2"
    user.email = "email2@em.ru"
    db_sess.add(user)
    user = User()
    user.name = "Пользователь 3"
    user.about = "Биография пользователя 3"
    user.email = "email3@em.ru"
    db_sess.add(user)
    db_sess.commit()


def get_first_user(db_sess):
    return db_sess.query(User).first()


def get_all_users(db_sess):
    return db_sess.query(User).all()


def update_username(id, name, db_sess):
    user = db_sess.query(User).filter(User.id == id).first()
    user.name = name
    user.created_date = datetime.datetime.now()
    db_sess.commit()


def delete_multiply_users(first_id, db_sess):
    db_sess.query(User).filter(User.id >= first_id).delete()
    db_sess.commit()


def delete_user(id, db_sess):
    user = db_sess.query(User).filter(User.id == id).first()
    db_sess.delete(user)
    db_sess.commit()


def add_news(db_sess):
    # 1 способ
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()
    # 2 способ
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()
    # 3 способ
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Личная запись", content="Эта запись личная",
                is_private=True)
    user.news.append(news)
    db_sess.commit()
