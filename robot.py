import wpilib
import wpilib.drive
import rev



class RRobot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()
        self.timer = wpilib.Timer()

        #Joystick Declaration
        self.controller = wpilib.XboxController(0)

        #Motor Declaration
        self.lf_motor = rev.CANSparkMax(4,rev.CANSparkMax.MotorType.kBrushless)
        self.lr_motor = rev.CANSparkMax(3,rev.CANSparkMax.MotorType.kBrushless)
        self.rf_motor = rev.CANSparkMax(9,rev.CANSparkMax.MotorType.kBrushless)
        self.rr_motor = rev.CANSparkMax(2,rev.CANSparkMax.MotorType.kBrushless)
        #self.lf_motor = wpilib.PWMSparkMax(4)
        #self.rf_motor = wpilib.PWMSparkMax(3)
        #self.lr_motor = wpilib.PWMSparkMax(6)
        #self.rr_motor = wpilib.PWMSparkMax(2)
        self.l_motor = wpilib.MotorControllerGroup(self.lf_motor, self.lr_motor)
        self.l_motor.setInverted(True)
        self.r_motor = wpilib.MotorControllerGroup(self.rf_motor, self.rr_motor)
        self.drive = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)


    def robotInit(self):
        print("Robot init called")
        print("Value = " + str())

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

    def old_drive(self):
        ly = self.controller.getLeftY()
        rx = self.controller.getRightX()

        if (rx < 0):
            rx = (rx ** 4) * -1
        else:
            rx = (rx ** 4)

        if (ly < 0):
            ly = (ly ** 4) * -1
        else:
            ly = (ly ** 4)
        rx = rx * .9
        ly = ly * .9
        # this makes it turn slower
        if (0.1 > rx > -0.1) and (ly >= 0.5 or ly <= -0.5):
            ly = ly * 0.66
        elif (0.1 > ly > -0.1) and (rx >= 0.5 or rx <= -0.5):
            rx = rx * 0.66

        self.drive.tankDrive(ly,rx)
    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""

        if self.controller.getRightTriggerAxis() != 0:
            self.drive.tankDrive(-self.controller.getRightTriggerAxis(), self.controller.getRightTriggerAxis())