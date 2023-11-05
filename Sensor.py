import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO_LED = 12
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)


GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_LED, False)


distance_limit = 15

try:
    print('Sensor ultrasonico HC-SR04')


    while True:


        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)


        start = time.time()


        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()


        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()

        
        elapsed = stop - start
        distance = (elapsed * 34300) / 2


        if distance < distance_limit:
            print('Stop! Objeto a ' + str(distance) + 'cm')
            GPIO.output(GPIO_LED, True)
        else:

            print('Go! No hay objetos delante')
            GPIO.output(GPIO_LED, False)

        # Pausa
        time.sleep(0.25)

except KeyboardInterrupt:

    print('Sensor Stopped')
    GPIO.cleanup()