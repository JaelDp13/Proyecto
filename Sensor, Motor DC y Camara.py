import RPi.GPIO as GPIO
import time
import cap
import cv2


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

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)


class UltrasonicSensor:
    def _init_(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.output(self.trigger_pin, False)
        time.sleep(2)

    def measure_distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2

        return distance



ENA = 18
IN1 = 23
IN2 = 24


TRIG = 18
ECHO = 24


motor = MotorControl(ENA, IN1, IN2)
ultrasonic_sensor = UltrasonicSensor(TRIG, ECHO)


try:
    while True:

        ret, frame = cap.read()
        cv2.imshow('Camara', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        distance = ultrasonic_sensor.measure_distance()
        print(f"Distancia: {distance:.2f} cm")

        if distance <= 15:
            motor.stop()
            print("Deteniendo motor")
        else:
            motor.forward(50)  
            print("Avanzando")

        time.sleep(1)

except KeyboardInterrupt:
    motor.stop()
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
