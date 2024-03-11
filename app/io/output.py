import pandas as pd


def output_to_console(text):
    """
    Outputs the given text to the console.

    Args:
        text (str): The text to be printed to the console.
    """
    print(text)


def write_to_file_builtin(text, filename):
    """
    Writes the given text to a file using Python's built-in functionality.

    Args:
        text (str): The text to be written to the file.
        filename (str): The path to the file where the text will be written.

    Raises:
        IOError: If the file could not be opened for writing.
    """
    with open(filename, 'w') as file:
        file.write(text)


def write_to_file_pandas(data, filename):
    """
    Writes the given DataFrame to a CSV file using the pandas library.

    Args:
        data (DataFrame): The pandas DataFrame to be written to the CSV file.
        filename (str): The path to the CSV file where the DataFrame will be written.

    Raises:
        IOError: If the CSV file could not be opened for writing.
    """
    data.to_csv(filename, index=False)
