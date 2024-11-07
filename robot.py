import wpilib
from util import util
import wpilib.drive

config = util.load_config("util/config.json")



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
    def robotPeriodic(self):
        return None

    def trigger_drive(self):

        # Trigger definitions

        r_trigger = self.controller.getRightTriggerAxis()
        l_trigger = self.controller.getLeftTriggerAxis()

        # Makes the bot move according to how much the trigger is pressed and turn at about the same speed it'll turn whilst moving

        if r_trigger > 0:
            self.drive.curvatureDrive(-1 * r_trigger, self.controller.getLeftX(), False)
        elif l_trigger > 0:
            self.drive.curvatureDrive(l_trigger, self.controller.getLeftX(), False)
        else:
            self.drive.curvatureDrive(0, 1 / 2 * self.controller.getLeftX(), True)

    def axis_drive(self):

        # Makes the bot move with only the left stick

        lx = self.controller.getLeftX()
        ly = self.controller.getLeftY()
        self.drive.curvatureDrive(ly,1/2 * lx,True)

    def dual_axis_drive(self):

        # Makes the bot accelerate with left stick and turn with the right stick

        ly = self.controller.getLeftY()
        rx = self.controller.getRightX()
        self.drive.curvatureDrive(ly,1/2 * rx,True)

    def true_dual_axis_drive(self):

        # Original movement each stick controls a side of motors

        ly = self.controller.getLeftY()
        ry = self.controller.getRightY()
        self.drive.tankDrive(ly,ry)



    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
        if config["control_mode"] == 1:
            RRobot.trigger_drive(self)
        elif config["control_mode"] == 2:
            RRobot.axis_drive(self)
        elif config["control_mode"] == 3:
            RRobot.dual_axis_drive(self)
        elif config["control_mode"] == 4:
            RRobot.true_dual_axis_drive(self)
        else:
            return None

