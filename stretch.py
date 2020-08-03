import time
import os
import sys
import datetime

total_breaks = 48 # 12 hours, break every 15 min
break_count = 0 # total 
break_length = 20 # seconds

# progress bar for break
def cli_progress(break_length, bar_length=20):
    for i in range(0, break_length):
        percent = float(i) / break_length
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        sys.stdout.write('\rPercent: [{0}] {1}% - Break length: {2} seconds.'.format(hashes + spaces, int(round(percent * 100)), break_length))
        sys.stdout.flush()

# clear terminal after break
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# beep for break
def beep():
    print('\a')

while (break_count < total_breaks):
    time.sleep(900) # 15 min
    
    # notification
    for i in range(3):
        beep()

    break_time = datetime.datetime.now().strftime('%a, %b %d %Y  %I:%M:%S %p')
    print("""
    ==========================================================================================
    ______                _      _____ _                
    | ___ \              | |    |_   _(_)               
    | |_/ /_ __ ___  __ _| | __   | |  _ _ __ ___   ___ 
    | ___ \ '__/ _ \/ _` | |/ /   | | | | '_ ` _ \ / _ \\
    | |_/ / | |  __/ (_| |   <    | | | | | | | | |  __/
    \____/|_|  \___|\__,_|_|\_\   \_/ |_|_| |_| |_|\___|
                                                    
    ==========================================================================================
    """)
    print("""
        Time: %s
        Break #: %d                                  
    """ % (break_time, break_count))

    # break progress bar
    for iteration in range(break_length):
        time.sleep(1)
        cli_progress(iteration)

    # clear terminal
    clear()
    break_count += 1
