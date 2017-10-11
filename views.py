from app import app, bcrypt, db
from flask import Flask, request, redirect, render_template, session, flash, url_for, make_response

# from models import Post, User
# from forms import LoginForm, RegisterForm, NewPostForm

from flask_login import login_user, login_required, logout_user, LoginManager, current_user
@app.route('/')
def index():
    return 'hello, piano'
