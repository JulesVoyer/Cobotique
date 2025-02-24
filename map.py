from djitellopy import Tello


import time
if __name__ == "__main__":
    tello = Tello()
    tello.connect()
    tello.takeoff()
    tello.move_up(50)
    #start position is (0,0)
    tello.move_forward(30)
    #U-turn
    time.sleep(2)
    tello.rotate_clockwise(180)
    time.sleep(2)
    tello.move_forward(30)
    time.sleep(2)
    #Original orientation
    tello.rotate_clockwise(180)
    tello.land()