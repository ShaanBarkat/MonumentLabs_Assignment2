#Monument Labs - Assignment 2 ~ Shaan Barkat

import subprocess
from collections import defaultdict
import datetime


commands = ['sleep 3', 'ls -1 /', 'find /', 'sleep 4', 'find /usr', 'date', 'sleep 5', 'uptime']

times = defaultdict(list)

for cmd in commands:
    for i in range(1,10):
    #Used to find an accurate average time.
        #Check the running time - gives initial state.
        start_time = datetime.datetime.now()
        x = subprocess.Popen(cmd)
        end_time = datetime.datetime.now()
        #Gives end state, through 10 runs to justify average, min, and max.

        #Wait till the process terminates.
        while x.poll() is None:
            time.sleep(0.5)
        
        runtime = end_time - start_time
        cmd_times[cmd].append(runtime)

        

for cmd in commands:
    print(min(cmd_times[cmd]))#Min execution time.
    print(max(cmd_times[cmd]))#Max execution time.
    print((sum(cmd_times[cmd]))/(len(cmd_times[cmd])))#Average execution time.
