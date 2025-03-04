N = int(input())
trees_list = []
lenght_list = []

for _ in range(N):
    a = int(input())
    trees_list.append(a)

start_point = trees_list[0]
end_point = trees_list[-1]
added_tree_point = start_point


# GCD
def GCD(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return GCD(b, a % b)


# Length list
for i in range(N - 1):
    length = trees_list[i + 1] - trees_list[i]
    lenght_list.append(length)

lenght_list = list(set(lenght_list))


# Find GCD num of Lenght list
def findGCD(num_list: list):
    gcd = GCD(num_list[0], num_list[1])
    for i in range(1, len(num_list)):
        gcd = GCD(gcd, num_list[i])
    return gcd


if len(lenght_list) <= 1:
    print(0)
else:
    GCD_num = int(findGCD(lenght_list))
    total_num_tree = (end_point - start_point) // GCD_num + 1
    print(total_num_tree - len(trees_list))
