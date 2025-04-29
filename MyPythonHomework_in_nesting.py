Navoiy = {'full_name' :'Alisher Navoiy', 'birthyear':1441, 
          'famous_work':'Xamsa', 'deathyear':1501, 
          'mashhur_asari':['Badoe ul-Bidoya', 'Navodir un-Nihoya'], 'tillar':['turkiy', 'forsiy']}
Bobur = {'full_name' :'Zahiriddin Muhammad Bobur','birthyear':1483, 
         'famous_work':'Boburnoma', 'deathyear':1526, 
         'mashhur_asari':["G'azallar"], 'tillar':['turkiy', 'forsiy']}
Amir_Temur = {'full_name' :'Amir Temur','birthyear':1336, 
              'famous_work':'Temuriylar davlati', 'deathyear':1405, 
              'mashhur_asari':['Temur tuzuklari'], 'tillar':['turkiy', 'forsiy']}
Qodiriy = {'full_name' :'Abdulla Qodiriy','birthyear':1894,
           'famous_work':'O\'tkan kunlar', 'deathyear':1938, 
           'mashhur_asari':['Mehrobdan Chayon'], 'tillar':['turkiy', "o'ris"]}
buyuk_shaxslar = [Navoiy, Bobur, Amir_Temur, Qodiriy]
for person in buyuk_shaxslar:
    print(f"{person['full_name']} {person['birthyear']}-{person['deathyear']}-yillar"
          f" oralig'ida yashagan, mashhur ishi — {person['famous_work']}. {person['tillar']} tillarini bilgan. ")
    
for shaxs in buyuk_shaxslar:
    ism = shaxs['full_name']
    asarlar = shaxs['mashhur_asari']
    print(f"{ism}ning mashhur asarlari:")
    for asar in asarlar:
        print(asar)
        
film_ixlosmandlari = {'Dadam':["Po'lat alamdar", "T-34", "Shaytanat"], 'Ayam':["Om, Shanti, Om", "Vir va Zara", "Devdas"],
                      'Davron':['Qasoskorlar', 'Birinchi qasoskor', 'Temir odam']}
                     
for kinochi, kino in film_ixlosmandlari.items():
    print(f"{kinochi}ning sevimli filmlari:")
    for movie in kino:
        print(movie, end = ', ')

davlatlar = {'AQSh':{'joylashuvi':'Shimoliy Amerika', 'Davlat tili':'Ingliz tili', 
    'pul birligi':'AQSh dollari', 'poytaxti':'Vashington'}, 
    'Yaponiya':{'joylashuvi':'Osiyo', 'Davlat tili':'yapon tili', 
    'pul birligi':'yapon iyenasi', 'poytaxti':'Tokiya'},
   'Xitoy':{'joylashuvi':'Osiyo', 'Davlat tili':'xitoy tili', 
   'pul birligi':'Xitoy yuani', 'poytaxti':'Pekin'}, 
   'Germaniya':{'joylashuvi':'Yevropa', 'Davlat tili':'nemis tili', 
   'pul birligi':'yevro', 'poytaxti':'Berlin'},
   'Rossiya':{'joylashuvi':'Osiyo, qisman Yevropa', 'Davlat tili':'rus tili', 
   'pul birligi':'Rossiya rubli', 'poytaxti':'Moskva'}
   }
for davlat, info in davlatlar.items():
    print(f"{davlat} {info['joylashuvi']}da joylashgan, "
  f" poytaxti {info['poytaxti']} shahri, davlat tili — {info['Davlat tili']}, ", 
  f" pul birligi — {info['pul birligi']}")
    
country = input('Birorta davlat kiriting\n>>>')
country = country.title()
if country in davlatlar.keys():
    davlat = country
    print(davlatlar[davlat])
    
else:
    print(f'Uzr, bizda {country.title()} haqida ma\'lumot yo\'q ')
    
    
               

        


