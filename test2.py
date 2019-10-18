import cham0421Library


print("_________Main Menu___________")
print("||  SELECT:                ||")
print("1- change the backlight color")
option = input()


if option == "1":
    x = int(input("please enter the number of x"))
    cham0421Library.vertical(x)

elif option == "2":
    y = int(input("please enter the number of y"))
    cham0421Library.horonztail()

elif option == "3":
    cham0421Library.staircase()

elif option == "4":
    cham0421Library.random_pixel()

elif option == "5":
    cham0421Library.clearBacklight()
else:
    print("hi")
