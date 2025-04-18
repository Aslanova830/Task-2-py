def choose_coffee_type(coffee):
    if coffee=="latte":
        return "latte"
    elif coffee=="cappuccino":
        return "cappuccino"
    elif coffee=="espresso":
        return "espresso"
ctype=input("hansi kofe?")
choose_coffee_type(ctype)
def choose_size():
    if size=="single":
        return "single"
    elif size=="double":
        return "double"
size=input("olcu nece olsun")
def brew_coffee(coffe, csize):
    if csize=="double":
        print("50q")
    elif csize != "double":
        print("25q qehve")
    if coffe=="latte" or coffe=="cappucino":
        print("sud elave et")
    else:
        print("sud olmasin")
brew_coffee(ctype,size)