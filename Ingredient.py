class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name=name
        self.quantity=quantity
        self.unit=unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,number):
        if number>0:
            self._quantity=float(number)
        else:
            raise ValueError("Количество должно быть положительным")
    def __str__(self):
        return self.name+": "+str(self.quantity)+" "+self.unit
    def __repr__(self):
        return "Ingredient('"+self.name+"', "+str(self.quantity)+", '"+self.unit+"')"
    def __eq__(self, other):
        return self.name==other.name and self.unit==other.unit