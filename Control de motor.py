import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

for i in range(5):
    # Giro de motor por 5 segundos
    print "Girando el motor"
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    time.sleep(5)

    # Gira de motor en sentido contrario por 5 segundos
    print "Gira el kotor en sentido contrario"
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(5)

GPIO.cleanup()
