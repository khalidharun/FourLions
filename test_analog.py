import time
from grovepi import *

analog_inputs = [0, 1 , 2]
digital_inputs  = [2,3,4]

print("WELCOME TO TEST APP")
print(version())

outputs = {
    'digital': {
        7: False,
        8: False
    }
}

inputs = {
    'analog': [0, 1, 2],
    'digital': [2, 3, 4]
}

# Setup
for port in inputs['digital']:
    pinMode(port, "INPUT")

for port in outputs['digital']:
    pinMode(port, "OUTPUT")
    digitalWrite(port, False)
    
count = 0
while True:
    count = (count + 1) % 4
    # Read Analog inputs
    analog_values = {port: analogRead(port) for port in inputs['analog']}
    
    # Read Digital inputs
    digital_values = {port: digitalRead(port) for port in inputs['digital']}
        
    # Set Digital outputs
    outputs['digital'] = {
        7: (count % 2) == 0,
        8: (count < 2) == 0
    }
    
    for pin, value in outputs['digital'].items():
        digitalWrite(pin, value)
    
    print("Count: %d" % count)
    print(" inputs['analog' ]: %s" % analog_values)
    print(" inputs['digital']: %s" % digital_values)
    print("outputs['digital']: %s" % outputs['digital'])
    time.sleep(1)
