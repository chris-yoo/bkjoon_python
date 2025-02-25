N, M = map(int, input().split())

pokemons = {}

targets = []

for i in range(1,N+1):
    a = input()
    pokemons[i] = a

for _ in range(M):
    a = input()
    targets.append(a)
    
reversed_pokemons = {v:k for k, v in pokemons.items()}

for t in targets:
    if t.isnumeric():
        print(pokemons[int(t)])
    else:
        print(reversed_pokemons[t])