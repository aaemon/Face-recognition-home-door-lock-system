import RPi.GPIO as GPIO
import time


def Distance(TRIG=23, ECHO=24):
    '''
    arguments:

    TRIG: trigger pin for the HC-SR04 ultrasonic sensor, by default value is 23
    ECHO: echo pin for the HC-SR04 ultrasonic sensor, by default value is 24
    '''
    GPIO.setmode(GPIO.BCM)

    # initialization in case sensor won't work
    start = time.time()
    end = time.time()

    # setting the trigger and echo pins as output and input respectively
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # sending trigger signal
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.0002)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # calculating time for echo to return
    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    sig_time = end - start

    # calculating distance from time
    distance = sig_time / 0.000058
    GPIO.cleanup()

    # print('Object is at {} cm'.format(round(distance),4))
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = Distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
