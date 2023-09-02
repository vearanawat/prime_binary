#check if prime number:
def prime(num):
    flag = False
    if num == 1:
        flag = False
    elif (num > 2):
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
            else:
                flag = True
    elif (num == 2):
        flag = True
    return flag

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
