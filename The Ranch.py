
import time
import grovepi

# Connect the Sound Sensor to analog port A0
soundsensor = 0

# Connect the LED to digital port D5
#led = 5

#grovepi.pinMode(led,"OUTPUT")
#time.sleep(1)
#i = 0

while True:
    try:
        # Read volume from soundsensor
        i = grovepi.analogRead(soundsensor)
        print(i)

        # Send PWM signal to LED
##        grovepi.analogWrite(led,i//4)

    except IOError:
        print("Error")