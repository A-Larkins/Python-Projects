catches = [10, 20, 30, 40]

def divide_by_two(x):
    return x/2

half_ppr = map(divide_by_two, catches)
half_ppr = list(half_ppr)
print(half_ppr)

# or

half_ppr2 = map(lambda x: x/2, catches)
half_ppr2 = list(half_ppr2)
print(half_ppr2)
