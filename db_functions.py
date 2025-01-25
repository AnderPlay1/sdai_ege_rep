import sqlite3
from time import time

# Special  functions:

def get_id_type(num):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT id FROM Types WHERE num_in_ege").fetchall()[0]
    connect.close()
    return result       # id

def get_status_task(id_message):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT status FROM Messages WHERE ID = ?", [id_message]).fetchall()
    connect.close()
    return result[0][0]

def get_status_user(id_message):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT status FROM Messages WHERE ID = ?", [id_message]).fetchall()
    connect.close()
    return result[0][0]

def get_status_message(id_message):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT status FROM Messages WHERE ID = ?", [id_message]).fetchall()
    connect.close()
    return result[0][0]

# Add functions:

def add_task(data):         # dict: (text, answer, difficulty, num_in_ege, date, source)
    current = [data['text'], data['answer'], data['difficulty'], get_id_type(data['num_in_ege']), data['source'], time(), 1]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Users (text, answer, difficulty, source, ID_type, date, status) VALUES (?, ?, ?, ?, ?, ?, ?)", current)
    connect.commit()
    connect.close()

def add_user(data):     # dict (name, surname, patronymic, email, password, telephone, age, country, role (student, teacher, admin), about, path (path to the photo))
    current = [data['name'], data['surname'], data['patronymic'], data['email'], data['password'], data['telephone'], data['age'], data['country'], data['role'], data['about'], data['path'], time(), 1]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Users (name, surname, patronymic, email, password, telephone, age, country, role, about, path, date, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", current)
    connect.commit()
    connect.close()

def add_attempt(data):      # dict: (ID_student, ID_task, is_right, ID_course)
    current = [data['ID_student'], data['ID_task'], data['is_right'], data['answer'], time(), data['ID_result'], data['ID_course']]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Attempt (ID_student, ID_task, is_right, time) VALUES (?, ?, ?, ?, ?, ?, ?)", current)
    connect.commit()
    connect.close()

def add_result(data):       # dict: (score, time, ID_student, ID_option)
    current = [data['score'], data['time'], data['ID_student'], data['ID_option'], data['']]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Results (score, time, ID_student, ID_option) VALUES (?, ?, ?, ?)", current)
    connect.commit()
    connect.close()
    return

def add_student_into_course(data):     # dict: (ID_student, ID_course)
    current = [data['ID_student'], data['ID_course']]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Course_teachers VALUES (ID_student, ID_course) VALUES (?, ?)", current)
    connect.commit()
    connect.close()

def add_teacher_into_course(data):     # dict: (ID_teacher, ID_course)
    current = [data['ID_teacher'], data['ID_student']]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Course_Students VALUES (ID_teacher, ID_course) VALUES (?, ?)", current)
    connect.commit()
    connect.close()

def add_file(data):     # dict: (ID_task, path, type)
    current = [data['ID_task'], data['path'], data['type']]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Files VALUES (ID_task, path, type) VALUES (?, ?, ?)", current)
    connect.commit()
    connect.close()

def add_message(data): # dict: (name, text, ID_user, date)
    current = [data['name'], data['text'], data['ID_user'], data['date'], 1]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Messages VALUES (name, text, ID_user, date, status) VALUES (?, ?, ?, ?, ?)", current)
    connect.commit()
    connect.close()

# Get functions:

def get_all_tasks(status): # (1-active, 2-banned, 3-deleted)
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Tasks WHERE status = ?", [status]).fetchall()
    connect.close()
    return result       # [(id, text, answer, difficulty, ID_type, source, solution, status(1-active)]

def get_answers():
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT id, answer FROM Tasks").fetchall()
    connect.close()
    return result       # [(id, answer)...]

def get_courses(status): # (1-active, 2-banned, 3-deleted)
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Courses WHERE status = ? ORDER BT date", [status]).fetchall()
    connect.close()
    return result       # [(id, name, ID_teacher, about, is_public, date, status)]

def get_messages(status): # (1-active, 2-banned, 3-deleted)
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Messages WHERE status = ? ORDER BY date", [status]).fetchall()
    connect.close()
    return result  # [(id, name, text, ID_user, status(1-active), date]

def get_user(id_user, status):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Users WHERE id = ? AND status != 3", [id_user]).fetchall()
    connect.close()
    return result       # [(name, surname, patronymic, email, password, telephone, age, country, role (student, teacher, admin), about, path (path to the photo)), date, status (1-active, 2-banned, 3-deleted)]

def get_user_id(email, status): # (1-active, 2-banned, 3-deleted)
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Users WHERE email = ? AND status = ?", [email, status]).fetchall()
    connect.close()
    return result[0][0]     # id

def get_answer(id_task):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT answer FROM Tasks WHERE id = ?", [id_task]).fetchall()[0]
    connect.close()
    return result[0][0]       # answer (string)

def get_options():
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Options").fetchall()
    connect.close()
    return result  # [(id, name, ID_teacher)]

def get_tasks_for_option(id_option):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT id_task FROM Tasks_Options WHERE ID = ?", [id_option]).fetchall()
    connect.close()
    return result  # [(id_task)]

def get_task(id_task):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Tasks WHERE ID = ?", [id_task]).fetchall()[0]
    connect.close()
    return result  # [(id, )]

def get_lessons_for_course(id_course):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT id_lesson FROM Course_Lessons WHERE ID_course = ?", [id_course]).fetchall()
    connect.close()
    return result  # [(id_lesson)]

def get_files_for_lesson(id_lesson):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Information WHERE ID_lesson = ?", [id_lesson]).fetchall()
    connect.close()
    return result  # [(id, path, ID_lesson)]

def get_attempts_of_user_task(id_student, id_task):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Attempts WHERE ID_user = ? AND ID_task = ?", [id_student, id_task]).fetchall()
    connect.close()
    return result  # (ID, ID_student, ID_task, is_right, date)

def get_attempts_of_user(id_student):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM Attempts WHERE ID_user = ?", [id_student]).fetchall()
    connect.close()
    return result  # (ID, ID_student, ID_task, is_right, date)

def get_type_name(id_type):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT name FROM Type WHERE ID = ?", [id_type]).fetchall()
    connect.close()
    return result[0][0] # name

# Del functions

def del_user(id_user):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Users SET status=3 WHERE ID = ?", [id_user]).fetchall()
    connect.commit()
    connect.close()

def del_task(id_task):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Tasks SET status=3 WHERE ID = ?", [id_task]).fetchall()
    connect.commit()
    connect.close()

def del_message(id_message):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Messages SET status=3 WHERE ID = ?", [id_message]).fetchall()
    connect.commit()
    connect.close()

# Ban functions

def ban_user(id_user):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Users SET status=2 WHERE ID = ?", [id_user]).fetchall()
    connect.commit()
    connect.close()

def ban_task(id_task):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Tasks SET status=2 WHERE ID = ?", [id_task]).fetchall()
    connect.commit()
    connect.close()

def ban_message(id_message):
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Messages SET status=2 WHERE ID = ?", [id_message]).fetchall()
    connect.commit()
    connect.close()

def unban_user(id_user):
    if get_status_user(id_user) != 2:
        return False
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Users SET status=2 WHERE ID = ?", [id_user]).fetchall()
    connect.commit()
    connect.close()
    return True

def unban_task(id_task):
    if get_status_user(id_task) != 2:
        return False
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Tasks SET status=2 WHERE ID = ?", [id_task]).fetchall()
    connect.commit()
    connect.close()
    return True

def unban_message(id_message):
    if get_status_user(id_message) != 2:
        return False
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Messages SET status=1 WHERE ID = ?", [id_message]).fetchall()
    connect.commit()
    connect.close()
    return True

# Change functions

def change_user(id_user, data): #list or dict (name, surname, patronymic, email, password, telephone, age, country, role (student, teacher, admin), about, path (path to the photo))
    current = [data['name'], data['surname'], data['patronymic'], data['email'], data['password'], data['telephone'], data['age'], data['country'], data['role'], data['about'], data['path'], 1]
    current += [id_user]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Users SET name=?, surname=?, patronymic=?, email=?, password=?, telephone=?, age=?, country=?, role=?, about=?, path=?, status=?  WHERE ID = ?", current).fetchall()
    connect.commit()
    connect.close()

def change_task(id_task, data):     #dict: (text, answer, difficulty, num_in_ege, source)
    current = [data['text'], data['answer'], data['difficulty'], get_id_type(data['num_in_ege']), data['source'], time(), 1]
    current += [id_task]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Tasks SET text=?, answer=?, difficulty=?, ID_type=?, source=?, date=?, status=? WHERE ID = ?", current).fetchall()
    connect.commit()
    connect.close()

def change_message(id_message, data):       # dict: (name, text, ID_user, date)
    current = [data['name'], data['text'], data['ID_user'], data['date'], 1]
    current += [id_message]
    connect = sqlite3.connect("MAIN_BD.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Messages SET name=?, text=?, ID_user=?, date=?, status=? WHERE ID = ?", current).fetchall()
    connect.commit()
    connect.close()