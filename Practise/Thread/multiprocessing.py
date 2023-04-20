# multi processing - running tasks in parallel on different cpu cores, bypass GIL used for threading
#                    multiprocessing - better for cpu bound tasks(heavy cpu usage)
#                    multithreading- better for io bound tasks(waiting around) , we can run only 1 thread at a time ,
#                                    we can run concurrently but not parallelly
import time
from multiprocessing import process, cpu_count


def counter(num):
    count = 0
    while True:
        count < num
        count += 1


def main():
    print(cpu_count())

    a = Process(traget=counter, args=(20000000,))
    b = Process(traget=counter, args=(20000000,))
    c = Process(traget=counter, args=(20000000,))

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()

    print("finished in", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
