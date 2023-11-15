def main():
    """
    The main function of the script.

    It calls iterate_over_file function with a specified file name ('its_me.txt') or prints an error message.

    Returns:
        None
    """
    file_name = 'its_me.txt'
    try:
        iterate_over_file(file_name)
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")


def iterate_over_file(file_path):
    """
    Iterates over the lines of a file and prints each line.

    Args:
        file_path (str): The path to the file to be iterated.

    Returns:
        None
    """
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Create an iterator for the file
        file_iterator = iter(file)

        try:
            # Use the next function to iterate over the file
            while True:
                # Get the next line from the iterator
                line = next(file_iterator)

                # Print the line
                print(line, end='')  # Use end='' to avoid adding extra newline (as lines already contain newline)

        except StopIteration:
            # StopIteration exception will be raised when the iterator is exhausted
            pass


if __name__ == "__main__":
    main()
