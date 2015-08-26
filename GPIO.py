import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
#22 - nothing
#10 - in7
#2  - in6
#pinList = [17, 27, 22, 10, 9]
pinList = [9, 27, 22, 10, 17, 2, 4, 3]

class open_garage:
    
    def __init__(self):

        # loop through pins and set mode and state to 'low'
        for i in pinList: 
            GPIO.setup(i, GPIO.OUT) 
            GPIO.output(i, GPIO.HIGH)

        # time to sleep between operations in the main loop

        SleepTimeL = 0.1

        # main loop
        #"""
        try:
                GPIO.output(9, GPIO.LOW)
                print "This is port", 9
                time.sleep(SleepTimeL)
                GPIO.output(9, GPIO.HIGH)

        # End program cleanly with keyboard
        except KeyboardInterrupt:
          print "  Quit"

          # Reset GPIO settings
          GPIO.cleanup()

