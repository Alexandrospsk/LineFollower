import board
import simpleio
import digitalio
import time
import pwmio
from adafruit_motor import servo, motor
from adafruit_debouncer import Debouncer



Start_Button = digitalio.DigitalInOut(board.GP20)
Start_Button.direction = digitalio.Direction.INPUT
Start_Button.pull = digitalio.Pull.UP

Speed_Button = digitalio.DigitalInOut(board.GP21)
Speed_Button.direction = digitalio.Direction.INPUT
Speed_Button.pull = digitalio.Pull.UP

Speed_Switch = Debouncer(Speed_Button)
Start_Switch = Debouncer(Start_Button)

speed=0
start=0

sensorA = simpleio.DigitalIn(board.GP0)
sensorB = simpleio.DigitalIn(board.GP7)

motor1_A = pwmio.PWMOut(board.GP8, frequency=50)
motor1_B = pwmio.PWMOut(board.GP9, frequency=50)
motor1= motor.DCMotor(motor1_A,motor1_B)

motor2_A = pwmio.PWMOut(board.GP10, frequency=50)
motor2_B = pwmio.PWMOut(board.GP11, frequency=50)
motor2= motor.DCMotor(motor2_A,motor2_B)



while True:
    Speed_Switch.update()
    Start_Switch.update()
    sensor1 = sensorA.value
    sensor2 = sensorB.value
    #zero is seeing white
    
    if Start_Switch.fell:
        start=1-start
    
    if Speed_Switch.fell and start == 1:
        if speed != 1:
            speed=speed+0.25
        else:
            speed=0.25
    if start == 0:
        speed=0
        
        
    if sensor1 == 0:
        if sensor2 == 0:
            motor1.throttle=speed
            motor2.throttle=speed
            
        elif sensor2 == 1:
            motor1.throttle=0
            motor2.throttle=speed
            
    elif sensor1 == 1:
        if sensor2 == 1:
            motor1.throttle=0
            motor2.throttle=0
            
        else:
            motor1.throttle=speed
            motor2.throttle=0
