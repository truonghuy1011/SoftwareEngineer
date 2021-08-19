class IBattery:
   def charge(self): pass

   def discharge(self): pass
   def getFullCapacity(self): pass
   def getCurrentCapacity(self): pass

# Adaptee
class FastBattery(IBattery):
   def charge(self):
      return 200

   def discharge(self):
      return 100
   
   def getFullCapacity(self):
      return 1000
   
   def getCurrentCapacity(self):
      return 0

# Target interface
class SacPin:
   def charge(self): pass
   def discharge(self): pass
   

# The Adapter
class Adapter(SacPin):
   __battery = None
   def __init__(self, battery):
      self.__battery = battery
   
   def charge(self):
      return 0
   
   def discharge(self):
      return self.__battery.discharge()
   
  

# Client
class ElectricKettle:
   __power = None
   
   def __init__(self, power):
	   self.__power = power
   
   def boil(self):
      if self.__power.charge()!=0:
         print ("dang sac!")
      elif self.__power.discharge() == 100:
         print ("Ngung sac")
     

def main():
   fastB=FastBattery()
  
   adapter = Adapter(fastB)
   kettle = ElectricKettle(adapter)
	

   kettle.boil()
	
   return 0
	
if __name__ == "__main__":
   main()