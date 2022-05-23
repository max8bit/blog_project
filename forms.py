from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from models import User


class LoginForm(FlaskForm):  # пишу свою форму поверх базовой формы из фласка
    username = StringField('Имя пользователя: ')
    password = PasswordField('Пароль: ')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = SubmitField('Имя пользователя', validators=[DataRequired()])
    email = SubmitField('Email', validators=[DataRequired()])
    password = SubmitField('Password', validators=[DataRequired()])
    password_again = SubmitField('Password(подтвержденние): ',
    validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Регистрация')

    def check_username(self, username):
        user = User.query.filter(username = username.data)
        if user is not None:
            raise ValidationError('Пользователь с таким ником уже зарегистрирован!')

    def check_email(self, email):
        user = User.query.filter(email = email.data)
        if user is not None:
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован!')