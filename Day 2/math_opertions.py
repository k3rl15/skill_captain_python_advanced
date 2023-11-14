class MathOperations:
    def __init__(self):
        """
        Initialize the constants used in math operations.
        """
        self.zero = 0
        self.half = 0.5
        self.one = 1
        self.two = 2

    @staticmethod
    def add(num1, num2):
        """
        Add two numbers.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the addition.
        """
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        """
        Subtract the second number from the first number.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the subtraction.
        """
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        """
        Multiply two numbers.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the multiplication.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divide the second number by the first number.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the division or an error message if division is by zero.
        """
        if num2 == self.zero:
            return "Cannot divide by zero."
        return num1 / num2

    @staticmethod
    def power(num1, num2):
        """
        Raise the first number to the power of the second number.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the exponentiation.
        """
        return num1 ** num2

    def mixed_number(self, num1, num2):
        """
        Convert the division of two numbers into a mixed number.

        :param num1: The first number.
        :param num2: The second number.
        :return: The mixed number representation or an error if division is by zero.
        """
        if num2 == self.zero:
            return "Cannot divide by zero."
        whole_number = num1 // num2
        remainder = num1 % num2
        if remainder != self.zero:
            result = f"{whole_number} {remainder}/{num2}"
        else:
            result = str(whole_number)
        return result

    def square_root(self, num):
        """
        Calculate the square root of a number.

        :param num: The number for which to calculate the square root.
        :return: The square root of the number.
        """
        return num ** self.half

    def factorial(self, num):
        """
        Calculate the factorial of a number.

        :param num: The number for which to calculate the factorial.
        :return: The factorial of the number or an error message if the number is negative.
        """
        if num < self.zero:
            return "Factorial undefined for negative numbers."
        elif num == self.zero or num == self.one:
            return self.one
        else:
            result = self.one
            for i in range(self.two, num + self.one):
                result *= i
            return result
