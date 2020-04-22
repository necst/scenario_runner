import os.path
import subprocess
import time

run = True

while True:
    time.sleep(10)
    if os.path.isfile("close.txt"):
        run = True
        os.remove("close.txt")
        print("close.txt removed!")
    if run:
        run = False
        print("Should launch scenario_runner.py ...")
        subprocess.Popen(['python', 'scenario_runner.py', '--host',
                          'dwarf7.local.necst.it', '--scenario', 'VehicleTurningRight_1',
                          '--reloadWorld'])
        print("scenario_runner.py launched!")
    #print(time.time())
