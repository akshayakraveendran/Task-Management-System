# Task Management System

This is a command-line-based Task Management System built using Django's management commands. It allows users to add, view, update, and delete tasks with status tracking.

## Features
- Add a new task with a description, deadline, and status (pending/completed).
- View all tasks or filter by status (pending/completed).
- Update task details and status.
- Delete a task.
- User-friendly menu navigation with an option to return to the main menu.

## Prerequisites
- Python (>=3.7)
- Django (>=3.0)

## Installation & Setup
1. Clone the repository or add this script to your Django project.
2. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
3. Run the task manager command:
   ```sh
   python manage.py task_cli
   ```

## Usage
Once you run the command, the system will display a menu with the following options:

1. **Add a task** - Allows users to input a task description, deadline, and status.
2. **View all tasks** - Displays all tasks stored in the database.
3. **View pending tasks** - Filters and shows only tasks marked as "pending".
4. **View completed tasks** - Filters and shows only tasks marked as "completed".
5. **Update a task** - Lets users modify task details, including description and status.
6. **Delete a task** - Deletes a specific task by ID.
7. **Exit** - Terminates the program.

Each menu option includes a prompt to return to the main menu after completion.
