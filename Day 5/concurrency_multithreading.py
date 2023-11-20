from threading import Thread
from random import randint
from time import sleep


def main():
    print("Start Fishing Trip.")
    fish_on = randint(1, 10)

    setup_thread = Thread(target=setup_rig)
    cast_thread = Thread(target=cast_line)
    hook_thread = Thread(target=hook_fish, args=(fish_on,))

    setup_thread.start()
    cast_thread.start()
    hook_thread.start()

    setup_thread.join()
    cast_thread.join()
    hook_thread.join()

    if fish_on < 4:
        print("That didn't take long.")
    elif fish_on in range(4, 8):
        print("Good day to fish.")
    else:
        print("Seemed like nothing was going to bite today.")

    print("Fishing Trip complete!")


def setup_rig():
    print("Setup saltwater fishing rig.")


def cast_line():
    print("Cast line and wait...")


def hook_fish(wait):
    sleep(wait)
    print("Set hook  and reel in fish.")


if __name__ == "__main__":
    main()
