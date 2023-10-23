import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p.start(25)
print("\n")
print("La velocidad y direccion del Motor")
print("C-Correr A-Alto Av-Avanzar R-Reversa L-Low M-Medium H-High E-Exit")
print("\n")

while (1):

    x = raw_input()

    if x == 'C':
        print("Correr")
        if (temp1 == 1):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            print("Av")
            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            print("Reversa")
            x = 'z'


    elif x == 'A':
        print("Alto")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        x = 'z'

    elif x == 'Av':
        print("Avanzar")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 'R':
        print("Reversa")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 'L':
        print("Low")
        p.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'M':
        print("Medium")
        p.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'H':
        print("High")
        p.ChangeDutyCycle(75)
        x = 'z'

if __name__ == "__main__"
  main()
