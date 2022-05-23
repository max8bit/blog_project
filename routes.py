from crypt import methods

from alembic.autogenerate import render
from flask import render_template, flash, redirect, url_for
from sqlalchemy.sql.functions import current_user

from app import app
from forms import LoginForm

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request for user{form.username.data}')
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login page', form=form)

@app.route('/register', methods=['GET', 'POST'])
def fregister():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('registr.html', form=form)