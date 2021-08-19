class Cell():
    def __init__(self, maximum, energy):
        self.maximum = maximum
        self.energy = energy

class Charge():
    def nomal_charge(self):
        print("nomal charge")
    def round_robin(self):
        print("round robin charge")
    
class Battery(Cell, Charge):
    def __init__(self):
        self.num_cell = 0
        self.list_cell = []
        

def main():
    battery = Battery()
    battery.nomal_charge()
main()

