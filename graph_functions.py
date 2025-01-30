import db_functions as db
import time

from db_functions import get_attempts_by_task_type

def convert_time(current_time):
    result = (time.localtime(current_time).tm_year, time.localtime(current_time).tm_mon)
    return result

def convert_attempts_by_months(user_id):
    all_attempts = db.get_attempts_of_user(user_id)
    for i in range(len(all_attempts)):
        all_attempts[i][5] = convert_time(all_attempts[i][5])
    cur_index = 0
    result = {}
    correct = 0
    wrong = 0
    while cur_index < len(all_attempts):
        if cur_index == 0 or all_attempts[cur_index][5] == all_attempts[cur_index - 1][5]:
            result[all_attempts[cur_index][5]] = (correct, wrong)
            correct = 0
            wrong = 0
        else:
            if all_attempts[cur_index][4]:
                correct += 1
            else:
                wrong += 1
    return result

def convert_attempts_by_type(user_id):
    all_attempts = get_attempts_by_task_type(user_id)
    cur_index = 0
    result1 = []
    result2 = []
    result3 = []
    correct = 0
    wrong = 0
    while cur_index < len(all_attempts):
        if cur_index == 0 or all_attempts[cur_index][2] == all_attempts[cur_index - 1][2]:
            result1.append(all_attempts[cur_index][3])
            result2.append(correct)
            result3.appen(wrong)
            correct = 0
            wrong = 0
        else:
            if all_attempts[cur_index][1]:
                correct += 1
            else:
                wrong += 1
    return result1, result2, result3
