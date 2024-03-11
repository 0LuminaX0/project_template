from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin, write_to_file_pandas


def main():
    console_text = input_from_console()
    output_to_console("You entered: " + console_text)

    try:
        builtin_text = read_from_file_builtin('Titanic-Dataset.csv')
        output_to_console("\nContent of Titanic-Dataset.csv read using built-in functions:")
        output_to_console(builtin_text[:300] + "\n")
        write_to_file_builtin(builtin_text, 'Builtin_Titanic-Dataset.csv')
        output_to_console("Content written to Builtin_Titanic-Dataset.csv using built-in functions.")
    except Exception as e:
        output_to_console("An error occurred with built-in file functions: " + str(e))

    try:
        pandas_data = read_from_file_pandas('Titanic-Dataset.csv')
        output_to_console("Content of Titanic-Dataset.csv read using pandas:")
        output_to_console(pandas_data.head().to_string())
        write_to_file_pandas(pandas_data.head(), 'Pandas_Titanic-Dataset.csv')
        output_to_console("Content written to Pandas_Titanic-Dataset.csv using pandas.")
    except Exception as e:
        output_to_console("An error occurred with pandas file functions: " + str(e))


if __name__ == "__main__":
    main()
