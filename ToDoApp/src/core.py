def show_task(tasks):
    if not tasks:
        print("No task aded yet")
    else:
        for i,task in enumerate(tasks,start=1):
            status = "Completed" if task["done"] else "Not Completed"
            print(f"{i},[{status} {task["title"]} ]")

def add_task(tasks):
    title = input("Enter your Task:").strip()
    if title:
        tasks.append({"title": title,"done": False })
        print(f"Added {title} successfully")


def mark_done(tasks):
    show_task(tasks)
    idx = int(input("Task Number:"))-1
    tasks[idx]["done"] = True
    print(f"Mark done :{ tasks[idx]["title"]}")


def delete_task(tasks):
    show_task(tasks)
    idx = int(input("Task Number:"))-1
    remove = tasks.pop(idx)
    print(f"Deleted : {remove["title"]}")

