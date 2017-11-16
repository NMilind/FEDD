# Import Adafruit library
import Adafruit_PCA9685

# Import threading modules
import time

get_time = lambda: int(round(time.time() * 1000))

#Initialize the PCA9685 Board using the default address (0x40)
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
SERVO_MIN = 120
SERVO_MAX = 660
CHANNEL = 0

# Make sure pulses stay in range
def get_pulse(value):
    if value < SERVO_MIN:
        return SERVO_MIN
    elif value > SERVO_MAX:
        return SERVO_MAX
    return value

# Set initial value of the servo
def initialize():
    global current
    current = (SERVO_MAX + SERVO_MIN) / 2.0
    current = int(current)
    pwm.set_pwm(CHANNEL, 0, current)

# Handle input from the webcam
def handle_input(v, dt, move=1E-3):
    global current
    current += move * v * dt
    current = get_pulse(current)
    current = int(current)
    pwm.set_pwm(CHANNEL, 0, current)
