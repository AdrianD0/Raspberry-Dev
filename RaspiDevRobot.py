from nanpy import (ArduinoApi, SerialManager)
from time import sleep

PWM_LEFT = 5
DirL = 12
PWM_RIGHT = 6
DirR = 7

ENCODER_LEFT = 2
ENCODER_RIGHT = 4

pwmL = 200
pwmR = 200
DirA = 1
DirB = 1

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print('Failed to connect to arduino!')

a.pinMode(PWM_LEFT, a.OUTPUT)
a.pinMode(PWM_RIGHT, a.OUTPUT)
a.pinMode(DirL, a.OUTPUT)
a.pinMode(DirR, a.OUTPUT)


while True:
    a.digitalWrite(PWM_LEFT, pwmL)
    a.digitalWrite(DirL, DirA)
    print(pwmL)
    sleep(1)
    a.digitalWrite(PWM_RIGHT, pwmR)
    a.digitalWrite(DirR, DirB)
    print(pwmR)
    sleep(1)