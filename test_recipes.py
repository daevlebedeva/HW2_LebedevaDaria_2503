from Recipe import Recipe
from Ingredient import Ingredient
from ShoppingList import ShoppingList
import pytest
def test_toCheckTheIngredientCreation():
    currIng=Ingredient("Бананчики", 267, "г")
    assert currIng.name=="Бананчики"
    assert currIng.quantity==267.0
    assert currIng.unit=="г"
def test_toCheckStr():
    currIng=Ingredient("Бананчики", 267, "г")
    assert str(currIng)=="Бананчики: 267.0 г"
def test_toCheckEq1():
    currIng=Ingredient("Бананчики", 267, "г")
    currIng1=Ingredient("Бананчики", 367, "г")
    assert currIng==currIng1
def test_toCheckEq2():
    currIng=Ingredient("Бананчики", 267, "г")
    currIng1=Ingredient("Помидоры", 267, "г")
    assert currIng!=currIng1
def test_toCheckEq3():
    currIng=Ingredient("Бананчики", 267, "г")
    currIng1=Ingredient("Бананчики", 267, "т")
    assert currIng!=currIng1
def test_toCheckTheRecipeCreation():
    currIng=Ingredient("Бананчики", 267, "г")
    currRec=Recipe("Мороженое", [currIng])
    assert currRec.title=="Мороженое"
    assert currRec.ingredients==[currIng]
def test_toCheckAdd():
    currRec=Recipe("Мороженое", [])
    currIng=Ingredient("Бананчики", 267, "г")
    currIng1=Ingredient("Бананчики", 267, "г")
    currIng2=Ingredient("Клубничка", 267, "г")
    currRec.add_ingredient(currIng)
    currRec.add_ingredient(currIng1)
    currRec.add_ingredient(currIng2)
    assert len(currRec.ingredients)==2
    assert currRec.ingredients[0].quantity==534.0
    assert currRec.ingredients[1].quantity==267.0
def test_toCheckScale():
    currRec=Recipe("Мороженое", [Ingredient("Бананчики", 267, "г")])
    newRec=currRec.scale(67)
    assert newRec is not currRec
    assert currRec.ingredients[0].quantity==267.0
    assert newRec.ingredients[0].quantity==17889.0
def test_scaleValueError():
    currRec=Recipe("Мороженое", [Ingredient("Бананчики", 267, "г")])
    with pytest.raises(ValueError):
        currRec.scale(0)
def test_toCheckLen():
    currRec=Recipe("Мороженое", [])
    currIng = Ingredient("Бананчики", 267, "г")
    currIng1 = Ingredient("Бананчики", 267, "г")
    currIng2 = Ingredient("Клубничка", 267, "г")
    currRec.add_ingredient(currIng)
    currRec.add_ingredient(currIng1)
    currRec.add_ingredient(currIng2)
    assert len(currRec.ingredients)==2
def test_toCheckAddRecipe():
    iceCream=Recipe("Мороженое", [])
    iceCream.add_ingredient(Ingredient("Бананчики", 267, "г"))
    iceCream.add_ingredient(Ingredient("Клубничка", 267, "г"))
    currShoppList=ShoppingList()
    currShoppList.add_recipe(iceCream, 1)
    assert len(currShoppList._items)==2
def test_toCheckIncorrectPortion():
    iceCream = Recipe("Мороженое", [])
    iceCream.add_ingredient(Ingredient("Бананчики", 267, "г"))
    iceCream.add_ingredient(Ingredient("Клубничка", 267, "г"))
    currShoppList=ShoppingList()
    with pytest.raises(ValueError):
        currShoppList.add_recipe(iceCream, 0)
def test_toCheckRemoveRecipe():
    currShoppList=ShoppingList()
    iceCream=Recipe("Мороженое", [])
    iceCream.add_ingredient(Ingredient("Бананчики", 267, "г"))
    iceCream.add_ingredient(Ingredient("Клубничка", 267, "г"))
    salad=Recipe("Салат",[])
    salad.add_ingredient(Ingredient("Огурцы", 267, "г"))
    salad.add_ingredient(Ingredient("Помидоры", 267, "г"))
    currShoppList.add_recipe(iceCream, 1)
    currShoppList.add_recipe(salad, 1)
    currShoppList.remove_recipe("Мороженое")
    assert len(currShoppList._items)==2
    currShoppList.remove_recipe("Шоколадный фондан")
    assert len(currShoppList._items)==2
def test_toCheckGetListDuplicates():
    currShoppList=ShoppingList()
    soup=Recipe("Супчик", [])
    soup.add_ingredient(Ingredient("Морковка", 267, "г"))
    salad = Recipe("Салат", [])
    salad.add_ingredient(Ingredient("Морковка", 267, "г"))
    currShoppList.add_recipe(soup, 1)
    currShoppList.add_recipe(salad, 1)
    assert len(currShoppList.get_list())==1
    assert currShoppList.get_list()[0].quantity==534.0
def test_toCheckGetListSorted():
    iceCream=Recipe("Мороженое", [])
    iceCream.add_ingredient(Ingredient("Бананчики", 267, "г"))
    iceCream.add_ingredient(Ingredient("Клубничка", 367, "г"))
    iceCream.add_ingredient(Ingredient("Голубичка", 467, "г"))
    iceCream.add_ingredient(Ingredient("Молочко", 567, "г"))
    currShoppList=ShoppingList()
    currShoppList.add_recipe(iceCream, 1)
    toCheck=currShoppList.get_list()
    titles=[]
    for i in toCheck:
        titles.append(i.name)
    assert titles==["Бананчики", "Голубичка", "Клубничка", "Молочко"]
def test_toCheckAddShoppLists():
    currShoppList=ShoppingList()
    currShoppList1=ShoppingList()
    iceCream=Recipe("Мороженое", [])
    iceCream.add_ingredient(Ingredient("Бананчики", 267, "г"))
    iceCream.add_ingredient(Ingredient("Клубничка", 267, "г"))
    salad=Recipe("Салат", [])
    salad.add_ingredient(Ingredient("Огурцы", 267, "г"))
    salad.add_ingredient(Ingredient("Помидоры", 267, "г"))
    currShoppList.add_recipe(iceCream, 1)
    currShoppList1.add_recipe(salad, 1)
    all=currShoppList+currShoppList1
    assert len(all._items)==4
    assert len(currShoppList._items)==2
    assert len(currShoppList1._items)==2