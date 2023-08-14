class Task:
    def __init__(self, title, description):
        self.title = title
        self.completed = False
        self.description = description
        
    def mark_completed(self):
        self.completed = True
        
    def info(self):
        print(f"""
              {self.title.upper()}
              {self.description}
              """)

class TaskList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        return completed_tasks
    
    def list_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        return pending_tasks

task1 = Task("clean house", "Milk, eggs, bread")
task2 = Task("update a code ", "play movil games")
task3 = Task("Exercise", "30 minutes of jogging")

# task finaly
task1.mark_completed()

#create a list 

task_list = TaskList()

#add task in list
task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)

completed_tasks = task_list.list_completed_tasks()
pending_tasks = task_list.list_pending_tasks()

print("Completed tasks:")
for task in completed_tasks:
    task.info()

print("\nPending tasks:")
for task in pending_tasks:
    task.info()

 
        
        
    

    