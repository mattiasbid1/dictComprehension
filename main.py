import random

listerino = ["Snake", "Worm", "Wurm", "Dragon"]

new_dict = {item:random.randint(1,100) for item in listerino}

print(new_dict)


supernew_dict = {n:m for (n,m) in new_dict.items() if m > 70}

print(supernew_dict)




