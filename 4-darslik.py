# STR method
name='Xolid'
print('my name is '+name)
name='Xolid'
surname='IBN vALID'
print(name+' '+surname)
# f STR method
name='Xolid'
surname='Ibn Valid'
name_surname=f"{name} {surname}"
print(name_surname)
name='Jone'
surname='Uwik'
print(f"Hello,I'm {name},{surname} ")
print('Hello World')
print('Hello \tWorld')
print('Hello\n World')


price=[15000,10000,900,123,456]
total=sum(price)
print(total)

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(cars[4])

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(cars[0:3])

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(cars[3:6])

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(cars[:5])


cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(cars[3:])

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
my_cars=cars
my_cars.remove('byd')
print(my_cars)

my_cars[0]='lacetti'
print(my_cars)

cars.append('jeep')
print(my_cars)

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
my_cars=cars[:]
print(my_cars)
print(cars.remove('jeep'))