from pymongo import MongoClient
from bson.objectid import ObjectId

class Task: 
    def __init__(self, title, created_at, deadline, description='', is_done=False, priority='Normal'):
        self.title = title
        self.is_done = is_done
        self.priority = priority
        self.created_at = created_at
        self.deadline = deadline
        self.description = description

    def to_dictionary(self):
        return {
            'title': self.title,
            'is_done': self.is_done,
            'priority': self.priority,
            'created_at': self.created_at,
            'deadline': self.deadline,
            'description': self.description
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            is_done=data.get('is_done', False),
            priority=data.get('priority', 'Normal'),
            created_at=data['created_at'],
            deadline=data['deadline'],
            description=data.get('description', '')
        )
    
class TaskManager:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="task_manager", collection_name="tasks"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_task(self, task: Task):
        task_dict = task.to_dictionary()
        self.collection.insert_one(task_dict)
        print(f"Task '{task.title}' added to the database.")

    def delete_task(self, task_id):
        self.collection.delete_one({'_id': ObjectId(task_id)})
        print(f"Task was deleted from the database.")
    
    def mark_done(self, task_id):
        self.collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'is_done': True}})
        print(f"Task was marked as done in the database.")

    def get_all_tasks(self):
        return list(self.collection.find())

    def get_tasks_by_priority(self, priority):
        return list(self.collection.find({'priority': priority}))
    
    def get_tasks_by_status(self, is_done): 
        return list(self.collection.find({'is_done': is_done}))  
      
class UrgentTask(Task):
    def __init__(self, title, created_at, deadline, description='', is_done=False):
        super().__init__(title, created_at, deadline, description, is_done, priority='Urgent')
