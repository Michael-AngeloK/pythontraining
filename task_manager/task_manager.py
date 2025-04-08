from task_manager.task import Task, TimedTask

class Task_Manager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def __str__(self):
        return "\n".join(str(task) for task in self.tasks) if self.tasks else 'No Tasks'
    
    def __iter__(self):
        return iter(self.tasks)
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task ID {task_id} not found")
    
    def add_task(self, task):
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        
    def filter_tasks(self, status=None, priority=None):
        """Generator yielding tasks"""
        for task in self.tasks:
            if status is not None and task.completed != status:
                continue
            if priority is not None and task.priority.lower() != priority.lower():
                continue
            yield task