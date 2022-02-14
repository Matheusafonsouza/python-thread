from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def delay(seconds: int) -> str:
    """
    Delay time, stoping code process for a given number of seconds.
    :param seconds: Number of seconds to delay the application
    """
    time.sleep(seconds)
    return f"{seconds} done..."


if __name__ == "__main__":
    start = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(delay, seconds)
        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")
