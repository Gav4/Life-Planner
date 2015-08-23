__author__ = 'Gav'

def list_all(task_list):  # list all tasks
    for task in task_list:
        print(task_list.index(task), end =" :")
        print(task)
    print()

