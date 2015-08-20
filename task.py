import pickle
from datetime import timedelta, datetime
import os

if os.path.isfile('taskFile2.list'):
    with open('taskFile2.list', 'rb') as taskFile:
        taskList = pickle.load(taskFile)  # taskList is automatically assigned to be a list.
else:
    print('no list file exists. Creating one now..')
    taskList = []

def listAll():  # list all tasks
   for task in taskList:
       print(taskList.index(task), end=" :")
       print(task)
   print()

listAll()


        # d = timedelta(microseconds=-1)
        # print(d.days, d.seconds, d.microseconds)
#print(datetime.now())  # time and date
#print(datetime.now())  # time only

# from datetime import datetime

i = str(input('date'))

try:
    dt_start = datetime.strptime(i, '%Y, %m, %d')
except ValueError:
    print('Incorrect format')

print(dt_start)

while True:
    choice = input('N=New task, L=List tasks, D=Delete, M=add mata data to a task M, Q=Quit \n')
    if choice == 'N' or choice == 'n':
        newTask = input('enter New task:')
        d = timedelta(microseconds=-1)
       
        newTask = [newTask,5,5,1,]
        taskList.append(newTask)
        os.system('cls')
        listAll()
        with open('taskFile2.list', 'wb') as taskFile:
            pickle.dump(taskList, taskFile)
    elif choice == 'L' or choice == 'l':
        listAll()
    elif choice == 'D' or choice == 'd':
        listAll()
        data = int(input('what number item? \n'))
        taskList.pop(data)
        os.system('cls')
        listAll()
        with open('taskFile2.list', 'wb') as taskFile:
            pickle.dump(taskList, taskFile)
    elif choice == 'M' or choice == 'm':
        data = int(input('what number item? \n'))
        task = taskList.pop(data)
        choice2 = input('F=friendship score, A=family, E=length , D=due date, V=value, H=health, L=love \n')
        if choice2 == 'F' or choice2 == 'f':
            score = input('score out of 10:')
            task = [task, score]
            taskList.append(task)
        elif choice2 == 'A' or choice2 == 'a':
            score = input('score out of 10:')
            task = [task, score]
            taskList.append(task)

            ##upto here A family..and how to keep meta data in order. ie F is [1]....


    elif choice == 'Q' or choice == 'q':
        break
    else:
        print('that is not a choice \n')



