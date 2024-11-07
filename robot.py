import rev, wpilib, time
import wpilib.drive
from halsim_gui.main import logger

kY = 4 #Y Button
kX = 3 #X Button
kB = 2 #B Button
kA = 1 #A Button
kLB = 5 #LB Button
kRB = 6 #RB Button
kBack = 7 #Back Button
kStart = 8 #Start Button

class RRobot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()


        #Joystick Declaration
        self.controller = wpilib.XboxController(0)

        #Motor Declaration
        self.lf_motor = wpilib.PWMSparkMax(1)
        self.lr_motor = wpilib.PWMSparkMax(3)
        self.rf_motor = wpilib.PWMSparkMax(2)
        self.rr_motor = wpilib.PWMSparkMax(4)

        self.l_motor = wpilib.MotorControllerGroup(self.lf_motor, self.lr_motor)
        self.l_motor.setInverted(True)
        self.r_motor = wpilib.MotorControllerGroup(self.rf_motor, self.rr_motor)
        self.drive = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)



    def robotInit(self):
        return None


    def teleopInit(self):
        return None

    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
        # TEST THIS LATER (MOVEMENT ADJUSTMENTS)
        # drive motors
        right_y = self.controller.getRightY()
        trigger = self.controller.getRightTriggerAxis()



        # Makes the bot move according to how much the trigger is pressed and turn at about the same speed it'll turn whilst moving

        if trigger > 0:
            self.drive.curvatureDrive(-1 * trigger, self.controller.getLeftX(), False)
        else:
            self.drive.curvatureDrive(0, 1/2 * self.controller.getLeftX(), True)