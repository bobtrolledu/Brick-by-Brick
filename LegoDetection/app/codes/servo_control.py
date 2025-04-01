import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def open_close():
    duty_cycle = 170 / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1.5)

    duty_cycle = 5 / 18 + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.7)

    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

def half():
    duty_cycle =  5 / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

if __name__ == "__main__":
    open_close()
    pwm.stop()
    GPIO.cleanup()

        
