#####################################
# import ground
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import print
from datetime import date
import importlib

DATABASE = importlib.import_module("plugins.internals.ToDo.database")
#####################################
console = Console()


def add_task():
    """
    Add a new task
    """
    task_title = input("Enter title: ")
    created_date = date.today().isoformat()
    tags = input("Enter tags (space separated): ")

    DATABASE.add_task_db(task_title, created_date, tags)


def show_tasks():
    """
    logs all the tasks from database
    """
    rows = DATABASE.log_tasks_db()
    # if no task break the function
    if not rows:
        print("No tasks found.")
        return
    table = Table(title="Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Date")
    table.add_column("Tags")
    table.add_column("Completed")
    # print each task with its state
    for row in rows:
        task_id, title, date, tags, done = row

        status = "✓" if done else "✗"

        table.add_row(
            str(task_id),
            title,
            date,
            tags,
            status,
        )
    console.print(table)


def complete_task():
    """
    change task completion status
    """
    show_tasks()
    print("Enter a task ID to modify task status: ")
    while True:
        choice = input("> ").strip()
        if not choice.isdigit():
            print("Invalid ID!\n")
            continue
        else:
            DATABASE.complete_task_db(choice)
            break


def delete_task():
    show_tasks()
    while True:
        task_id = input("Task ID: ").strip()
        if not task_id.isdigit():
            print("Please enter a valid task ID.")
            continue
        else:
            DATABASE.delete_task_db(task_id)
            break
    print("Task deleted.")


def search_by_tag():
    tag = input("Tag: ")

    rows = DATABASE.search_by_tag_db(tag)

    if not rows:
        print("No matching tasks.")
        return

    for row in rows:
        status = "✓" if row[4] else "✗"

        print(f"[{row[0]}] " f"{row[1]} " f"({row[2]}) " f"[{row[3]}] " f"{status}")


def main():
    print(Panel("Welcome to the RedbooK TodO App!\n"))
    while True:
        print(
            Panel.fit(
                "1. Add a new task\n2. Mark as completed\n3. Show tasks\n4. Delete a task\n5. Search tasks by tag\n6. Quit",
                title="Choose an option",
            )
        )
        try:
            choice = int(input("> ").strip())
        except ValueError:
            print("Please enter a number.")
            continue
        if choice not in range(1, 7):
            print("Invalid choice.")
            continue
        elif choice == 1:
            add_task()
        elif choice == 2:
            complete_task()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            search_by_tag()
        elif choice == 6:
            DATABASE.conn.close()
            print("Bye!")
            break


def register():
    return {
        "name": "tasks",
        "version": "0.1.0",
        "author": "inkitten",
        "description": "managing tasks",
        "commands": {"tasks": main},
    }


if __name__ == "__main__":
    main()
