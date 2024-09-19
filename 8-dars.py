cars= ['jeep','Byd','mersedes benz','codillact','volvo','audy']
cars.sort()
print(cars)


cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
cars.sort(reverse=True)
print(cars)

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(sorted(cars))
print(sorted(cars,reverse=True))

numbers=[2,12,3,5,-4,7,0,-3,3.5]
print(sorted(numbers))
numbers.sort(reverse=True)
print(numbers)

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
cars.reverse()
print(cars)

cars= ['jeep','byd','mersedes benz','codillact','volvo','audy']
print(len(cars))

numbers=[2,12,3,5,-4,7,0,-3,3.5]
print(len(numbers))

numbers=list(range(0,12))
print(numbers)

toq_numbers=list(range(1,15,2))
print(toq_numbers)

juft_number=list(range(0,20,2))
print(juft_number)

colculate=list(range(0,102,11))
print(colculate)

toq_numbers=[1,2,3,5,7,9,11,13,15]
max_qiymat=max(toq_numbers)
print(max_qiymat)

price=[15000,10000,900,123,456]
minimal_qiymat=min(price)
print(minimal_qiymat)

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

my_cars=cars[:]
print(my_cars)

#Tuple
toys=('lizard', 'teddy','bear', 'doll', 'mise')
print('toys[3:]')

toys=('lizard', 'teddy','bear', 'doll', 'mise')
toys=list(toys)
toys.append('Crocidile')
print(toys)
