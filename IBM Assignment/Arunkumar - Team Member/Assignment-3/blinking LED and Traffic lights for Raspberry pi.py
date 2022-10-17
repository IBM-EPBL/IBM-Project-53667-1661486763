PYTHON CODE FOR BLINKING LED FOR RASPBERRY PI:
Import RPi.GPIO as GPIO
## Import GPIO library
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
## Use board pin numbering
## Setup GPIO Pin 11 to OUT
While True:
GPIO.output(11,True) ## Turn on Led
Time.sleep(1)
## Wait for one second
GPIO.output(11,False) ## Turn off Led
Time.sleep(1)
## Wait for one second
PYTHON CODE FOR TRAFFIC LIGHTS FOR RASPBERRY PI:
from gpiozero import Button, TrafficLights, Buzzer
From time import sleep
Buzzer = Buzzer(15)
Button = Button(21)
Lights = TrafficLights(25, 8, 7)
While True:
Button.wait_for_press()
Buzzer.on()
Light.green.on()
Sleep(1)
Lights.amber.on()
Sleep(1)
Lights.red.on()
Sleep(1)
Lights.off()
Buzzer.off()
