# Sikl
guests=('jone','alex', 'joseph','smith','andrew')
print('Hello',guests[0],'warm welcome')
print('Hello',guests[1],'warm welcome')
print('Hello',guests[4],'warm welcome')

guests=('jone','alex', 'joseph','smith','andrew')
for guest in guests:
    print('Hello',guest)
    print('bay bay',guest)

guests=('jone','alex', 'joseph','smith','andrew')
for guest in guests:
    print(f"dear {guest}',we invite you our wedding party which take place tomorrow morning ")
    print('looking forward','family of Ruzmetov\n')

numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
numbers=list(range(1,11))
for son in numbers:
    print(f"{son} ning kvadrati {son**2} ga teng")

numbers=[0,1,2,3,4,5,6,7,8,9,10]
numbers=list(range(11))
numbers_kvadrati=[]
for number in numbers:
    numbers_kvadrati.append(number**2)
print(numbers)
print(numbers_kvadrati)

dostlar=[]
print('5 ta yaqin dostingiz kim?')
for n in range(5):
    dostlar.append(input(f"{n+1} -dostlaringizni ismini kiriting:"))
print(dostlar)