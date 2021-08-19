class Cell():
    def __init__(self, maximum, energy):
        self.maximum = maximum
        self.energy = energy

class Battery(Cell):
    def __init__(self, type):
        self.type = type
        self.num_cell =0
        self.list_cell = []
    def charge(self):
        return ("Đang sạc pin")
class Proxy_Battery(Battery):
    def check(self):
        if self.type == "boost":
            print(f'{self.charge()} lần 1')
            print(f'{self.charge()} lần 2')
        elif self.type == 'nomal':
            print(f'{self.charge()} ')
def main():
    battery = Proxy_Battery('boost')
    battery.check()
main()
