from task_manager.task_manager import Task_Manager
from task_manager.task import Task, TimedTask

manager = Task_Manager()
manager.add_task(Task("Do homework", "Medium"))
manager.add_task(TimedTask("Dentist appointment", "High", "08.04.25"))
manager.add_task(Task("Call friend", "Low"))

print("All tasks:")
for task in manager:
    print(task)
    
task = manager.get_task(1)
task.complete_task()

print("Complete tasks:")
for task in manager.filter_tasks(status=True):
    print(task)