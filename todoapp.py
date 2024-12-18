import argparse
import json
import os

# File to store tasks
FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "✔" if task["completed"] else "✗"
        print(f"[{task['id']}] {status} - {task['description']}")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")


def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task {task_id} marked as completed.")
            break
    else:
        print(f"Task {task_id} not found.")
    save_tasks(tasks)


def main():
    parser = argparse.ArgumentParser(description="A CLI-based To-Do App")
    subparsers = parser.add_subparsers(dest="command")

    # Add subcommands
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("id", type=int, help="Task ID")

    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Parse arguments
    args = parser.parse_args()

    # Execute commands
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "complete":
        complete_task(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
