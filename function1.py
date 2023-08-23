import constnts
import random
from PIL import Image


def input_username():
    username = input("please write your username:")
    return username


def get_3_tasks():
    tasks = []
    print("here are your tasks for today:")

    for i in range(3):
        tasks.append(random.choice(constnts.regular_tasks))
        constnts.regular_tasks.remove(tasks[i])
    for i in range(len(tasks)):
        print(tasks[i])


def print_image():
    print("please enter the path in the computer for your image: ")
    path = input()
    img = Image.open(path)
    img.show()


