from django.core.management.base import BaseCommand
from tasks.models import Task
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        menu_options = {
            "1": ("Add a task", self.add_task),
            "2": ("View all tasks", self.view_tasks),
            "3": ("View pending tasks", lambda: self.view_tasks(status="pending")),
            "4": ("View completed tasks", lambda: self.view_tasks(status="completed")),
            "5": ("Update a task", self.update_task),
            "6": ("Delete a task", self.delete_task),
            "7": ("Exit", self.exit_program),
        }

        while True:
            print("\nTask Management System")
            for key, (desc, _) in menu_options.items():
                print(f"{key}. {desc}")

            choice = input("\nEnter your choice: ").strip()
            action = menu_options.get(choice)

            if action:
                action[1]()  
            else:
                print("Invalid choice. Please try again.")



    def add_task(self):
        description = input("Enter task description: ").strip()
        deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ").strip()
        deadline = deadline if deadline else None
        status = input("Enter status (pending/completed): ").strip().lower()

        if status not in ['pending', 'completed']:
         status = 'pending' 

        task = Task(description=description, deadline=deadline,status=status)
        task.save()
        
        print(f"Task added: {task}")

        input("\nPress Enter to return to the main menu...")


    def view_tasks(self, status=None):
        tasks = Task.objects.all() if status is None else Task.objects.filter(status=status)
        
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")

        input("\nPress Enter to return to the main menu...")


    def update_task(self):
        task_id = input("Enter task ID to update: ").strip()
        
        try:
            task = Task.objects.get(id=task_id)
           
            print(f"Current Task: {task}")
            
            new_description = input("Enter new description (leave blank to keep the same): ").strip()
            new_status = input("Enter new status (pending/completed): ").strip().lower()

            if new_description:
                task.description = new_description
            if new_status in ["pending", "completed"]:
                task.status = new_status

            task.save()

            print("Task updated successfully.")
            input("\nPress Enter to return to the main menu...")

        except Task.DoesNotExist:
            print("Task not found.")


    def delete_task(self):
        task_id = input("Enter task ID to delete: ").strip()
        try:
            task = Task.objects.get(id=task_id)
            task.delete()

            print("Task deleted successfully.")
        except Task.DoesNotExist:
            print("Task not found.")
        
        input("\nPress Enter to return to the main menu...")


    def exit_program(self):
            print("Exiting... Goodbye!")
            exit()