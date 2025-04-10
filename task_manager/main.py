import argparse
from task_manager.task_manager import Task_Manager
from task_manager.task import Task, TimedTask

VALID_PRIORITIES = {'low', 'medium', 'high'}

parser = argparse.ArgumentParser(description="Task Manager CLI")
parser.add_argument("--add", type=str, help="Add a new task")
parser.add_argument("--priority", type=str, help="Task priority")
parser.add_argument("--deadline", type=str, help="Deadline (for timed task)")
parser.add_argument("--list", action="store_true", help="List all tasks")
parser.add_argument("--complete", type=int, help="Mark task complete by ID")

args = parser.parse_args()

manager = Task_Manager()
manager.add_task(Task("Do homework", "medium"))
manager.add_task(TimedTask("Dentist appointment", "high", "08.04.25"))
manager.add_task(Task("Call friend", "low"))

if args.add:
    if args.priority:
        args.priority = args.priority.lower()
        if args.priority not in VALID_PRIORITIES:
            print(f"Error: Priority must be one of {VALID_PRIORITIES}")
            exit(1)
    else:
        args.priority = "low"    
    
    if args.deadline:
        task = TimedTask(args.add, args.priority, args.deadline)
    else:
        task = Task(args.add, args.priority)
    
    manager.add_task(task)
    print(f"Added task: {task}")
    
elif args.list:
    print("Displaying all tasks:")
    print(manager)
    
elif args.complete:
    try:
        task = manager.get_task(args.complete)
        task.complete_task()
        print(f"Task {task.id} marked as complete: {task.title}")
    except ValueError as e:
        print(f"Invalid Id: {e}")
    
print("Tasks:")
for task in manager:
    print(task)
    
print("Complete tasks:")
for task in manager.filter_tasks(status=True):
    print(task)
    