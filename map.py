from djitellopy import Tello


import time
if __name__ == "__main__":
    height = [[0,0],
              [0,0]]
    tello = Tello()
    tello.connect()

    #start position is (0,-1)
    tello.enable_mission_pads()

    #takeoff
    print("before_takeoff")
    print(tello.get_height())

    tello.takeoff()
    time.sleep(5)
    print("after takeoff")
    print(tello.get_height())

    tello.move_up(50)

    time.sleep(5)

    print("after move up")
    print(tello.get_height())

    #move to (0,0)
    tello.move_forward(50)

    time.sleep(5)
    print("after move forward")
    height[0][0] = tello.get_height()
    print(height[0][0])

    #move to (1,0)
    tello.move_right(50)

    time.sleep(5)


    print("after move right")
    height[1][0] = tello.get_height()
    print(height[1][0])


    #move to (1,1)

    tello.move_forward(50)

    time.sleep(5)


    print("after move forward")
    height[1][1] = tello.get_height()
    print(height[1][1])


    #move to (0,1)

    tello.move_left(50)

    time.sleep(5)

    print("after move left")
    height[0][1] = tello.get_height()



    tello.rotate_clockwise(180)
    tello.move_forward(100)
    #Original orientation
    tello.rotate_clockwise(180)
    tello.land()