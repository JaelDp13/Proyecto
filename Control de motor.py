import RPi.GPIO as GPIO
import time


class MotorControl:
    def _init_(self, ena, in1, in2):
        self.ENA = ena
        self.IN1 = in1
        self.IN2 = in2

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.ENA, 100)
        self.pwm.start(0)

    def forward(self, speed):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def backward(self, speed):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)


ENA = 18
IN1 = 23
IN2 = 24

motor = MotorControl(ENA, IN1, IN2)

try:
    motor.forward(50)
    time.sleep(2)
    motor.backward(75)
    time.sleep(2)
    motor.stop()

except KeyboardInterrupt:
    motor.stop()
    GPIO.cleanup()
