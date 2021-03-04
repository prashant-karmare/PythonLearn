#Supporting Module for 5CheckPrime to find Prime No
def ChkPrime(no):
    for i in range(2,no):
        if no%i == 0:
            return False
    else:
        return True