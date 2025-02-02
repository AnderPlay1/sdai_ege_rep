from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm, PostForm, CommentForm
from models import User, Post, Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash('Вход выполнен успешно!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверный email или пароль', 'danger')
    return render_template('login.html', form=form)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author_id=1)  # Здесь нужно будет заменить на текущего пользователя
        db.session.add(post)
        db.session.commit()
        flash('Пост успешно создан!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post_id=post.id, author_id=1)  # Здесь нужно будет заменить на текущего пользователя
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен!', 'success')
        return redirect(url_for('post_detail', post_id=post.id))
    return render_template('post_detail.html', post=post, form=form)

if __name__ == '__main__':
    app.run(debug=True)