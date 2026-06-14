def fac(num:int)->int:
    if num == 1 or num == 0:
        return 1
    else:
        return fac(num-1) * num

print(fac(3))

#----------------------------------

def fibb(num:int)->int:
    if num == 1 or num == 2:
        return 1
    else:
        return fibb(num-1) + fibb(num-2)

print(5)