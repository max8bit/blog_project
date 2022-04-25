from flask import render_template
from app import app
from forms import LoginForm

@app.route('/')
def main_page():
    return render_template('index.html')