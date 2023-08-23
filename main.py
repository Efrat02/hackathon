import constnts
import function1

names = []
save_info = {}
sum_points = 0
extra_task = False
how_many_extra = 0
how_many_users = int(input("how many people want to check their tasks today: "))

for j in range(how_many_users):
    names.append(function1.input_username())
    name = names[j]
    sum_points = 0
    print(f"hello {name}")

    for day in constnts.DAYS:
        print(f"today is {day} and its a good day to help the planet :)")
        function1.get_3_tasks()
        how_much_did = int(input("how many tasks did you do today? "))

        for image in range(how_much_did):
            function1.print_image()

        if how_much_did != constnts.LEN_DAILY_TASKS:
            print("good job!")

        else:
            if not extra_task:
                print(f"amazing! you just got 3 more tasks to do and earn points:"
                      f"each task worth {constnts.EXTRA_POINTS} whole points!!")
                extra_task = True

        print("did you do any extra tasks today?"
              "\nif yes please enter how many did you do: ")
        how_many_extra = int(input())

        sum_points += constnts.TASK_POINT * how_much_did
        sum_points += constnts.EXTRA_POINTS * how_many_extra

    save_info[name] = sum_points

