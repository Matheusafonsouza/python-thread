from threading import Thread
import time


def delay(seconds: int) -> None:
    """
    Delay time, stoping code process for a given number of seconds.
    :param seconds: Number of seconds to delay the application
    """
    time.sleep(seconds)


if __name__ == "__main__":
    start = time.perf_counter()

    threads = list()
    for _ in range(10):
        t = Thread(target=delay, args=[2])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")
