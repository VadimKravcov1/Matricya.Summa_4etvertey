n = int(input())
list=[]
pie1 = 0
pie2 = 0
pie3 = 0
pie4 = 0
for i in range(n):
    # print(i)
    item = [int(num) for num in input().split()]
    list.append(item)

for i in range(n):
    for j in range(n):
        if i<j and i<n-1-j:
            pie1+=list[i][j]
print("Верхняя четверть:",pie1)

for i in range(n):
    for j in range(n):
        if i<j and i>n-1-j:
            pie2+=list[i][j]
print("Правая четверть:",pie2)

for i in range(n):
    for j in range(n):
        if i>j and i>n-1-j:
            pie3+=list[i][j]
print("Нижняя четверть:",pie3)

for i in range(n):
    for j in range(n):
        if i>j and i<n-1-j:
            pie4+=list[i][j]
print("Левая четверть:",pie4)