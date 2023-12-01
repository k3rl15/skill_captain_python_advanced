import logging
from time import sleep


def main():
    """Main function to execute the logging program."""
    configure_logging()
    logging.debug("Starting the Program.")
    sleep(0.1)
    try:
        # Prompt user for log level and message.
        level_name = get_logging_level()
        log_message = get_log_message()

        # Log the message using the logging module.
        logging.log(getattr(logging, level_name), log_message)
    except Exception as e:
        # Handle and unexpected exceptions.
        logging.error(f"{e}")
    finally:
        sleep(0.1)
        logging.debug("Closing the Program.")


def configure_logging():
    """Configure the logging module."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler()]
    )


def get_logging_level():
    """Prompt the user for logging level name.

    Returns:
        str: The logging level name user entered."""
    log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    while True:
        level_name = input(f"Enter logging level name {log_levels}: ").upper()
        if level_name in log_levels:
            return level_name
        elif level_name == 'QUIT':
            exit()
        else:
            logging.error("Invalid logging level. Please enter a valid logging level. Enter quit to exit the program.")
        sleep(0.1)


def get_log_message():
    """Prompt the user for the log message.

    Returns:
        str: The log message user entered."""
    log_message = input("Enter the log message: ")
    return log_message


if __name__ == "__main__":
    main()
