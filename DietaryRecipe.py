from Recipe import Recipe
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients=[]
        self.diet_type=diet_type
        super().__init__(title, ingredients)
    def scale(self, ratio):
        return DietaryRecipe(self.title, self.diet_type, super().scale(ratio).ingredients)
    def __str__(self):
        return "["+self.diet_type+"] "+super().__str__()