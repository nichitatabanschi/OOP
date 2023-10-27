import os
from datetime import datetime
from document import Document
from text_document import TextDocument
from image_document import ImageDocument
from python_script_document import PythonScriptDocument

class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.documents = {}

    def commit(self):
        self.snapshot_time = datetime.now()
        self.documents = self._get_documents_info()

    def _get_documents_info(self):
        documents = {}
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            if os.path.isfile(file_path):
                file_stat = os.stat(file_path)
                created_time = datetime.fromtimestamp(file_stat.st_ctime)
                updated_time = datetime.fromtimestamp(file_stat.st_mtime)
                _, file_extension = os.path.splitext(file_name)

                if file_extension.lower() == '.txt':
                    document = TextDocument(self.folder_path, file_name, file_extension, created_time, updated_time)
                elif file_extension.lower() in {'.png', '.jpg'}:
                    document = ImageDocument(self.folder_path, file_name, file_extension, created_time, updated_time)
                elif file_extension.lower() == '.py':
                    document = PythonScriptDocument(self.folder_path, file_name, file_extension, created_time, updated_time)
                else:
                    document = Document(self.folder_path, file_name, file_extension, created_time, updated_time)

                documents[file_name] = document

        return documents

    def info(self, filename):
        if filename in self.documents:
            document = self.documents[filename]
            document.display_info()
        else:
            print(f"File '{filename}' not found.")

    def status(self):
        if not self.snapshot_time:
            print("Snapshot not performed. Please use 'commit' to perform a snapshot.")
            return

        print(f"Snapshot Time: {self.snapshot_time}")

        for filename, document in self.documents.items():
            document.update_status(self.snapshot_time)
            if document.changed:
                print(f"{filename} has changed since the snapshot time.")
            else:
                print(f"{filename} has experienced no change since the snapshot time.")
