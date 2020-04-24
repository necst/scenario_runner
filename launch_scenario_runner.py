import os.path
import subprocess
import time

#run = True
#num_of_reps = 2
#n = 0
#ego_target_speeds = [8.34, 19.45]
scenarios = ["VehicleTurningLeft_3"]

for scenario in scenarios:
    run = True
    num_of_reps = 1
    n = 0
    ego_target_speeds = [15]
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
                                  '--egoTargetSpeed', str(ego_target_speeds[n]),
                                  '--scenario', scenario,
                                  '--reloadWorld'])

                print("scenario_runner.py launched! Rep #"+str(n))
    print("All reps done!")
    time.sleep(5)
