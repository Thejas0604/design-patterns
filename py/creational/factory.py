# burgerFactory

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:
    def createCheeseBurgers(self):
        ingredients = "Cheese"
        return Burger(ingredients)
    def createBeefBurgers(self):
        ingredients = "Beef"
        return Burger(ingredients)
    def createVegBurgers(self):
        ingredients = "Veg"
        return Burger(ingredients)
    
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurgers().print()