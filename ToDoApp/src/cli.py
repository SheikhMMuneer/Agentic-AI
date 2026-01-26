from storage.storage import load_tasks,save_tasks
from src.core import show_task,add_task,mark_done,delete_task


def run_cli():
    
    tasks = load_tasks() 

    while True:
        print("""===To do List Cli===
                1)Show Task
                2)Add Task
                3)Mark Done Task
                4)Delete Task
                0)Exit
               """)
        
        choice = input("Pick an option:")
        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            save_tasks(tasks)
            print("Task saved Allah Hafiz")
            break
        else:
            print("Invalid Option")


