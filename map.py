from djitellopy import Tello


import time
if __name__ == "__main__":
    height = [0,0]
    tello = Tello()
    tello.connect()

    #start position is (0,0)
    tello.enable_mission_pads()

    #takeoff
    print("before_takeoff")
    print(tello.get_height())

    tello.takeoff()
    time.sleep(5)
    print("after takeoff")
    print(tello.get_height())

    tello.move_up(20)

    time.sleep(5)

    print("after move up")
    print(tello.get_height())


    tello.move_forward(25)
    time.sleep(5)

    print("after move forward 1")
    print(tello.get_height())


    tello.move_forward(25)
    time.sleep(5)

    print("after move forward 2")
    print(tello.get_height())


    tello.flip("b")
    time.sleep(5)

    print("after flip")

    print(tello.get_height())


    tello.rotate_clockwise(180)
    tello.move_forward(50)
    #Original orientation
    tello.rotate_clockwise(180)
    tello.land()