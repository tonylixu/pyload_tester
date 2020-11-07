import argparse
import LoadTester
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np


def create_load_tester(url, concurrent, times):
    return LoadTester.LoadTester(url, concurrent, times)


def calculate_95_percentile(response_lists):
    """Calculate 95 percentile time"""
    time_list = []
    for r_list in response_lists:
        for r in r_list:
            time_list.append(r.response_time)
    return np.percentile(time_list, 95)


def calculate_average(response_lists):
    """Calculate average time"""
    time_list = []
    for r_list in response_lists:
        for r in r_list:
            time_list.append(r.response_time)
    return np.average(time_list)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description='Process tester argument')
    parser.add_argument('-u', dest='url', required=True, help='Test url')
    parser.add_argument('-c', dest='concurrent', type=int, required=True, help='Concurrent number')
    parser.add_argument('-t', dest='times', type=int, required=True, help='Total tests')
    return parser.parse_args()


def main():
    # Retrieve command line arguments
    args = parse_command_line_arguments()
    url, concurrent, times = args.url, args.concurrent, args.times

    # Create load tester
    lt = create_load_tester(url, concurrent, times)

    # Start load tests
    response_lists, tasks = [], []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(concurrent):
            tasks.append(executor.submit(lt.test_url))
        for future in as_completed(tasks):
            response_lists.append(future.result())

    # Process test results
    ninty_five_percentile = calculate_95_percentile(response_lists)
    average_time = calculate_average(response_lists)
    print(f'Concurrent {concurrent} visit {url}, total visits {times} times, pressure tests results:\n'
          f'Average response time: {average_time}\n'
          f'95% response time: {ninty_five_percentile}')


if __name__ == "__main__":
    main()
