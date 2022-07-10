import time

def print_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Time spent: {}h: {}m: {}s'.format(hours, mins, seconds))

input('Press Enter/Return key to start stopwatch: ')
start_time = time.time()

print('Time is running....')

input('Press Enter/Return key to stop the stopwatch: ')
stop_time = time.time()

print_time(stop_time - start_time)