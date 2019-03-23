import time
import grovepi

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 7

grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        # Sense motion, usually human, within the target range
        print(grovepi.digitalRead(pir_sensor))
        if grovepi.digitalRead(pir_sensor):
            print( 'Motion Detected')
        else:
            print( '-')

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.2)

    except IOError:
        print( "Error")