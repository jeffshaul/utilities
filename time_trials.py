import timeit


def average_execution_time(function, args):
    """Measures the average execution time of a function by performing five time trials.
    
    Args:
        args (tuple): the arguments to be passed into the function.  If no arguments, use ().
                      If only one argument, use (arg1,).
                      If more than two arguments, use (arg1, arg2, ...)
                      
    Returns:
        the average execution time in seconds (it'll probably look like scientific notation)
    """
    
    results = 0
    for i in range(5):
        start = timeit.default_timer()
        function(*args) # Unpack arguments to be passed into the function
        end = timeit.default_timer()
        results += end - start
    return results / 5


def compare_execution_times(function1, args1, function2, args2):
    """Compares the average execution times of two functions!"""
    
    function1_time = average_execution_time(function1, args1)
    function2_time = average_execution_time(function2, args2)
    time_diff = str(round(abs(function2_time - function1_time), 10))
    if function2_time > function1_time:
        factor = str(round(function2_time / function1_time, 3))
        print(function1.__name__ + " wins!  Time difference: " + time_diff + " seconds, factor of " + factor)
    else:
        factor = str(round(function1_time / function2_time, 3))
        print(function2.__name__ + " wins!  Time difference: " + time_diff + " seconds, factor of " + factor)