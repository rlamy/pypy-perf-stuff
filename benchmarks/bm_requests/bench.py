import pyperf
import time

import requests


def time_func(loops):
    start = time.perf_counter()
    for _ in range(loops):
        requests.get("http://localhost:8000/").text
    return time.perf_counter() - start


def main():
    runner = pyperf.Runner()
    runner.bench_time_func('requests.get', time_func)

if __name__ == '__main__':
    main()
