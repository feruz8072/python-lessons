# Dictionary
from os import PathLike

car_0={'model':'ferrari','rangi':'qizil'}
print(car_0['model'])
print(car_0['rangi'])

en_uz={'apple':'olma','apricot':'Orik','banana':'banan'}
print(en_uz['apple'])
print(en_uz['apricot'])
print(en_uz['banana'])

mevalar={'olma':'10000','tarvuz':'8000','qovun':'15000'}
print(f"olma narxi {mevalar['olma']} so'm")
# print(mevalar['olma'])
# print(mevalar['tarvuz'])
# print(mevalar['qovun'])

# talaba_0={'ism':'Murod olimov','yosh':'20','t_yil':'2000'}
# print(f" {talaba_0['ism'].title()},\
#       {talaba_0['t_yil']}-yilda tugilgan, \
#     {talaba_0['yosh']} yoshda")
# print(talaba_0)

# # yangi kalit soz qoshish
# talaba_0['kurs']=4
# talaba_0['fakultet']='informatika'
# talaba_0['ism']='Ali'
# print(talaba_0)

# bosh lugat
talaba_1={}
talaba_1['ism']='Jobir'
talaba_1['kurs']=3
talaba_1['yosh']=20
print(talaba_1)
print(f"Talaba {talaba_1 ['ism'].title()} {talaba_1 ['kurs']}-kurs")

#qiymat tanlash
talaba_1['kurs']=4
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_0={'ism':'Murod olimov','yosh':'20','t_yil':'2000'}
del talaba_0['yosh']
print(talaba_0)


en_uz={'apple':'olma','apricot':'Orik','banana':'banan'}
del en_uz['banana']
print(en_uz)

telefonlar={ 'ali':'apple','vali':'nokia',
            'jalil':'samsung'}
del telefonlar['vali']
print(telefonlar)
print(telefonlar['jalil'])


# Get method
phone=telefonlar['ali']
print(f"Alining telfoni {phone}")
phone=telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)




