import rev, wpilib, time
import wpilib.drive


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
        self.left_y = self.controller.getLeftY()
        self.left_x = self.controller.getLeftX()

        #Motor Declaration
        self.lf_motor = wpilib.PWMSparkMax(1)
        self.lr_motor = rev.CANSparkMax(3, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.rf_motor = wpilib.PWMSparkMax(2)
        self.rr_motor = rev.CANSparkMax(2, rev.CANSparkLowLevel.MotorType.kBrushed)

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
        left_y = self.controller.getLeftY()
        # print(f"RightY: {RightY} - LeftY: {LeftY}")
        old = str(self.left_y) + " : " + str(self.left_x)
        new = str(self.left_y) + " : " + str(self.left_x)
        if new != old:
            print(new)

        # exponential movement
        if right_y < 0:
            right_y = (right_y ** 4) * -1
        else:
            right_y = (right_y ** 4)

        if left_y < 0:
            left_y = (left_y ** 4) * -1
        else:
            left_y = (left_y ** 4)
        right_y = right_y * .9
        left_y = left_y * .9
        # this makes it turn slower
        if (0.1 > right_y > -0.1) and (left_y >= 0.5 or left_y <= -0.5):
            left_y = left_y * 0.66
        elif (0.1 > left_y > -0.1) and (right_y >= 0.5 or right_y <= -0.5):
            right_y = right_y * 0.66

        self.drive.tankDrive(right_y, left_y)