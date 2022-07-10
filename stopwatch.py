def print_start_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Time spent: {}h: {}m: {}s'.format(hours, mins, seconds))

    
    
