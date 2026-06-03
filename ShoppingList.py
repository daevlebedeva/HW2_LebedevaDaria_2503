from Ingredient import Ingredient
class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self,recipe,portions):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        newReceipe=recipe.scale(portions)
        for currIng in newReceipe.ingredients:
            self._items.append((currIng, newReceipe.title))
    def remove_recipe(self,title):
        self._items=[curr for curr in self._items if curr[1]!=title]
    def get_list(self):
        dict={}
        final=[]
        for currIng in self._items:
            if (currIng[0].name,currIng[0].unit) not in dict:
                dict[(currIng[0].name,currIng[0].unit)]=currIng[0].quantity
            else:
                dict[(currIng[0].name,currIng[0].unit)]+=currIng[0].quantity
        for k in dict:
            final.append(Ingredient(k[0],dict[k],k[1]))
        final.sort(key=lambda x: x.name)
        return final
    def __add__(self, other):
        new=ShoppingList()
        for i in self._items:
            new._items.append(i)
        for i in other._items:
            new._items.append(i)
        return new