def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: called '{func.__name__}' on task '{args[0].title}'")
        return func(*args, **kwargs)
    return wrapper
