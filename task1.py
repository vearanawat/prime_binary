#check if prime number:
def prime(num):
    if num <= 1: #num has to be greater than 1
        return False
    if num <= 3: #2,3 are prime num
        return True
    if num % 2 == 0 or num % 3 == 0: 
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

#find divisors:
def div(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# final result:
def Final(start, end):
    result = {}
    for num in range(start, end):
        if prime(num):
            result[num] = bin(num)[2:]  #print without 0b
        else:
            result[num] = div(num)
    return result

start = int(input("start: "))
end = int(input("end: "))
result_dict = Final(start, end)
print(result_dict)
