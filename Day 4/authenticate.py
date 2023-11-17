class Authenticate:
    def __init__(self, func):
        """
        A decorator class for authentication before accessing a function.

        Args:
            func (callable): The function to be decorated.
        """
        self.func = func
        self.authorized_users = ['qrious', 'cker', 'kahtzs']

    def check_authorization(self, name):
        """
        Check if the given username is in the list of authorized users.

        Args:
            name (str): The username to check.

        Returns:
            bool: True if authorized, False otherwise.
        """
        return name in self.authorized_users

    def __call__(self, *args, **kwargs):
        """
        Call method that checks authorization before executing the decorated function.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.

        Returns:
            Any: Result of the decorated function if authorized.
        """
        user = input("Enter your username to decrypt the message: ")
        if self.check_authorization(user):
            result = self.func(user, *args, **kwargs)
            return result
        else:
            print(f"Error: The username {user.capitalize()} is not authorized to view the decrypted message.")


def main():
    """
    Main function to demonstrate the usage of the Authenticate decorator.
    """
    cipher_text = ("Ovwpun fvb ohk h ohwwf, wyvzwlyvbz huk qvfmbs Kpdhsp dpao fvby myplukz \nhuk mhtpsf hszv"
                   " lclu aovbno pa'z zapss lhysf, Ohwwf Ovspkhfz!")
    cipher_shift = 7
    print(f"Encrypted Message:\n{cipher_text}\n")
    decrypt_message(cipher_text, cipher_shift)


@Authenticate
def decrypt_message(username, encrypted_text, shift):
    """
    Decrypt the given encrypted text using the Caesar cipher.

    Args:
        username (str): The username attempting to decrypt the message.
        encrypted_text (str): The text to be decrypted.
        shift (int): The shift value for the Caesar cipher.

    Returns:
        None
    """
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Decrypt uppercase letters
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            # Decrypt lowercase letters
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    print(f"\nDecrypted Message for {username.capitalize()}:\n{decrypted_text}")


if __name__ == "__main__":
    main()
