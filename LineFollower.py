import board
import simpleio

import time
import pwmio
from adafruit_motor import  motor

time.sleep(2)

sensorA = simpleio.DigitalIn(board.GP0)
sensorB = simpleio.DigitalIn(board.GP7)

motor1_A = pwmio.PWMOut(board.GP8, frequency=50)
motor1_B = pwmio.PWMOut(board.GP9, frequency=50)
motor1= motor.DCMotor(motor1_A,motor1_B)

motor2_A = pwmio.PWMOut(board.GP10, frequency=50)
motor2_B = pwmio.PWMOut(board.GP11, frequency=50)
motor2= motor.DCMotor(motor2_A,motor2_B)

def Motors(M1=0,M2=0):
    motor1.throttle = M1
    motor2.throttle = M2
    
speed=0.7
Motors(1,1)
while True:
    L_sensor = sensorA.value
    R_sensor = sensorB.value
    #optimal speed 0.55
    #zero is seeing white
    if L_sensor == 0 and R_sensor == 0 :
        Motors(speed,speed)
    if L_sensor == 0 and R_sensor == 1 :
        if L_sensor ==1:
            Motors(0,0)
            break
        else:
            Motors(-(speed+0.25),speed+0.25)
    if L_sensor == 1 and R_sensor == 0 :
        if R_sensor == 1 :
            Motors(0,0)
            break
        else:
            Motors(speed,-speed)
    if L_sensor == 1 and R_sensor == 1 :
        Motors(0,0)
        break   
            
