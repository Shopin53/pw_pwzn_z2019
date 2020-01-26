from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    def wrapper(*args, **kwargs):
        set = ", ".join(kwargs.keys()) if kwargs else '-'
        line = f"""
            {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}| function {fun.__name__} called with:
            \n
            {len(args)} postional parameters
            \n
            optional parameters: {set}
            """
        print(line)
        tim = -time()
        diference = fun(*args, **kwargs)
        tim += time()
        line = f"returned: {diference} ({tim:.3}s)"
        print(line)
        return diference
    return wrapper


@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 postional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 postional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
