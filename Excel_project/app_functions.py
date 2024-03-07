import pandas as pd
import openpyxl

def merge_excel_sheets(file_path, sheet1_name, sheet2_name):
    """Loads data from two Excel sheets, merges them based on the specified join column,
    and returns the merged DataFrame.

    Args:
        file_path (str): Path to the Excel file.
        sheet1_name (str): Name of the first sheet.
        sheet2_name (str): Name of the second sheet.
        join_column (str): Name of the common column used for merging.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """

    try:
        # Read dataframes from sheets using try-except to handle potential errors
        df1 = pd.read_excel(file_path, sheet_name=sheet1_name)
        df2 = pd.read_excel(file_path, sheet_name=sheet2_name)

        # Merge DataFrames using outer join (default behavior) or other join types
        merged_data = pd.merge(df1, df2, on=['Credit Control Area', 'Company code'], how='inner')
        
        return merged_data

    except (FileNotFoundError, pd.errors.ParserError, ValueError) as e:
        print(f"Error during merging: {e}")
        return None


def create_blocked_pivot_table(excel_file, sheet_name):
    """
    Create a pivot table from an Excel file with counts and ratios of blocked and not blocked customers.

    Parameters:
    - excel_file (str): Path to the Excel file.
    - sheet_name (str): Name of the sheet in the Excel file containing the data.

    Returns:
    - pandas.DataFrame: Pivot table with counts and ratios of blocked and not blocked customers.
    """
    
    # Read Excel file
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # Filter out the specific column
    indicator_column = df["Indicator: Blocked b"]
    
    # Count the number of blocked and not blocked customers
    blocked_count = indicator_column.value_counts().get("Blocked", 0)
    not_blocked_count = indicator_column.value_counts().get("Not Blocked", 0)
    
    # Calculate the ratio
    total_customers = blocked_count + not_blocked_count
    blocked_ratio = (blocked_count / total_customers * 100) if total_customers > 0 else 0
    not_blocked_ratio = (not_blocked_count / total_customers * 100) if total_customers > 0 else 0
    
    # Create a DataFrame for the pivot table
    pivot_data = {
        "Blocked": [blocked_count, blocked_ratio],
        "Not Blocked": [not_blocked_count, not_blocked_ratio]
    }
    pivot_df = pd.DataFrame(pivot_data, index=["Count", "Ratio"])
    
    return pivot_df.transpose()


def create_GFS_and_company_pivot_table(excel_file, sheet_name):
    """
    Create a pivot table from an Excel file with counts of occurrences for each combination of GFS entity and Company code.

    Parameters:
    - excel_file (str): Path to the Excel file.
    - sheet_name (str): Name of the sheet in the Excel file containing the data.

    Returns:
    - pandas.DataFrame: Pivot table with counts of occurrences for each combination of GFS entity and Company code.
    """
    
    # Read Excel file
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Create pivot table
    pivot_table = pd.pivot_table(df, index=["GFS entity", "Company code"], aggfunc='size', fill_value=0)

    # Convert Series to DataFrame and set header name
    pivot_table = pivot_table.to_frame("Count")
    
    return pivot_table


def get_unique_values_from_excel(file_path, sheet_name, column_name):
    """
    This function takes an Excel file path, sheet name, and column name,
    and returns the unique values in that column ordered alphabetically.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to analyze.
        column_name (str): Name of the column to analyze.

    Returns:
        pandas.DataFrame: A DataFrame containing unique values in the specified column, ordered alphabetically.
    """

    try:
        # Read data from the specified Excel sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Get unique values from the column and sort alphabetically
        unique_values = df[column_name].unique()
        unique_values_df = pd.DataFrame(unique_values, columns=[column_name])
          
        return unique_values_df.sort_values(by=[column_name], ignore_index=True)

    except (FileNotFoundError, pd.errors.ParserError) as e:
        print(f"Error during analysis: {e}")
        return None