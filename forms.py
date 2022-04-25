from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):  # пишу свою форму поверх базовой формы из фласка
    username = StringField('Имя пользователя: ')
    password = PasswordField('Пароль: ')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')