import numpy as np
from adafruit_rplidar import RPLidar

# Setup the RPLidar
PORT_NAME = "/dev/ttyUSB0"
lidar = RPLidar(None, PORT_NAME, timeout=3)
scan_arr = np.zeros(360)


def process_scan(raw_scan):
    for _, angle, distance in raw_scan:
        scan_arr[int(angle)] = distance
    return scan_arr


try:
    for scan in lidar.iter_scans():
        scan_data = process_scan(scan)
        print(scan_data[180])
except KeyboardInterrupt:
    print("Stopping.")
finally:
    lidar.stop()
    lidar.disconnect()
