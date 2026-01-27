n1 = input()
n2 = input()
if ((n1 =="rock") and (n2 =="paper")):
    print(f"{n1} wins")
elif ((n1 =="rock") and (n2 =="scissors")):
    print(f"{n2} wins")
elif ((n1 == "rock") and (n2=="rock")):
    print("match draw")
elif ((n1 == "paper") and (n2 =="rock")):
    print(f"{n2} wins")
else:
    print("enter valid input")