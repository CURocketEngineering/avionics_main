# Config.py

# For use in debugging program
DEBUG = False

# Seconds to push charge to e-match
PARACHUTE_CHARGE_TIME = 0.5

# Seconds to wait after apogee before deploying parachute
APOGEE_DELAY = 0

# Main parachute height in ft
MAIN_ALTITUDE = 1000

# Seconds to wait after reaching parachute height before deploying parachute
MAIN_DELAY = 0

class Config:
    def __init__(self):
        """Read (TODO) initialization values."""
        self.DEBUG = True
        self.Test = False
        self.PARACHUTE_CHARGE_TIME = 0.5
        self.APOGEE_DELAY = 0
        self.MAIN_ALTITUDE = 1000
        self.MAIN_DELAY = 0
