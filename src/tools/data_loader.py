import csv
import random

class CSVLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_rows(self, num_rows, randomize=False, encoding='utf-8'):
        """
        Load a specified number of rows from the CSV file.

        Args:
        - num_rows: The number of rows to load.
        - randomize: Whether to randomize the rows (default: False).
        - encoding: The encoding of the CSV file (default: 'utf-8').

        Returns:
        - A list of rows, where each row is a list of values.
        """
        rows = []
        with open(self.file_path, 'r', encoding=encoding) as file:
            csv_reader = csv.reader(file)
            all_rows = list(csv_reader)  # Read all rows into memory
            if randomize:
                random.shuffle(all_rows)     # Shuffle the rows if randomize is True
            rows = all_rows[:num_rows]   # Select the specified number of rows
        return rows
