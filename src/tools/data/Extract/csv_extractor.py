import csv
import random

class CsvExtractor:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv_data(self, num_rows, randomize=False, encoding='utf-8'):
        
        """
        Load a specified number of rows from the CSV file.

        Args:
        - num_rows: The number of rows to load.
        - randomize: Whether to randomize the rows (default: False).
        - encoding: The encoding of the CSV file (default: 'utf-8').

        Returns:
        - A list of the rows in the csv file to extract.
        """

        data = self.load_rows(encoding)

        if randomize: random.shuffle(data)

        data = data[:num_rows]

        return data
        

    def load_rows(self, encoding='utf-8'):

        """
        Load rows from the specified CSV file.

        Args:
        - encoding: The encoding of the CSV file (default: 'utf-8').

        Returns:
        - A list of the rows in the csv file.
        """

        with open(self.file_path, 'r', encoding=encoding) as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        return rows

