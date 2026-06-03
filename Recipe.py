from Ingredient import Ingredient
class Recipe:
    def __init__(self, title, ingredients):
        self.title=title
        self.ingredients=ingredients
    def add_ingredient(self,ingredient):
        flag=False
        for currIng in self.ingredients:
            if currIng==ingredient:
                currIng.quantity+=ingredient.quantity
                flag=True
        if flag==False:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if (type(ratio)==int or type(ratio)==float) and ratio>0:
            return True
        else:
            return False
    def scale(self,ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        newIngredients=[]
        for currIng in self.ingredients:
            newIngredients.append(Ingredient(currIng.name,currIng.quantity*ratio,currIng.unit))
        return Recipe(self.title,newIngredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        final=self.title+":\n"
        for currIng in self.ingredients:
            final+="-"+str(currIng)+"\n"
        return final