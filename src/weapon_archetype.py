
class Archetype:

    def __init__(self) -> None:
        self.base_range = 0
        self.scaled_range = 0
        self.body_damage = 0
        self.precision_damage = 0

    def calculateRange(self, range_stat):
        return self.base_range + (self.scaled_range * range_stat)


class AutoRifle(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 18.28
        self.scaled_range = 0.2125
        self.firing_mode = 'single'
        self.subfamilies = [
            'Adapative (600 RPM)',
            'Precision (450 RPM)',
            'Rapid-Fire (720 RPM)',
            'High-Impact (360 RPM)'
        ]

class Autorifle_Adapative(AutoRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 15.01
        self.precision_damage = 23.40
        self.rpm = 600


class Autorifle_Precision(AutoRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 20.0
        self.precision_damage = 31.18
        self.rpm = 450

class Autorifle_RapidFire(AutoRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 13.41
        self.precision_damage = 20.12
        self.rpm = 720

class Autorifle_HighImpact(AutoRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 22.0
        self.precision_damage = 35.16
        self.rpm = 360


class HandCannon(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 24
        self.scaled_range = 0.135
        self.firing_mode = 'single'
        self.subfamilies = [
            'Adapative (140 RPM)',
            'Lightweight (140 RPM)',
            'Precision (180 RPM)',
            'Aggressive (120 RPM)'
        ]

#Adaptive and Precision HC's share a damage profile
class HandCannon_Adapative(HandCannon):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 46.50
        self.precision_damage = 69.75
        self.rpm = 140

class HandCannon_Precision(HandCannon):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 40.00
        self.precision_damage = 60.00
        self.rpm = 180

class HandCannon_Aggressive(HandCannon):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 50.0
        self.precision_damage = 79.90
        self.rpm = 120


class SMG(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 14.42
        self.scaled_range = 0.091
        self.subfamilies = [
            'Adapative (900 RPM)',
            'Lightweight (900 RPM)',
            'Precision (600 RPM)',
            'Aggressive (750 RPM)'
        ]

class SMG_Adapative(SMG):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 11.25
        self.precision_damage = 16.88
        self.rpm = 900

class SMG_Lightweight(SMG):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 10.86
        self.precision_damage = 17.99
        self.rpm = 900

class SMG_Precision(SMG):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 17.01
        self.precision_damage = 23.85
        self.rpm = 600

class SMG_Aggressive(SMG):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 14.00
        self.precision_damage = 21.00
        self.rpm = 720


class PulseRifle(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 25.5
        self.scaled_range = 0.1445
        self.firing_mode = 'burst'
        self.subfamilies = [
            'Adapative (390 RPM)',
            'Lightweight (450 RPM)',
            'Rapid-Fire (540 RPM)',
            'High-Impact (340 RPM)',
            'Aggressive (450 RPM)'
        ]

class PulseRifle_Adaptive(PulseRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 19.01
        self.precision_damage = 31.50
        self.rpm = 385.71
        self.shots_per_burst = 3

class PulseRifle_Lightweight(PulseRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 16.0
        self.precision_damage = 26.51
        self.rpm = 450.0
        self.shots_per_burst = 3

class PulseRifle_RapidFire(PulseRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 14.00
        self.precision_damage = 23.75
        self.rpm = 540.0
        self.shots_per_burst = 3

class PulseRifle_HighImpact(PulseRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 22.0
        self.precision_damage = 35.16
        self.rpm = 337.5
        self.shots_per_burst = 3

class PulseRifle_Aggressive(PulseRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 15.5
        self.precision_damage = 26.29
        self.rpm = 450.0
        self.shots_per_burst = 4


class ScoutRifle(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 60
        self.scaled_range = 0.3
        self.subfamilies = [
            'Lightweight (200 RPM)',
            'Precision (180 RPM)',
            'Rapid-Fire (260 RPM)',
            'High-Impact (150 RPM)',
            'Aggressive (120 RPM)'
        ]

class ScoutRifle_Lightweight(ScoutRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 30.50
        self.precision_damage = 53.52
        self.rpm = 200

class ScoutRifle_Precision(ScoutRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 38.00
        self.precision_damage = 60.73
        self.rpm = 180

class ScoutRifle_RapidFire(ScoutRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 27.50
        self.precision_damage = 46.64
        self.rpm = 257.14

class ScoutRifle_HighImpact(ScoutRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 40.00
        self.precision_damage = 70.20
        self.rpm = 150

class ScoutRifle_Aggressive(ScoutRifle):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 54.0
        self.precision_damage = 79.94
        self.rpm = 120


class Sidearm(Archetype):
    def __init__(self) -> None:
        super().__init__()
        self.base_range = 13.2
        self.scaled_range = 0.048
        self.firing_mode = 'single'
        self.subfamilies = [
            'Omolon Adapative Frame (491)',
            'Adapative Frame (300)',
            'Precision (260 RPM)',
            'Lightweight (360 RPM)',
            'Rapid-Fire (450 RPM)',
            'Aggressive (325 RPM)'
        ]      

class Sidearm_OmolonAdapative(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 20.00
        self.precision_damage = 31.96
        self.rpm = 490.91
        self.firing_mode = 'burst'
        self.shots_per_burst = 3

class Sidearm_Adaptive(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 36.00
        self.precision_damage = 50.47
        self.rpm = 300

class Sidearm_Precision(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 40.0
        self.precision_damage = 56.08
        self.rpm = 257.14

class Sidearm_Lightweight(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 31.00
        self.precision_damage = 43.56
        self.rpm = 360

class Sidearm_RapidFire(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 25.00
        self.precision_damage = 35.05
        self.rpm = 450

class Sidearm_Aggressive(Sidearm):
    def __init__(self) -> None:
        super().__init__()
        self.body_damage = 32.01
        self.precision_damage = 44.88
        self.rpm = 327.27
        self.firing_mode = 'burst'
        self.shots_per_burst = 2

