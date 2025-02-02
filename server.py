# Инициализация базы данных (создание таблиц, если их нет)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'forum.db'

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            topic_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL, 
            FOREIGN KEY (topic_id) REFERENCES topics (id)
        )
    ''')
    conn.commit()
    conn.close()

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Возвращает строки в виде словарей
    return conn

# Главная страница
@app.route('/')
def index():
    conn = get_db_connection()
    topics = conn.execute('SELECT * FROM topics').fetchall()
    conn.close()
    return render_template('index.html', topics=topics)

# Страница темы
@app.route('/topic/<int:topic_id>', methods=['GET', 'POST'])
def topic(topic_id):
    conn = get_db_connection()
    if request.method == 'POST':
        comment_content = request.form['comment']
        user_id = 1  # Здесь можно добавить логику для получения ID текущего пользователя
        conn.execute('INSERT INTO comments (content, topic_id, user_id) VALUES (?, ?, ?)',
                     (comment_content, topic_id, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('topic', topic_id=topic_id))

    topic = conn.execute('SELECT * FROM topics WHERE id = ?', (topic_id,)).fetchone()
    comments = conn.execute('SELECT * FROM comments WHERE topic_id = ?', (topic_id,)).fetchall()
    conn.close()
    return render_template('topic.html', topic=topic, comments=comments)

# Создание новой темы
@app.route('/create_topic', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO topics (title, content) VALUES (?, ?)',
                     (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create_topic.html')

# Админская панель
@app.route('/admin')
def admin():
    conn = get_db_connection()
    topics = conn.execute('SELECT * FROM topics').fetchall()
    comments = conn.execute('SELECT * FROM comments').fetchall()
    conn.close()
    return render_template('admin.html', topics=topics, comments=comments)

# Удаление темы
@app.route('/delete_topic/<int:topic_id>')
def delete_topic(topic_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM topics WHERE id = ?', (topic_id,))
    conn.execute('DELETE FROM comments WHERE topic_id = ?', (topic_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

# Удаление комментария
@app.route('/delete_comment/<int:comment_id>')
def delete_comment(comment_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM comments WHERE id = ?', (comment_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    init_db()  # Инициализация базы данных при запуске приложения
    app.run(debug=True)

