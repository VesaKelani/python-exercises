import random;

a = [random.randint(0,50)for i in range(10)]
b = [random.randint(0,50)for i in range(10)]
# a = []
# for i in range(0,20):
#     x = random.randint(1,100)
#     a.append(x)
# b = []
# for i in range(0,20):
#     x = random.randint(1,100)
#     b.append(x)
#a = [1,4,5,7,8]
#b = [1,3,4,5,8]

common = list(set(a).intersection(b))
if len(common) == 0:
    print("no common")
else:
    print(common)
