import random

again = True

while again:
    print(random.randint(1,6))
    anotherroll = input("Want to roll again? (y/n): ")
    if anotherroll.lower()=="y":
        continue
    else:
        break