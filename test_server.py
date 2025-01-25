from flask import Flask, render_template, session, request, redirect
from os import urandom

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(16)


def auth(route):
    def inner(*args, **kwargs):
        if 'email' in session:
            return route(*args, **kwargs)
        else:
            return redirect('/sign-in/')


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')
    data = dict(request.form)
    data['country'] = 'Russia! GOYDA!'
    data['about'] = None
    data['path'] = None
    db.add_user(data)
    session['email'] = data['email']
    return redirect('/dashboard/')


@app.route('/sign-in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')
    data = dict(request.form)
    uid = db.get_user_id(data['email'], 1)
    user = db.get_user(uid, 1)
    # orms were invented in 1995... People before 1995:
    if user and user[0][4] == data['password']:
        session['email'] = data['email']
        return redirect('/dashboard/')
    else:
        return render_template('sign-in.html', error='Неверные данные!')


@app.route('/dashboard/')
def dashboard():
    # Месяцы как категории
    labels = [str(i) for i in range(1, 28)]

    # Количество ПРАВИЛЬНО решённых задач по кадому номеру
    correct = [i for i in range(10, 38)]

    # Количество НЕПРАВИЛЬНО решённых задач по каждому номеру
    incorrect = [c for c in correct]

    return (render_template('dashboard.html', labels=labels, correct=correct, incorrect=incorrect))


@app.route('/text-lesson/')
def text_lesson():
    return render_template('text-lesson.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

