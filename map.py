from djitellopy import Tello
import numpy as np

import time
if __name__ == "__main__":
    height = np.zeros(5,5)
    tello = Tello()
    tello.connect()

    tello.takeoff()
    tello.move_up(100)
    sens = 1
    for i in range(5):
        for j in range(5):
            tello.move_forward(100)
            height[i][j] = tello.get_height()
        tello.rotate_clockwise(sens*90)


    tello.land()