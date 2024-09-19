from bisect import insort
from os import remove

a=20
b=5.5
temp=36.6
numer_people=7_594_345_234
print("nume_people:",numer_people)
x,y,z=10, 5.5, -5
c=a*b
print('c')
radius=20
PI=3.1459
diametr=2*radius
print('Aylana uzunligi',PI*diametr)
name='Alex'
age=25
information=name+ ' ' + str(age) +'yoshda'
print(information)
#b_data=int(input('Enter your birthdata'))
#age=2024-b_data
print('You are',age, 'your age')
a=('10')
b=float('10')
temp=str(36.6)
print(type(a))
radius=10
name='Alex'
mevalar=['apple', 'oreng','peach']
price=[12000,18000,22000]
print(price)
numers=['one', 'two',3,4,5]
print(numers)
print(mevalar[0])
print(mevalar[1])
print(mevalar[2])
print(mevalar[-1])
print(mevalar[-2].upper())
print(mevalar[-3].lower())
print(mevalar[2].title())
print(price[2])
print(mevalar)
mevalar[0]='pomegranate'
print(mevalar)
mevalar[-1]='Cherry'
print(mevalar)
mevalar.append('Wotermelon')
print(mevalar)
mevalar.insert(0,'banana')
print(mevalar)
mevalar.insert(3,'Melon')
print(mevalar)
cars=[]
cars.append('locetti')
cars.append('Nexia')
cars.append('Cobalt')
print(cars)
del cars[1]
print(cars)
cars.insert(1,'Nexia')
print(cars)
del cars[2]
print(cars)
print(cars)
print("oxirgi:")
print(cars)
# yangi royxat animals
animals=['dog','fox','crocodile','cat','dog']
animals.remove('dog')
print(animals)
dailyproducts=[ 'meal', 'flour', 'banana', 'oil']
#products=dailyproducts.pop(1)
#print(products)
#print(dailyproducts)
products=dailyproducts.pop()
print(dailyproducts)
price=[12000,18000,22000]
price.remove(18000)
print(price)
price=[12000,18000,22000]
price[0]=price[0]+8000
print(price)

