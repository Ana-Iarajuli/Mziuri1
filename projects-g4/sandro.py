import random as r
print("            ______")
print("            _\ _~-\___")
print("    =  = ==(____AA____D")
print("                \_____\___________________,-~~~~~~~`-.._")
print("                /     o O o o o o O O o o o o o o O o  |\_")
print("                `~-.__        ___..----..                  )")
print("                      `---~~\___________/------------`````")
print("                      =  ===(_________D")
print("There is a man in this plane, who is planting bombs in the airplane.\nOne bomb is planted in the top of the airplane.\nHe thought of one of the dozen. If you guess at least one of these ten numbers, the bomb will not explode, otherwise he will plant down another bomb.\nIf you guess the right, he will try to detonate the bomb again, so he will thought and you have to guess again.")
num1 = int(input("\n\nEnter the number from 10 to 100, you think he thought: "))
thought_number1 = r.randint(1, 9)
if num1 // 10 == thought_number1:
    print("You are very lucky!!!  ARRRRRR")
    print("            ______")
    print("            _\ _~-\___")
    print("    =  = ==(____AA____D")
    print("                \_____\___________________,-~~~~~~~`-.._")
    print("                /     o O o o o o O O o o o o o o O o  |\_")
    print("                `~-.__        ___..----..                  )")
    print("                      `---~~\___________/------------`````")
    print("                      =  ===(_________D")
else:
    print("BOOOOOOOM!!!\n Another bomb has been planted, bad luck HAHAHAHA")
    print("            ______")
    print("            _\ _~-\___")
    print("    =  = ==(____AA____D")
    print("                \_____                        ~~~~`-.._")
    print("                /     o O                   o o o O o  |\_")
    print("                `~-.__        ___.     ..                  )")
    print("                      `---~~\___________/------------`````")
    print("                      =  ===(_________D")
print("If you guess first number, that doesn't mean that plane survived, so i blew it up and placed down a bomb! HAHAHAHA ")
num2 = int(input("\n\nEnter the number from 10 to 100, you think he thought: "))
thought_number2 = r.randint(1, 9)
if num2 // 10 == thought_number2:
    print("That mean nothing for me, plane has been destroyed anyway!")
else:
    print("I ordered nuke on this plane and it will come and blew plane up in 10 seconds and i will give you no chances to save a plane!\n PPPPPPXXXXXSSSSSSSS")
