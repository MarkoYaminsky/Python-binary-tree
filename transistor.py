class Transistor:
    def __init__(self, transistor_type: str, make: str, amperage: float, voltage: float):
        self.voltage = voltage
        self.amperage = amperage
        self.make = make
        self.transistor_type = transistor_type

    def __str__(self):
        return f'voltage = {self.voltage}, amperage = {self.amperage}, ' \
               f'make is {self.make}, transistor type is {self.transistor_type}'
