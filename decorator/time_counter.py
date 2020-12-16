from time import time


def time_counter(decorated_function):
    def measure_time(*args, **kwargs):
        start_time = time()
        returned_data = decorated_function(*args, **kwargs)
        stop_time = time()
        elapsed_time = stop_time - start_time
        print('Ta funkcja zajela {} sekund'.format(elapsed_time))
        return returned_data

    return measure_time
