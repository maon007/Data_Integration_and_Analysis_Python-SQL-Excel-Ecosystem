import os
import re
import sys
import logging
import pandas as pd
from datetime import datetime
from helpers import clean_cols


class CSVDataProcessor:
    """
    A class to process CSV data files from a specified folder.
    """
    def __init__(self, folder_path):
        self.folder_path = folder_path


    def extract_date_and_replace_column(self, dataframe, filename):
        """
        Extracts the date from the filename and replaces values in the 'Date' column of the DataFrame.

        Args:
            dataframe (pandas.DataFrame): The DataFrame containing the data.
            filename (str): The name of the file from which the date should be extracted.

        Returns:
            pandas.DataFrame: The DataFrame with the 'Date' column replaced.

        Raises:
            ValueError: If the filename format is invalid or the 'Date' column is missing.
        """

        try:
            # Extract date using a regular expression for flexibility
            file_date_str = re.search(r"_(\d{4}-\d{2}-\d{2})\.", filename).group(1)
            file_date = pd.to_datetime(file_date_str).strftime('%B %d, %Y')  # Format directly

            # Verify 'Date' column existence before replacement
            if 'Date' not in dataframe.columns:
                raise ValueError("DataFrame does not have a 'Date' column.")

            dataframe['Date'] = file_date
            return dataframe

        except AttributeError:
            raise ValueError(f"Invalid filename format: '{filename}'")


    def load_csv_files_to_dataframe(self):
        """
        Loads all CSV files from the specified folder into a single pandas DataFrame,
        replacing values in the 'Date' column with the date from the filename.

        Returns:
        pandas.DataFrame: A DataFrame containing data from all CSV files.

        Raises:
        ValueError: If no CSV files are found in the folder.
        """

        csv_files = [
            os.path.join(self.folder_path, file)
            for file in os.listdir(self.folder_path)
            if file.endswith(".csv")
        ]

        if not csv_files:
            raise ValueError("No CSV files found in the specified folder.")

        combined_data = pd.concat(
            (
                pd.read_csv(file)
                .pipe(self.extract_date_and_replace_column, filename=os.path.basename(file))
                for file in csv_files
            ),
            ignore_index=True,
        )

        return combined_data


    def save_dataframe_to_csv(self):
        """
        Save the combined DataFrame to a CSV file with the name 'user_actions_{today}.csv'.
        """
        # Get today's date
        today = datetime.today().strftime('%Y-%m-%d')

        # Construct the filename
        filename = f"user_actions_{today}.csv"

        # Load data into a DataFrame
        dataframe = self.load_csv_files_to_dataframe()

        # Clean column names using clean_cols from helpers.py
        dataframe.columns = [clean_cols(col) for col in dataframe.columns]

        # Save DataFrame to CSV
        dataframe.to_csv(filename, index=False)

        logging.info("DataFrame saved to: %s", filename)


    def analyze_csv_files(self):
        """
        Analyzes CSV files in the specified folder and prints:
        - Number of CSV files
        - Number of files with data (excluding files with only headers)
        - Total number of rows across all files
        """

        csv_files = [file for file in os.listdir(self.folder_path) if file.endswith(".csv")]
        total_csv_files = len(csv_files)

        files_with_data = 0
        total_rows = 0

        for file_path in (os.path.join(self.folder_path, file) for file in csv_files):
            with open(file_path, 'r') as f:
                # Use next() to skip the header row directly
                next(f)  # Skip header
                num_rows = sum(1 for _ in f)  # Count data rows only

                if num_rows > 0:
                    files_with_data += 1
                    total_rows += num_rows

        logging.info("Number of CSV files: %d", total_csv_files)
        logging.info("Number of files with data: %d", files_with_data)
        logging.info("Total number of rows: %d", total_rows)


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Check for command-line arguments
    if len(sys.argv) != 2:
        logging.error("Usage: python data_processor.py <folder_path>")
        sys.exit(1)

    # Get folder path from command-line argument
    folder_path = sys.argv[1]

    # Create an instance of the CSVDataProcessor class
    data_processor = CSVDataProcessor(folder_path)

    # Call methods of the CSVDataProcessor instance
    data_processor.analyze_csv_files()
    data_processor.save_dataframe_to_csv()
