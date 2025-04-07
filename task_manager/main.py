

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
    
    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.title} {self.priority}"
        
    def complete_task(self):
        self.completed = True
    
class TimeTask(Task):
    def __init__(self, title, priority, deadline):
        super().__init__(title, priority)
        self.deadline = deadline
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} (Due: {self.deadline})"
    
timed_task = TimeTask("Do homework", "middle", "07.04.25")
timed_task.complete_task()
print(timed_task)