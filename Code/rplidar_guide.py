import numpy as np
from adafruit_rplidar import RPLidar


# Setup the RPLidar
PORT_NAME = "/dev/ttyUSB0"
lidar = RPLidar(None, PORT_NAME, timeout=3)

scan_data = np.ones(360) * np.nan

try:
    #    print(lidar.get_info())
    for raw_scan in lidar.iter_scans():
        scan_data = np.ones(360) * np.nan  # refresh
        for _, angle, distance in raw_scan:
            if distance == 0:
                scan_data[min([359, int(angle)])] = np.nan
            else:
                scan_data[min([359, int(angle)])] = distance
        # print(scan_data[180])
        n0_l = np.argwhere(np.isnan(scan_data[345:])).size
        n0_r = np.argwhere(np.isnan(scan_data[:15])).size
        print(n0_l, n0_r)
        # print(np.nanmin(scan_data[345:]), np.nanmin(scan_data[:15]))
        # if np.nanmin(scan_data[345:]) < 3000 or np.nanmin(scan_data[:15]) < 3000:
        #     n0_l = len(np.where(scan_data[345:] == np.nan)[0])
        #     n0_r = len(np.where(scan_data[:15] == np.nan)[0])
        #     print(n0_l, n0_r)
        if n0_l - n0_r > 3:
            print("lean right")
        elif n0_l - n0_r < -3:
            print("lean left")
        else:
            print("keep")

except KeyboardInterrupt:
    print("Stopping.")
lidar.stop()
lidar.disconnect()
