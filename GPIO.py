import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinList = [11, 12, 13, 15, 16, 19, 21, 23]

class board:
    
    def __init__(self, board_pin):

        # loop through pins and set mode and state to 'low'
        for i in pinList: 
            GPIO.setup(i, GPIO.OUT) 
            GPIO.output(i, GPIO.HIGH)

        # time to sleep between operations in the main loop

        SleepTimeL = 1

        # main loop
        #"""
        try:
                GPIO.output(board_pin , GPIO.LOW)
                print "This is port", board_pin
                time.sleep(SleepTimeL)
                GPIO.output(board_pin, GPIO.HIGH)
                # Reset GPIO settings
                GPIO.cleanup()

        # End program cleanly with keyboard
        except KeyboardInterrupt:
          print "  Quit"

          # Reset GPIO settings
          GPIO.cleanup()

