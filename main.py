def fibb(num:int):
    if num == 1 or num == 2:
        return 1
    else:
        return fibb(num-1) + fibb(num-2)

print(fibb(5))