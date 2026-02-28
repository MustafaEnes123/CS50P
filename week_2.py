def main():
    projects = [
        {"name": "Project 1", "status": "In Progress"},
        {"name": "Project 2", "status": "Completed"},
        {"name": "Project 3", "status": "In Progress"}
    ]
    for project in projects:
        if project["status"] == "In Progress":
            print(f"Working on: {project['name']}")
    count = 5
    while count > 0:
        print(f"Next update in {count}...")
        count -= 1
main()
