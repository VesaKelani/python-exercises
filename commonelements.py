import random;

a = [random.randint(0,50)for i in range(10)]
b = [random.randint(0,50)for i in range(10)]

common = list(set(a).intersection(b))
if len(common) == 0:
    print("no common")
else:
    print(common)
