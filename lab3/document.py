import os
from datetime import datetime

class Document:
    def __init__(self, folder_path, filename, extension, created_time, updated_time):
        self.folder_path = folder_path
        self.filename = filename
        self.extension = extension
        self.created_time = created_time
        self.updated_time = updated_time
        self.changed = False  # Flag to track changes

    def update_status(self, snapshot_time):
        file_path = os.path.join(self.folder_path, self.filename)
        modified_since_snapshot = (
            os.path.getmtime(file_path) > snapshot_time.timestamp() or
            os.path.getctime(file_path) > snapshot_time.timestamp()
        )
        self.changed = modified_since_snapshot

    def display_info(self):
        print(f"File: {self.filename}")
        print(f"Extension: {self.extension}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")
