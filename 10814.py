import sys

input = sys.stdin.readline

T = int(input())
users = []

for _ in range(T):
    a,b = input().split(" ")
    users.append((int(a),b.replace("\n","")))

sorted_users = sorted(users, key=lambda user: user[0])

for user in sorted_users:
    print(f"{user[0]} {user[1]}")