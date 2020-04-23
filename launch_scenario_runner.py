import os.path
import subprocess
import time

run = True
num_of_reps = 1
n = 0

while n < num_of_reps:
    time.sleep(10)
    if os.path.isfile("close.txt"):
        run = True
        os.remove("close.txt")
        print("close.txt removed!")
        n += 1
    if run:
        run = False
        if n < num_of_reps:
            print("Should launch scenario_runner.py ...")
            subprocess.Popen(['python', 'scenario_runner.py', '--host',
                              'dwarf7.local.necst.it', '--reps', str(n),
                              '--scenario', 'VehicleTurningRight_1',
                              '--reloadWorld'])

            print("scenario_runner.py launched! Rep #"+str(n))
print("All reps done!")
