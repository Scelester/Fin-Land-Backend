import RPi.GPIO as gpio
from time import sleep
from time import perf_counter as clock

# importing files
from food_servo import start_servo
from Dphsense import get_ph_value
from relay_me import relay_module

# setting up goio keys
gpio.setmode(gpio.BCM)

# servo motor setup
gpio.setup(14, gpio.OUT) # output signal fo GPIO
food_dispenser_servo = gpio.PWM(14,50)    # setting frequency
servo_initial_duty = 1
food_timer = 5
STATE_SERVO = False


# --------------------------- Clock setup ---------------------------------
initial_timer = clock()


# --------------------------- Relay stuff ------------------------------------
relay_pin = 18
gpio.setup(relay_pin,gpio.OUT)

# --------------------------------- Inputs --------------------------------

# pH sensor setup
gpio.setup(23,gpio.IN)



try:
    while True:
      if STATE_SERVO:
         start_servo(food_dispenser_servo, servo_initial_duty)
      
      # get_ph_value()

      # relay stuff
      relay_module(relay_pin)
      
      if clock() - initial_timer >= 50:
            break

      # delay some time
      sleep(0.5)


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")


# other errors
except:
   print("some error") 


finally:
   print("clean up") 
   gpio.cleanup() # cleanup all GPIO 
