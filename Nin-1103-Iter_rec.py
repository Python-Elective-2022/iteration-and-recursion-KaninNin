#Navy helped me with this assignement
'''
function iterativePower base and exponent 
    result equal to one
    for i every range of exponent value 
        it will be equal to the result multiply the base
    return the result
print the function iterativePower and the base 2 and exponent 3

function recursivePower base and exponent
    if exponent is one
        will return base
    else
        will return base and exponent -1
    print recursivePower and base 2 and exponent 3
'''
def iterativePower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterativePower(2,3))
base = 0
exp = 0
def recursivePower(base, exp):
    if exp == 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(2,3))