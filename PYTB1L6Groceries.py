GroceryList = ["applesauce", "instant noodles", "hamburger", "pancaks"]

ShoppingCart = ["instant noodles", "applesauce", "pancakes", "hamburger", "ketchup", "bread"]

for x,y in zip(GroceryList, ShoppingCart):
    print(x,y)
    if x == y:
        print("Done Shopping")
    else:
        print("Continue Shopping")











