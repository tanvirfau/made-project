import unittest
import os
import pandas as pd
import sqlite3
from pipeline import main  

class TestDataPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Runs the data pipeline before tests start.
        """
        main()  # Execute the pipeline

    def test_csv_file_exists(self):
        """
        Check if the CSV output file exists.
        """
        output_csv = './data/merged_obesity_socioeconomic_data.csv'
        self.assertTrue(os.path.isfile(output_csv), f"CSV output file does not exist at {output_csv}")

    def test_sqlite_file_exists(self):
        """
        Check if the SQLite database file exists.
        """
        output_db = './data/obesity_socioeconomic.db'
        self.assertTrue(os.path.isfile(output_db), f"SQLite database file does not exist at {output_db}")

    def test_csv_file_content(self):
        """
        Validate the CSV file contains data.
        """
        output_csv = './data/merged_obesity_socioeconomic_data.csv'
        df = pd.read_csv(output_csv)
        self.assertFalse(df.empty, "CSV file is empty")
        self.assertTrue(len(df) > 0, "CSV file has no data rows")
        self.assertIn('Location', df.columns, "CSV file does not contain the 'Location' column")

    def test_sqlite_file_content(self):
        """
        Validate the SQLite database table contains data.
        """
        output_db = './data/obesity_socioeconomic.db'
        conn = sqlite3.connect(output_db)
        query = "SELECT COUNT(*) FROM merged_data"  
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        self.assertTrue(count > 0, "SQLite database table 'merged_data' is empty")

if __name__ == '__main__':
    unittest.main()
