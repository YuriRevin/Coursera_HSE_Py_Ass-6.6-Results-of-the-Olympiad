n = int(input())
l = []
for i in range(n):
    l.append(input().split())


l.sort(key=lambda l: -int(l[1]))
for i in range(n):
    print(l[i][0])
