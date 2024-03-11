import pandas as pd


def output_to_console(text):

    print(text)


def write_to_file_builtin(text, filename):

    with open(filename, 'w') as file:
        file.write(text)


def write_to_file_pandas(data, filename):

    data.to_csv(filename, index=False)
