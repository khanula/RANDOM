# 1 2 4 8 ...
sum=0
for i in range(0,64):
    sum+=2**i
print('Suma wszystkich ziaren na szachownicy: ', sum)

#założenia
tons = (sum*0.0004)/1000/1000
print('Ton:' ,tons)