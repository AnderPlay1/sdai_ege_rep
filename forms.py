from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')

class CommentForm(FlaskForm):
    content = TextAreaField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Отправить')