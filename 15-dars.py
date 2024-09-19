# lugatlar bn ishlash
from tkinter import PanedWindow

talaba_0={'ism':'alijon','familya':'shamsiyev',
          'yosh':22,'fakultet':'matematika',
          'kurs':4}
print(talaba_0['ism'])
print(talaba_0.items())
for kalit,qiymat in talaba_0.items():
    print(f"kalit:{kalit}")
    print(f"Qiymat:{qiymat}\n")

telefonlar={'ali':'iphonex',
            'vali':'galaxy s10',
            'olim':'mi 10 pro',
           'orif':'nokia' }
for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

    # keys method
mahsulotlar={
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'shaftoli':30000}
print(mahsulotlar.keys())
print('dokondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik=['anor','uzum','non','baliq']
for mahsulot in  mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f" Iltimos dokoningizga {buyum } ham olib keling")

        #lugat elementlarini tartib bilan chiqarish
print("dikondagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

print('Foydaluvchilar quidagi telefon ishlatishadi:')
for tel in telefonlar.values():
    print(tel.title())


print('Foydaluvchilar quidagi telefon ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel.title())

# set funksiyasi
toys={ 'ball','cars','lamp','ball','ship','cars'}
print(toys)
