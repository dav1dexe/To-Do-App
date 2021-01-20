from flask import Flask, render_template, request, redirect, flash, session, url_for
from db import Database
import bcrypt


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = '+dZL@dds^xyzNG.ifgjWO-]8v>Cj)xe1}t@CiEyNU4#)8ZenoaOeN"3+'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' in session:
        data = Database()
        user_data = data.check_data(session.get('user'))
        posts = data.get_posts(session.get('user'))
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['text']
            data.add_post(session.get('user'), title, text)
            flash('Данные были отправлены!')
            return redirect(url_for('profile'))
        else:
            return render_template('profile.html', user_data=user_data, posts=posts)
    else:
        return render_template('404.html', cause='Чтобы просмотреть эту страницу, нужно авторизоваться!')


@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if 'user' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        data = Database()
        login = request.form['login']
        password = request.form['pass'].encode('UTF-8')
        user_data = data.check_data(login.lower())
        if user_data:
            password_hash = bcrypt.checkpw(password, user_data[2])
            if password_hash:
                session['user'] = login
                return redirect(url_for('profile'))
            else:
                flash('Пароль не совпадает!')
                return render_template('auth.html')
        else:
            flash('Не найден аккаунт!')
            return render_template('auth.html')
    else:
        return render_template('auth.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if 'user' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        data = Database()
        login = request.form['username']
        password = request.form['pass'].encode('UTF-8')
        password2 = request.form['pass2'].encode('UTF-8')
        name = data.check_data(login.lower())
        if not name:
            if len(login) > 3 and len(password) > 4:
                if password == password2:
                    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
                    data.add_user(login, password_hash)
                    return redirect(url_for('auth'))
                else:
                    flash('Пароли не совпадают!')
                    return render_template('register.html')
            else:
                flash('Логин и пароль должны быть больше 4 символов')
                return render_template('register.html')
        else:
            flash(f'Пользователь с именем {login} уже зарегистрирован')
            return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))
    else:
        return render_template('404.html', cause='Ты не авторизован')

