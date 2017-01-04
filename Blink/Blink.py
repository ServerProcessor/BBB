from bbio import *

# Create a setup function:

def setup():
  # Set the two LEDs as outputs: 
  pinMode(USR2, OUTPUT)
  pinMode(USR3, OUTPUT)

  # Start one high and one low:
  digitalWrite(USR2, HIGH)
  digitalWrite(USR3, LOW)

# Create a main function:
def loop():
  # Toggle the two LEDs and sleep a few seconds:
  toggle(USR2)
  toggle(USR3)
  delay(500)

# Start the loop:
run(setup, loop)
