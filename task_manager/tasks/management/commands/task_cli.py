from django.core.management.base import BaseCommand
from tasks.models import Task
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        while True:
            print("\nTask Management System")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. View pending tasks")
            print("4. View completed tasks")
            print("5. Update a task")
            print("6. Delete a task")
            print("7. Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks(status="pending")
            elif choice == "4":
                self.view_tasks(status="completed")
            elif choice == "5":
                self.update_task()
            elif choice == "6":
                self.delete_task()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice.. Please try again.")

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

    def view_tasks(self, status=None):
        tasks = Task.objects.all() if status is None else Task.objects.filter(status=status)
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")

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