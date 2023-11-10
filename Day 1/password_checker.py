from re import search
from string import punctuation


class PasswordStrengthChecker:
    def __init__(self, password):
        """
        Initializes the PasswordStrengthChecker object.

        Parameters:
        - password (str): The password to be checked for strength.
        """
        self.password = password

    def check_password_strength(self):
        """
        Checks the strength of the password based on various criteria.

        Returns:
        - str: A message indicating the strength of the password.
        """
        score = 0
        if len(self.password) >= 8:
            # Length score
            score += 2
        if self.uppercase_check():
            # Uppercase letter score
            score += 2
        if self.lowercase_check():
            # Lowercase letter score
            score += 2
        if self.numeric_check():
            # Numeric digit score
            score += 2
        if self.punctuation_check():
            # Punctuation character score
            score += 2

        if score > 8:
            return "Password strength: Your password is strong."
        elif 6 < score <= 8:
            return "Password strength: Your password has medium strength."
        else:
            return "Password strength: Your password is weak."

    def uppercase_check(self):
        """
        Checks if the password contains at least one uppercase letter.

        Returns:
        - bool: True if the password contains at least one uppercase letter, otherwise False.
        """
        return bool(search(r'[A-Z]', self.password))

    def lowercase_check(self):
        """
        Checks if the password contains at least one lowercase letter.

        Returns:
        - bool: True if the password contains at least one lowercase letter, otherwise False.
        """
        return bool(search(r'[a-z]', self.password))

    def numeric_check(self):
        """
        Checks if the password contains at least one numeric digit.

        Returns:
        - bool: True if the password contains at least one numeric digit, otherwise False.
        """
        return bool(search(r'\d', self.password))

    def punctuation_check(self):
        """
        Checks if the password contains at least one punctuation character.

        Returns:
        - bool: True if the password contains at least one punctuation character, otherwise False.
        """
        return bool(search(fr'[{punctuation}]', self.password))


def main():
    user_password = input("Enter a password: ")
    password_checker = PasswordStrengthChecker(user_password)
    strength = password_checker.check_password_strength()
    print(strength)


if __name__ == "__main__":
    main()
