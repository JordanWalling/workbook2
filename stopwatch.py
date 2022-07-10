import time

def print_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Time spent: {}h: {}m: {}s'.format(hours, mins, seconds))

    
input('To start the Stopwatch, please press "Enter/Return": ')
start_time = time.time()

print('Time is running....')

input('To stop the Stopwatch, please press "Enter/Return": ')
stop_time = time.time()

    

print_time(stop_time - start_time)