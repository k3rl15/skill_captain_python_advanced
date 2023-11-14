from math_opertions_script import MathOperations

# Create an instance of the MathOperations class
solve = MathOperations()


def main():
    """
    Main function for the calculator program.
    Handles user input, performs calculations, and displays results.
    """

    result, user_operation = None, None
    operations = ['add', 'subtract', 'multiply', 'divide', 'power', 'fraction', 'sroot', 'factorial']
    print("MATH OPERATIONS")

    # Main program loop
    while True:
        print("\nPossible Operations: ['add', 'subtract', 'multiply', 'divide', 'power', "
              "'fraction' mixed number, 'sroot' square root, 'factorial', 'quit']:")
        user_operation = input("Operation: ").lower()

        # Check if the entered operation is valid
        if user_operation in operations:
            result = user_number_inputs(user_operation)
        elif user_operation == 'quit':
            exit()
        else:
            result = "Invalid input. Please enter one of the possible operations, for example, 'add' or 'quit.'"

        # Display the result to the user
        if isinstance(result, (int, float)):
            # Format the result for display
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 5)
            result_output = f"Calculation Results: {result}"
        else:
            result_output = result

        print(result_output)


def user_number_inputs(operation):
    """
    Get user input for numbers and perform input validation.
    Args:
        operation (str): The mathematical operation to be performed.

    Returns:
        The result of the operation or an error message.
    """
    tries = 0
    num_inputs = []

    # Determine the number of inputs required based on the operation
    if operation == 'sroot' or operation == 'factorial':
        accept_inputs = 1
    else:
        accept_inputs = 2

    # Get user input with input validation
    if operation == 'sroot':
        print("Square Root")
    elif operation == 'fraction':
        print("Mixed Number")
    else:
        print(f"{operation.capitalize()}")
    while tries < 3:
        try:
            for i in range(accept_inputs):
                num_inputs.append(float(input("Num: ")))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
        tries += 1

    # Check if valid numbers were entered
    if num_inputs:
        return perform_operation(operation, *num_inputs)
    else:
        return "Maximum tries reached. Please input a new operation."


def perform_operation(operation, *numbers):
    """
    Perform the specified mathematical operation.

    Args:
        operation (str): The mathematical operation to be performed.
        *numbers: Variable number of numerical arguments.

    Returns:
        The result of the operation or an error message.
    """
    try:
        if operation == 'add':
            return solve.add(*numbers)
        elif operation == 'subtract':
            return solve.subtract(*numbers)
        elif operation == 'multiply':
            return solve.multiply(*numbers)
        elif operation == 'divide':
            return solve.divide(*numbers)
        elif operation == 'power':
            return solve.power(*numbers)
        elif operation == 'fraction':
            return solve.mixed_number(*numbers)
        elif operation == 'sroot':
            return solve.square_root(*numbers)
        elif operation == 'factorial':
            return solve.factorial(*numbers)
    except Exception as e:
        return f"Error: {str(e)}"


# Entry point of the program
if __name__ == "__main__":
    main()
