class TextFileWriter:
    def __init__(self, file_path, append=False, newline=False, encoding='utf-8'):
        """
        Initialize the TextFileWriter.

        Args:
        - file_path: The path to the text file.
        - append: Whether to append to the file instead of overwriting (default: False).
        - newline: Whether to append a newline after each write operation (default: False).
        - encoding: The encoding to use when writing to the file (default: 'utf-8').
        """
        self.file_path = file_path
        self.mode = 'a' if append else 'w'
        self.newline = newline
        self.encoding = encoding

    def __call__(self, text):
        """
        Save a string to the text file.

        Args:
        - text: The string to save.
        """
        with open(self.file_path, self.mode, encoding=self.encoding) as file:
            file.write(text)
            if self.newline:
                file.write('\n')
