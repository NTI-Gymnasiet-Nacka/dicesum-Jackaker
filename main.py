# Dice sum probability calculator
# Författare: Jack Åkerblom
# Datum:20240822

user_input = input().split(" ")
N = int(user_input[0])
M = int(user_input[1])

def main(N,M):
    lista=[]
    for f in range(1,N+1):
        for i in range(1,M+1):
            lista.append(f+i)
        lista=sorted(lista)
    return lista

lista2=[]
lista3=[]
for t in range(min(main(N,M)),max(main(N,M))+1):
    lista2.append(main(N,M).count(t))
    lista3.append(t)

c=lista2.index(max(lista2))
e=len(lista2)-c

for r in range(c,e):
    print(str(lista3[r]))

