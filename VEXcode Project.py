#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
FrontLeft = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
FrontRight = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
BackLeft = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
BackRight = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
flywheel_motor_a = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
flywheel_motor_b = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
flywheel = MotorGroup(flywheel_motor_a, flywheel_motor_b)
intake = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
#
# 	Project:
#	Author:
#	Created:
#	Configuration:
#
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

def pre_autonomous(): #anything before the match starts
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous(): #without human control
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control(): #user control
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        wait(20, MSEC)
        #X-Drive
        FrontLeft.spin(FORWARD,controller_1.axis3.position()-controller_1.axis4.position()+controller_1.axis1.position(),PERCENT)
        FrontRight.spin(FORWARD,controller_1.axis1.position()-controller_1.axis3.position()-controller_1.axis4.position(),PERCENT)
        BackLeft.spin(FORWARD,controller_1.axis3.position()+controller_1.axis4.position()+controller_1.axis1.position(),PERCENT)
        BackRight.spin(FORWARD,controller_1.axis1.position()-controller_1.axis3.position()+controller_1.axis4.position(),PERCENT)
        FrontLeft.set_stopping(BRAKE)
        FrontRight.set_stopping(BRAKE)
        BackLeft.set_stopping(BRAKE)
        BackRight.set_stopping(BRAKE)
        #flywheel
        if (controller_1.buttonX.pressing()):
            flywheel.spin(FORWARD,100,PERCENT)
        if (controller_1.buttonA.pressing()):
            flywheel.spin(FORWARD,50,PERCENT)
        if (controller_1.buttonB.pressing()):
            flywheel.spin(FORWARD,0,PERCENT)
        #intake
        if (controller_1.buttonR1.pressing()):
            intake.spin(FORWARD,100,PERCENT) #out
        elif (controller_1.buttonR2.pressing()):
            intake.spin(FORWARD,-100,PERCENT) #in
        else:
            intake.spin(FORWARD,0,PERCENT)
# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
