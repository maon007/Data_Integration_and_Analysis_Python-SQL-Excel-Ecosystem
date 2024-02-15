# helpers.py

def clean_cols(column_name):
    """
    Cleanses a column name by removing additional information.

    Parameters:
    column_name (str): The original column name.

    Returns:
    str: The cleansed column name.
    """
    # Split the column name by '['
    parts = column_name.split('[')
    # Return the first part before '['
    return parts[0].strip()
