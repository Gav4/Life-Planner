import pickle
from datetime import timedelta
from taskFunc import listall

import os

if os.path.isfile('taskFile2.list'):
    with open('taskFile2.list', 'rb') as taskFile:
        taskList = pickle.load(taskFile)  # taskList is automatically assigned to be a list.
else:
    print('no list file exists. Creating one now..')
    taskList = []



list_all()


# d = timedelta(microseconds=-1)
# print(d.days, d.seconds, d.microseconds)
# print(datetime.now())  # time and date
# print(datetime.now())  # time only

# from datetime import datetime
# Start of user interaction.
while True:
    choice = input('N=New task, L=List tasks, D=Delete, M=add mata data, Q=Quit \n')

    if choice == 'N' or choice == 'n':
        newTask = input('enter New task "name, duration in minutes" :').split(",")
        newTaskObject = [newTask[0], newTask[1], 5, 5, 1]

        d = timedelta(microseconds=-1)

        taskList.append(newTaskObject)
        os.system('cls')
        list_all()
        with open('taskFile2.list', 'wb') as taskFile:
            pickle.dump(taskList, taskFile)
    elif choice == 'L' or choice == 'l':
        list_all()
    elif choice == 'D' or choice == 'd':
        list_all()
        data = 1
        while True:
            try:
                data = int(input('what number item? \n'))
                break
            except ValueError:
                print("invalid input. not a number. Try again:")
        taskList.pop(data)
        os.system('cls')
        list_all()
        with open('taskFile2.list', 'wb') as taskFile:
            pickle.dump(taskList, taskFile)
    elif choice == 'M' or choice == 'm':
        num = int(input('what number item? \n'))
        task = taskList.pop(num)
        choice2 = input('F=friendship score, A=family, D=due date, V=value, H=health, L=love \n')
        # F,A,D,V,H,L stored in task[2 to 7]
        if choice2 == 'F' or choice2 == 'f':
            score = input('friendship score out of 10:')
            task[2] = score
            taskList.append(task)
        elif choice2 == 'A' or choice2 == 'a':
            score = input('score out of 10:')
            task = [task, score]
            taskList.append(task)
    elif choice == 'Q' or choice == 'q':
        break
    else:
        print('that is not a choice \n')