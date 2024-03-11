import pandas as pd


def input_from_console():
    """
    Prompts the user to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Please enter text: ")


def read_from_file_builtin(filename):
    """
    Reads content from a file using Python's built-in functionality.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file could not be opened.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_from_file_pandas(filename):
    """
    Reads content from a CSV file using the pandas library.

    Args:
        filename (str): The path to the CSV file to be read.

    Returns:
        DataFrame: A pandas DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the CSV file is empty or has invalid content.
    """
    return pd.read_csv(filename)
