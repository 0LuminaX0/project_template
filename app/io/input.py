import pandas as pd


def input_from_console():

    return input("Please enter text: ")


def read_from_file_builtin(filename):

    with open(filename, 'r') as file:
        return file.read()


def read_from_file_pandas(filename):

    return pd.read_csv(filename)
