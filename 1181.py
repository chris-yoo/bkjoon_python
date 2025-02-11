import sys

input = sys.stdin.readline

T = int(input())

strings = []

for i in range(T):
    a = input()
    strings.append(a.replace("\n",""))
    
strings = list(set(strings))
    
def sort_function (string):
    return len(string), string
    
sorted_string = sorted(strings, key = sort_function)

for string in sorted_string :
    print(string)