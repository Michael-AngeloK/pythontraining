from task_manager.decorators import log_action

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
        self.id = None
    
    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} ID:{self.id}, {self.title} {self.priority}"
    
    @log_action
    def complete_task(self):
        self.completed = True
    
class TimedTask(Task):
    def __init__(self, title, priority, deadline):
        super().__init__(title, priority)
        self.deadline = deadline
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} (Due: {self.deadline})"