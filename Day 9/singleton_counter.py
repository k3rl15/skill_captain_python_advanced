import logging
from time import sleep


class Counter:
    """Singleton class for counting instances."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create a new instance only if it doesn't exist."""
        try:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
                cls._instance._counter = 0
            return cls._instance
        except Exception as e:
            logging.error(f"Error occurred during instance creation: {str(e).capitalize()}.")

    def count(self):
        """Increment the counter and log the current count."""
        self._counter += 1
        logging.info(f"Counter incremented to {self._counter}.")
        sleep(.1)
        return self._counter

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of Counter, creating it if necessary."""
        sleep(.2)
        if cls._instance is None:
            logging.info("Creating a new instance of Counter.")
            cls._instance = Counter()
        return cls._instance


def logging_config():
    """Configure logging for the program."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler()]
    )


def main():
    """Main function for testing singleton counter."""
    logging_config()
    logging.debug("Starting program.")

    counter = Counter.get_instance()

    for _ in range(3, 0, -1):
        print(counter.count())

    print(counter.count())

    sleep(.1)
    logging.debug("Closing program.")


if __name__ == "__main__":
    main()
