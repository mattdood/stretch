import time
import os
import sys
import datetime

total_breaks = 48 # 12 hours, break every 15 min
break_count = 0 # total 
break_length = 20 # seconds

# progress bar for break
def cli_progress(break_length, bar_length=40):
    for i in range(break_length):
        percent = float(i) / break_length
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        sys.stdout.write('\rPercent: [{0}] {1}% - Break timer: {2} seconds.'.format(hashes + spaces, int(round(percent * 100)), i))
        sys.stdout.flush()
        time.sleep(1)

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
    time.sleep(10) # 15 min
    
    # notification
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
    cli_progress(break_length)

    # clear terminal
    clear()
    break_count += 1
