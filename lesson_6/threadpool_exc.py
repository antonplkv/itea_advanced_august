from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def io_bound(arg1):
    # print(f'i am {arg1}')
    time.sleep(2)
    # print(f'{arg1} woken uo')
    return arg1


with ThreadPoolExecutor(max_workers=10) as exc:

    futures = []
    for i in range(10):
        futures.append(exc.submit(io_bound, i))

    for i in futures:
        print(i.result())


    # for result in as_completed(futures):
    #     print(result.result())