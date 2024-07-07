class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.sauce = None
        
    def setBuns(self, bunStyle):
        self.buns = bunStyle  
    def setPatty(self, pattystyle):
        self.patty = pattystyle  
    def setSauce(self, sauceStyle):
        self.sauce = sauceStyle
        
    def print(self):
        print(self.buns, self.patty, self.sauce)
        
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
        
    def addBuns(self, buns):
        self.burger.setBuns(buns)
        return self
    def addPatty(self, patty):
        self.burger.setPatty(patty)
        return self
    def addSauce(self, sauce):
        self.burger.setSauce(sauce)
        return self
        
    def build(self):
        return self.burger.print()
        
cheeseBurgerBuilder = BurgerBuilder().addBuns("Toased").addPatty("Beef").addSauce("Ketchup").build()




