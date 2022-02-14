import time


def delay(seconds: int) -> None:
    """
    Delay time, stoping code process for a given number of seconds.
    :param seconds: Number of seconds to delay the application
    """
    time.sleep(seconds)


def do_something() -> None:
    """ main function """
    delay(seconds=1)


if __name__ == "__main__":
    start = time.perf_counter()
    do_something()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")
