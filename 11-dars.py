## If else elif
x,y=25,50
if x>y:
    print('x>y')
else:
    print('x<Y')


son=-50
if son<0:
    print("manfiy son")
else:
    print("musbat son")

#yosh=int(input('Yoshingiz nechada?>>>'))
#if yosh<=4:
#        print('Sizga kirish tekin')
#elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
#elif yosh <= 18:
        # print('Sizga kirish 8000 so\'m')
#else:
#        print('Sizga kirish 10000 so\'m')

#yosh = int(input('Yoshingiz nechada?>>>'))
#if yosh <= 4:
 #           narx= 0
#elif yosh <= 12:
 #           narx= 5000
#elif yosh <= 18:
 #       narx = 8000
#else:
 #       narx = 10000
#print(f"Sizga kirish {narx} so'm")


#kun=input('Bugun qaysi kun>>>')
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print('Bugun dam olish kuni.')
#else:
 #   print('Bugun ish kuni.')

#kun=input("bugun nima kun?")
#harorat=float(input('Havo harorati qanday?'))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("cho'milishga ketdik")
#elif kun.lower()=='yakshanba'and harorat<30:
 #   print("uyda dam olamiz!")
#else:
 #   print('Boshqa kuni borarmiz')


#narx=15000
#choy=False
#salat=True
#if choy and salat:
 #   narx=narx+10000
#elif choy or salat:
 #   narx=narx+5000
#print(f"J ami {narx} so'm")

#
# narx=15000
# choy=False
# salat=True
# non=True
# kompot=True
# assorti=False
# if choy:
#     print("mijoz choy oldi.")
#     narx=narx+3000
# if salat:
#         print("mijoz salat oldi.")
#         narx = narx + 5000
# if non:
#      print("mijoz non oldi.")
#      narx = narx + 2000
# if kompot:
#          print("mijoz kompot oldi.")
#          narx = narx + 5000
# if assorti:
#              print("mijoz assarti oldi.")
#              narx = narx + 15000
# print(f"Jami {narx} so'm")m

# menu=['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat=input('Nima ovqat yeysiz>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print("Afsus bizda bunday ovqat yo\'q")

# menu=['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat=input('Nima ovqat yeysiz>>>')
# if ovqat.lower() not in menu:
#     print("Afsus bizda bunday ovqat yo\'q")
# else:
#     print('Buyurtma qabul qilindi.')

menu=['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar=['osh', 'somsa','manti', 'shashlik']
if buyurtmalar:
    print(f"Royxatda {len(buyurtmalar)} ta taom bor")
else:
    print("ro'yxat bosh")
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz,menuda {taom} yo'q")

