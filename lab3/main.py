from folder_monitor import FolderMonitor

# Example of usage:
folder_monitor = FolderMonitor("folder1")

while True:
    user_input = input("Enter command: ")
    if user_input.startswith("commit"):
        folder_monitor.commit()
        print("Snapshot committed.")
    elif user_input.startswith("info"):
        _, filename = user_input.split(" ", 1)
        folder_monitor.info(filename)
    elif user_input.startswith("status"):
        folder_monitor.status()
    elif user_input.lower() == "exit":
        break
    else:
        print("Invalid command. Please try again.")
