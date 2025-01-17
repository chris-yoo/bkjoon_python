T = int(input())
num_list = list(map(int, input().split()))

def find_decimal(num_list):
    decimal_list = []
    for num in num_list:
        divisors = []
        for j in range(1,num+1):
            if num%j == 0:
                divisors.append(j)
        if len(divisors) == 2:
            decimal_list.append(num)
    return len(decimal_list)

print(find_decimal(num_list))