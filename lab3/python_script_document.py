from document import Document
import os

class PythonScriptDocument(Document):
    def __init__(self, folder_path, filename, extension, created_time, updated_time):
        super().__init__(folder_path, filename, extension, created_time, updated_time)
        self.class_count = None
        self.method_count = None

    def display_info(self):
        super().display_info()
        print("Additional information for Python Script Document")
        self._display_python_script_stats()

    def _display_python_script_stats(self):
        file_path = os.path.join(self.folder_path, self.filename)
        line_count, self.class_count, self.method_count = self._get_python_script_stats(file_path)
        print(f"Line Count: {line_count}")
        print(f"Class Count: {self.class_count}")
        print(f"Method Count: {self.method_count}")

    def _get_python_script_stats(self, file_path):
        line_count = 0
        class_count = 0
        method_count = 0

        try:
            with open(file_path, 'r') as file:
                inside_class = False
                for line in file:
                    line_count += 1
                    line = line.strip()
                    if line.startswith("class "):
                        class_count += 1
                        inside_class = True
                    elif inside_class and line.startswith("def "):
                        method_count += 1
                return line_count, class_count, method_count
        except Exception as e:
            print(f"Error reading Python script statistics: {e}")
            return 0, 0, 0
