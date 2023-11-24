import time


class MotorControl:
    def _init_(self):
        print("Inicializando control de motor")

    def stop(self):
        print("Deteniendo motor")


class UltrasonicSensor:
    def _init_(self):
        print("Inicializando sensor ultrasónico")

    def measure_distance(self):
        # Simulación de la medición de distancia
        distance = 14  # Simula una distancia de 14 cm
        return distance


motor = MotorControl()
ultrasonic_sensor = UltrasonicSensor()

try:
    while True:
        distance = ultrasonic_sensor.measure_distance()
        print(f"Distancia: {distance} cm")

        if distance <= 15:
            motor.stop()
        else:
            print("Avanzando")

        time.sleep(1)

except KeyboardInterrupt:
    motor.stop()
