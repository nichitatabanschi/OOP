from document import Document
import os

class ImageDocument(Document):
    def __init__(self, folder_path, filename, extension, created_time, updated_time):
        super().__init__(folder_path, filename, extension, created_time, updated_time)
        self.width = None
        self.height = None

    def display_info(self):
        super().display_info()
        print("Additional information for Image Document")
        self._display_image_file_stats()

    def _display_image_file_stats(self):
        file_path = os.path.join(self.folder_path, self.filename)
        try:
            size_bytes = os.path.getsize(file_path)
            print(f"Image Size: {size_bytes} bytes")

            # Extract image dimensions without using any third-party library
            with open(file_path, 'rb') as f:
                f.seek(16)  # Skip to the start of the dimensions
                width = int.from_bytes(f.read(4), byteorder='big')
                height = int.from_bytes(f.read(4), byteorder='big')

            self.width, self.height = width, height
            print(f"Image Width: {width} pixels")
            print(f"Image Height: {height} pixels")

        except Exception as e:
            print(f"Error reading image information: {e}")
