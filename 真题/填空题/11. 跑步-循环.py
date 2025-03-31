days = [31,28,31,30,31,30,31,31,30,31,30,31]

cnt = 0
w = 6
for month in range(12):
    for day in range(1,days[month]):
        if w == 6 or w == 0:
            cnt += 1
        elif day%10 == 1:
            cnt += 1
        w = (w+1)%7

print(cnt)