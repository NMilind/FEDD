# Import Adafruit library
import Adafruit_PCA9685

# Import threading modules
import threading
import time

get_time = lambda: int(round(time.time() * 1000))

# Movement constant
MOVE = 1E-4

#Initialize the PCA9685 Board using the default address (0x40)
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
SERVO_MIN = 120
SERVO_MAX = 660
CHANNEL = 0

# Current position
current = 0
currentThread = None

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
def handle_input(v, dt):
    global current
    current += MOVE * v * dt
    current = get_pulse(current)
    current = int(current)
    pwm.set_pwm(CHANNEL, 0, current)
    return
    global currentThread
    if currentThread is None:
        currentThread = threading.Thread(target=handle_input_async, args=(v, dt))
        currentThread.start()
    else:
        currentThread.join()
        currentThread = None
        handle_input(v, dt)

# Handle input asynchronously by lerping over the range in the given dt
def handle_input_async(v, dt):
    global current
    start = get_time()
    while get_time() <= start + dt:
        dx = lerp(v, (get_time() / (start + dt)) * dt)
        current += dx
        current = get_pulse(current)
        current = int(current)
        pwm.set_pwm(CHANNEL, 0, current)

# LERP helper function
def lerp(v, t):
    return MOVE * v * t
