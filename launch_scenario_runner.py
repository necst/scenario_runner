import os.path
import subprocess
import time

#run = True
#num_of_reps = 2
#n = 0
#ego_target_speeds = [8.34, 19.45]
#ego_brake_values = [0.3, 0.7]
"""
scenarios = [
            "VehicleTurning_1A",
            "VehicleTurning_1B",
            "VehicleTurning_1C",
            "VehicleTurning_1D",
            "VehicleTurning_1E",
            "VehicleTurning_1F",
            "VehicleTurning_1G",
            "VehicleTurning_1H",
            "VehicleTurning_1I",
            "VehicleTurning_1L",
            "VehicleTurning_2A",
            "VehicleTurning_2B",
            "VehicleTurning_2C",
            "VehicleTurning_2D",
            "VehicleTurning_2E",
            "VehicleTurning_2F",
            "VehicleTurning_2G",
            "VehicleTurning_2H",
            "VehicleTurning_2I",
            "VehicleTurning_2L",
            "VehicleTurning_3A",
            "VehicleTurning_3B",
            "VehicleTurning_3C",
            "VehicleTurning_3D",
            "VehicleTurning_3E",
            "VehicleTurning_3F",
            "VehicleTurning_3G",
            "VehicleTurning_3H",
            "VehicleTurning_3I",
            "VehicleTurning_3L",
            "VehicleTurning_4A",
            "VehicleTurning_4B",
            "VehicleTurning_4C",
            "VehicleTurning_4D",
            "VehicleTurning_4E",
            "VehicleTurning_4F",
            "VehicleTurning_4G",
            "VehicleTurning_4H",
            "VehicleTurning_4I",
            "VehicleTurning_4L",
            "VehicleTurning_5A",
            "VehicleTurning_5B",
            "VehicleTurning_5C",
            "VehicleTurning_5D",
            "VehicleTurning_5E",
            "VehicleTurning_5F",
            "VehicleTurning_5G",
            "VehicleTurning_5H",
            "VehicleTurning_5I",
            "VehicleTurning_5L",
            "VehicleTurning_6A",
            "VehicleTurning_6B",
            "VehicleTurning_6C",
            "VehicleTurning_6D",
            "VehicleTurning_6E",
            "VehicleTurning_6F",
            "VehicleTurning_6G",
            "VehicleTurning_6H",
            "VehicleTurning_6I",
            "VehicleTurning_6L",
            "VehicleTurning_7A",
            "VehicleTurning_7B",
            "VehicleTurning_7C",
            "VehicleTurning_7D",
            "VehicleTurning_7E",
            "VehicleTurning_7F",
            "VehicleTurning_7G",
            "VehicleTurning_7H",
            "VehicleTurning_7I",
            "VehicleTurning_7L",
            "VehicleTurning_10A",
            "VehicleTurning_10B",
            "VehicleTurning_10C",
            "VehicleTurning_10D",
            "VehicleTurning_10E",
            "VehicleTurning_10F",
            "VehicleTurning_10G",
            "VehicleTurning_10H",
            "VehicleTurning_10I",
            "VehicleTurning_10L",
            "VehicleTurning_11A",
            "VehicleTurning_11B",
            "VehicleTurning_11C",
            "VehicleTurning_11D",
            "VehicleTurning_11E",
            "VehicleTurning_11F",
            "VehicleTurning_11G",
            "VehicleTurning_11H",
            "VehicleTurning_11I",
            "VehicleTurning_11L",
            "VehicleTurning_12A",
            "VehicleTurning_12B",
            "VehicleTurning_12C",
            "VehicleTurning_12D",
            "VehicleTurning_12E",
            "VehicleTurning_12F",
            "VehicleTurning_12G",
            "VehicleTurning_12H",
            "VehicleTurning_12I",
            "VehicleTurning_12L",
            "VehicleTurning_13A",
            "VehicleTurning_13B",
            "VehicleTurning_13C",
            "VehicleTurning_13D",
            "VehicleTurning_13E",
            "VehicleTurning_13F",
            "VehicleTurning_13G",
            "VehicleTurning_13H",
            "VehicleTurning_13I",
            "VehicleTurning_13L",
    #"VehicleTurning_8A",
    #"VehicleTurning_9A",
    ]
"""
"""
for scenario in scenarios:
    run = True
    num_of_reps = 2
    n = 0
    ego_brake_values = [0.3, 0.7]
    #ego_brake_values = [0.7]
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
                                  '--egoTargetSpeed', str(19.45),
                                  '--scenario', scenario,
                                  '--brakeValue', str(ego_brake_values[n]),
                                  '--reloadWorld'])

                print("scenario_runner.py launched! Rep #"+str(n))
    print("All reps done!")
    time.sleep(5) 
"""

"""
for scenario in scenarios:
    run = True
    num_of_reps = 2
    n = 0
    ego_target_speeds = [8.3333, 19.4444]
    #ego_target_speeds=[19.4444]
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
"""
