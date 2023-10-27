from document import Document
import os

class TextDocument(Document):
    def __init__(self, folder_path, filename, extension, created_time, updated_time):
        super().__init__(folder_path, filename, extension, created_time, updated_time)

    def display_info(self):
        super().display_info()
        print("Additional information for Text Document")
        self._display_text_file_stats()

    def _display_text_file_stats(self):
        file_path = os.path.join(self.folder_path, self.filename)
        line_count, word_count, char_count = self._get_text_file_stats(file_path)
        print(f"Line Count: {line_count}")
        print(f"Word Count: {word_count}")
        print(f"Character Count: {char_count}")

    def _get_text_file_stats(self, file_path):
        line_count = 0
        word_count = 0
        char_count = 0

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    words = line.split()
                    line_count += 1
                    word_count += len(words)
                    char_count += sum(len(word) for word in words)

        except Exception as e:
            print(f"Error reading text file stats: {e}")

        return line_count, word_count, char_count

