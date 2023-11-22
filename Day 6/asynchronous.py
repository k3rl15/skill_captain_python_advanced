import asyncio


async def main():
    """
    The main function to initiate the countdown timer.

    This function prompts the user to enter a positive integer as the countdown start value.
    It then calls the countdown_timer function to start the asynchronous countdown.

    Returns:
        None
    """
    countdown = get_positive_integer_input()
    await countdown_timer(countdown)


def get_positive_integer_input():
    """
    Get positive integer input from the user.

    This function repeatedly prompts the user until a valid positive integer is entered.

    Returns:
        int: The positive integer entered by the user.
    """
    while True:
        try:
            user_input = int(input("Enter a number to start the countdown: "))
            if user_input > 0:
                return user_input
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


async def countdown_timer(time):
    """
    Asynchronous countdown timer.

    This function prints the countdown timer value every second until it reaches zero.

    Args:
        time (int): The initial countdown value.

    Returns:
        None
    """
    while time:
        print(f"Timer: {time}")
        await asyncio.sleep(1)
        time -= 1


if __name__ == "__main__":
    asyncio.run(main())
