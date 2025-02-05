import numpy as np
from adafruit_rplidar import RPLidar

# SETUP
PORT_NAME = "/dev/ttyUSB0"
lidar = RPLidar(None, PORT_NAME, timeout=3)

# LOOP
for raw_scan in lidar.iter_scans():
    scan_data = np.zeros(360)  # refresh data storage
    for _, angle, distance in raw_scan:
        scan_data[min([359, int(angle)])] = distance
    print(scan_data[:15], scan_data[345:])
    ns_l = np.nonzero(scan_data[345:])[0].size
    ns_r = np.nonzero(scan_data[:15])[0].size
    print(ns_l, ns_r)
    if ns_l - ns_r > 4:
        print("lean right")
    elif ns_l - ns_r < -4:
        print("lean left")
    else:
        print("keep")

lidar.stop()
lidar.disconnect()
