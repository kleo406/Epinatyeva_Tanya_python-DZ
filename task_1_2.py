# Задача 2 а)
count=list(range(1,1000,2))
count_1=[]
for i in count:
    count_1.append(i**3)
# print(count_1)
count_2=[]
for i in count_1:
    count_2.append((i//100000000)+(i//10000000%10)+(i//1000000%10)+(i//100000%10)+(i//10000%10)+(i//1000%10)+(i//100%10)+(i//10%10)+(i%10))
# print(count_2)
count_3=[]
for i in count_2:
    if i%7==0:
        count_3.append(i)
# print(count_3)
print(sum(count_3))

# Задача 2 б)
count=list(range(1,1000,2))
count_1=[]
for i in count:
    count_1.append(i**3)
# print(count_1)
count_2=[]
for i in count_1:
    count_2.append(i+17)
# print(count_2)
count_3=[]
for i in count_2:
    count_3.append((i//100000000)+(i//10000000%10)+(i//1000000%10)+(i//100000%10)+(i//10000%10)+(i//1000%10)+(i//100%10)+(i//10%10)+(i%10))
# print(count_3)
count_4=[]
for i in count_3:
    if i%7==0:
        count_4.append(i)
# print(count_4)
print(sum(count_4))
