# Import todoist API
from todoist_api_python.api import TodoistAPI

# Initial sync of your account
api = TodoistAPI("c2a871be87699ad039c0c6867d1536b08a56bf7b")

# Find all projectd
try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print("Error fetching projects:", error)

# Process tasks until explicitly aborted
while True:
    try:
        # Get completed tasks for project; replace 'your_project_id' with the actual project ID
        completed_items = api.get_completed_items(project_id='2297894868', limit=100)
        completed = completed_items.items  # Assuming completed items are stored in .items
        if not completed:
            break  # No completed tasks left, abort
    except Exception as error:
        print("Error fetching completed items:", error)
        break

# Check if completed is properly extracted and is iterable
if completed:
    for c in completed:
        try:
            api.delete_task(c.id)  # Accessing 'id' assuming completed items have this attribute
        except Exception as error:
            print(f"Error deleting task with ID {c.id}:", error)

print("Completed tasks deleted.")
