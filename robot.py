import rev, wpilib
import wpilib.drive


class RRobot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()


        #Joystick Declaration
        self.joystick = wpilib.XboxController(0)

        #Motor Declaration
        self.lf_motor = rev.CANSparkMax(4, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.lr_motor = rev.CANSparkMax(3, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.rf_motor = rev.CANSparkMax(9, rev.CANSparkLowLevel.MotorType.kBrushed)
        self.rr_motor = rev.CANSparkMax(2, rev.CANSparkLowLevel.MotorType.kBrushed)

    def robotInit(self):
        return None
