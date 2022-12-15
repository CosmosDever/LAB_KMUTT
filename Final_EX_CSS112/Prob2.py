#Question 2
class Item:
    def __init__(self,energy):
        self.energy = energy
    
class Robot:
   
    def serve(self):
        return "serve with {} Electrical energy need is {} Watt-Hour".format(self.item.__class__.__name__,self.item.energy)

class Armhand(Item):
    def __init__(self,energy,length):
        super(Armhand, self).__init__(energy)
        self.length = length   
      
    
class IndustrialArmRobot(Robot):
    
    def __init__(self,height,energy,length):
        self.height = height
        self.item = Armhand(energy, length)




def Problem2(): 

    anIndustrialArmRobot = IndustrialArmRobot(170,213,2.0)
    msg  = anIndustrialArmRobot.serve()
    print(msg)
    return msg
Problem2()