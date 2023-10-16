import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

for i in range(5):
    # Gira el motor en un sentido durante 3 segundos
    print "Girando motor en un sentido"
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    time.sleep(3)

    # Gira el motor en el otro sentido durante 3 segundos
    print "Girando motor en sentido contrario"
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(3)

GPIO.cleanup()
