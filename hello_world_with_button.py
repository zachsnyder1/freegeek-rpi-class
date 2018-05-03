# Print "hello world" to the console when you push
# on pin 17

# We will use the Button class from the gpiozero library
# to control the pins on the Raspberry Pi:
from gpiozero import Button

# Let's initialize a Button object, and connect it to
# pin 17:
btn = Button(17)

# Next, we need to define a function that will execute
# every time we push the button:
def say_hello_world():
    print('hello world')

# Finally, let's introduce our Button object to our
# say_hello_world function:
btn.when_pressed = say_hello_world

# Loop infinitely
while True:
    pass
