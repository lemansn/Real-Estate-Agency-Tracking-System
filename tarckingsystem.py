ASGARI_UCRET = 2324.70
IYI_KIRA_SAY = 10
IYI_KIRA_BEDELI = 25000
KOMISYON_CARPANI = 0.04
PRIM_CARPANI = 0.1
top_konut_bedel = top_arsa_bedel = top_is_yer_bedel = 0             #Tüm danışmanlar için satiışını gerçekleştirdiği konut/arsa/iş yeri toplam bedeli için ayarlanmıştır
top_konut_satilan = top_arsa_satilan = top_isyeri_satilan = 0       #Tüm danışmanlar için satiışını gerçekleştirdiği konut/arsa/iş yeri toplam sayı için ayarlanmıştır
MAX_DANISMAN = MAX_DANISMAN_MAAS = MAX_PRIM = MAX_TOP_UCRET = 0     #En çok prim alan danışman bilgileri için ayarlanmıştır
MIN_DANISMAN = MIN_DANISMAN_MAAS = MIN_PRIM = MIN_TOP_UCRET = 0     #En az prim alan danışman  bilgileri için ayarlanmıştır
top_kira_konut = top_kira_arsa = top_isyer_kira = 0                 #Tüm danışmanlar için kirasını gerçekleştirdiği konut/arsa/iş yeri toplam sayı için ayarlanmıştır
asgariden_buyuk_kira = 0                                            #Kirası Aylık Net Asgari Ücretden çok olan konut sayı için ayarlanmıştır
MAX_SATIS_SAY = MAX_ISIM = MAX_SATILAN_BEDEL = 0                    #Satış adeti olarak en çok satış yapan danışman bilgileri için ayarlanmıştır
MAX_BEDEL = MAX_TIP = MAX_ISIM_SATIS = 0                            #En yüksek bedelle satılan konut tipli emlak için ayarlanmıştır
maasdan_cok_prim = 0                                                #Primi maaşından çok olan danışman sayını bulmak için ayarlanmıştır
iyi_danisman = 0
aylik_top_ucret = 0
top_komisyon = 0
kota_dolduran = 0
top_ucret = 0
satis_yapmayan_danisman  = 0
MAX_BEDEL_DANISMAN = MAX_BEDEL_SAY = MAX_BEDEL_SATIS = 0            #Satış bedeli olarak en çok satış yapan danışman bilgileri için ayarlanmıştır
MAX_TOP_KIRA_KONUT  = MAX_KONUT_KIRALAYAN = 0                       #En yüksek bedelle kiralan konut bilgileri için ayarlanmıştır

danisman_say = int(input('Acenteye bağlı olarak çalışan emlak danışmanı sayısı: '))
while danisman_say <= 0:
    danisman_say = int(input('Hatalı veri, lütfen tekrar giriniz: '))

for say in range (1,danisman_say+1):
    isim = input('Lütfen ad ve soyadı giriniz: ')
    maas = float(input('Danışmanın aylık net maaşı ne kadardır?(TL): '))
    while maas < ASGARI_UCRET:
        maas = float(input('Maaş asgari ücretden küçük olamaz,lütfen bir daha deneyiniz: '))

    kota = float(input('Danışmanın 1 aylık kotası ne kadardır?(TL): '))
    while kota < 10 * maas:
        kota = float(input('Kota maaşın 10 katı ve daha büyük olmalıdır, lütfen tekrar giriniz: '))

    satis_yapmayan = True
    MAX_KIRA_KONUT = 0                #Her danışmanın  kiraladığı konutların en büyük bedeli için ayarlanmıştır.
    satilan = 0                       #Toplam satılan emlak
    kiralanan = 0                     #Toplam kiralanan emlak
    konut_satis_bedel = 0             #Her danışman için satiışını gerçekleştirdiği konut toplam bedeli için ayarlanmıştır
    arsa_satis_bedel = 0              #Her danışman için satiışını gerçekleştirdiği arsa toplam bedeli için ayarlanmıştır
    is_yeri_satis_bedel = 0           #Her danışman için satiışını gerçekleştirdiği iş yeri toplam bedeli için ayarlanmıştır
    konut_kira = 0                    #Her danışmanın kiraladığı konut sayı için ayarlanmıştır
    konut_kira_bedel = 0              #Her danışmanın kiraladığı konut bedeli için ayarlanmıştır
    kira_bedel = 0                    #Her danışmanın gerçekleştirdiği toplam kira bedeli için ayarlanmıştır
    isyeri_kira = 0                   #Her danışmanın kiraladığı işyeri sayı için ayarlanmıştır
    konut = 0                         #Her danışmanın sattığı toplam konut sayı için ayarlanmıştır
    is_yeri = 0                       #Her danışmanın sattığı toplam iş yeri sayı için ayarlanmıştır
    arsa = 0                          #Her danışmanın sattığı toplam arsa sayı için ayarlanmıştır
    arsa_kira = 0                     #Her danışmanın kiraladığı arsa sayı için ayarlanmıştır
    top_bedel = 0                     #Her danışmanın sattığı tüm emlakların bedeli için ayarlanmıştır
    komisyon = 0                      #yapılan her satış için satış bedelinin %4’ü kadar, her kiralama için 1 aylık kira bedeli kadar kazandığı ücreti ifade etmektedir

    devam = 'e'
    while devam == 'e' or devam == 'E':
        tip = input('Bu ay sattığı ya da kiraladığı emlak tipini giriniz(Konut,İş yeri,Arsa (K/k/İ/i/A/a)): ')
        while tip not in ['K','k','A','a','i','i']:
            tip = input('Hatalı veri, lütfen tekrar giriniz: ')

        tur =input('Bu emlakın işlem türünü giriniz(Satış, Kiralama (S/s/K/k)): ')
        while tur not in ['S','s','K','k']:
            tur = input('Hatalı veri, lütfen tekrar giriniz: ')

        bedel = float(input('Satış veya kira işlemi yaptığı emlakın bedeli(TL): '))
        while bedel <= 0:
            bedel = float(input('Hatalı veri, lütfen tekrar giriniz: '))

        devam = input('Sattığı veya kiraladığı başka emlak var mı?(E/e/H/h): ')
        while devam not in ['E','e','H','h']:
            devam = input('Hatalı veri, lütfen tekrar giriniz: ')
        print('------------------------')

        if tip in ['K','k']: #verileri girerken emlak tiplerinin ilk harfleri yazılacağı icin çıktı zamanı görsellik açısından stringlere dönüştürdüm
            emlak_adi = 'Konut'
        elif tip in ['A','a']:
            emlak_adi = 'Arsa'
        else:
            emlak_adi = 'Iş yeri'

        if tur in ['S','s']: #Her emlak tipi için satış sayı,satış bedeli,MİN/MAX bulma
            satis_yapmayan = False
            if tip in ['k','K']:
                konut_satis_bedel += bedel
                konut += 1
            elif tip in ['A','a']:
                arsa_satis_bedel += bedel
                arsa += 1
            else:
                is_yeri_satis_bedel += bedel
                is_yeri += 1

            if bedel > MAX_BEDEL:
                MAX_BEDEL = bedel
                MAX_TIP = emlak_adi
                MAX_ISIM_SATIS = isim

            satilan += 1
            top_bedel += bedel

        else:   #Her emlak tipi için kiralananların sayı,kira bedeli,MİN/MAX bulma
            kira_bedel += bedel
            kiralanan += 1
            if tip in ['k','K']:
                konut_kira += 1
                konut_kira_bedel += bedel

                if bedel > ASGARI_UCRET:  #kira bedeli aylık asgari ücretden fazla olan konut sayı
                    asgariden_buyuk_kira += 1

              #Her danışman için en yüksek bedelle kiraladığı konutun kira bedeli
                if bedel > MAX_KIRA_KONUT:
                    MAX_KIRA_KONUT = bedel

               #Tüm danışmanlar arasında en yüksek bedelle kiralanan konutun bedeli ve danışmanın adı
                if bedel > MAX_TOP_KIRA_KONUT:
                    MAX_TOP_KIRA_KONUT = bedel
                    MAX_KONUT_KIRALAYAN = isim

            elif tip in ['A','a']:
                arsa_kira += 1
            else:
                isyeri_kira +=1

        # Satış adedi olarak en çok satış yapmış danışman bilgileri
        if satilan > MAX_SATIS_SAY:
            MAX_SATIS_SAY = satilan
            MAX_ISIM = isim
            MAX_SATILAN_BEDEL = top_bedel

        # Toplam satış bedeli olarak en çok satış yapan danışman bilgileri
        if top_bedel > MAX_BEDEL_SATIS:
            MAX_BEDEL_SATIS = top_bedel
            MAX_BEDEL_DANISMAN = isim
            MAX_BEDEL_SAY = satilan

    if satis_yapmayan:  #Bu ay hiç satış yapmayan danışman sayı
        satis_yapmayan_danisman += 1

    top_konut_satilan += konut
    top_arsa_satilan += arsa
    top_isyeri_satilan += is_yeri
    top_konut_bedel += konut_satis_bedel
    top_arsa_bedel += arsa_satis_bedel
    top_is_yer_bedel += is_yeri_satis_bedel
    top_kira_konut += konut_kira
    top_kira_arsa += arsa_kira
    top_isyer_kira += isyeri_kira

    komisyon = (konut_satis_bedel + arsa_satis_bedel + is_yeri_satis_bedel) * KOMISYON_CARPANI + kira_bedel
    prim = komisyon * PRIM_CARPANI

    #primi maaşından çok olan danışman sayı
    if prim > maas:
        maasdan_cok_prim += 1

    #en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı
    if kiralanan >= IYI_KIRA_SAY or kira_bedel >= IYI_KIRA_BEDELI:
        iyi_danisman += 1

    #Aylık net ücretin hesaplanması
    if komisyon >= kota:
        kota_dolduran += 1
        aylik_net_ucret = maas + prim + ASGARI_UCRET / 2
    else:
        aylik_net_ucret = maas + prim

    if say == 1:  #Girilen ilk primi MİN ve MAX olarak ayarladım
        MAX_PRIM = MIN_PRIM = prim

    #En çok prim alan danışman bilgileri
    if prim >= MAX_PRIM:
        MAX_PRIM = prim
        MAX_DANISMAN = isim
        MAX_DANISMAN_MAAS = maas
        MAX_TOP_UCRET = aylik_net_ucret

    # En az prim alan danışman bilgileri
    if prim <= MIN_PRIM:
        MIN_PRIM = prim
        MIN_DANISMAN = isim
        MIN_DANISMAN_MAAS = maas
        MIN_TOP_UCRET = aylik_net_ucret

    top_ucret += aylik_net_ucret  #tüm satış danışmanlarına ödenecek toplam ücretlerin toplamı
    top_komisyon += komisyon      #acentenin kazandığı toplam komisyon

    print('Danışmanın ismi ve soyismi: ',isim)
    print('Sattığı emlak adedi: ',satilan,'oranı: ','%',format(satilan*100/(satilan+kiralanan),',.2f'),
          'Kiraladığı emlak adedi: ',kiralanan,'oranı: ','%',format(kiralanan*100/(satilan+kiralanan),',.2f'))
    print('Sattığı konutların toplam bedeli: ',format(konut_satis_bedel,',.2f'),'TL',
          'Sattığı arsaların toplam bedeli: ',format(arsa_satis_bedel,',.2f'),'TL',
          'Sattığı iş yerlerinin toplam bedeli: ',format(is_yeri_satis_bedel,',.2f'),'TL')
    print('Kiraladığı konutların ortalama kira bedeli (TL): ',format(konut_kira_bedel/konut_kira,',.2f'),'TL')
    print('En yüksek bedelle kiraladığı konutun kira bedeli: ',format(MAX_KIRA_KONUT,',.2f'),'TL')
    print('Aldigi maas: ',format(maas,',.2f'),'TL')
    print('Bu ay aldigi prim: ',format(komisyon * 0.1,',.2f'),'TL')
    print('Bu ay ki kotasi: ',format(kota,',.2f'),'TL')
    print('Bu ay acenteye kazandırdığı toplam komisyon tutarı: ',format(komisyon,',.2f'),'TL')
    if komisyon >= kota:
        print(isim,'bu ay kotasını doldurmuştur.')
        print('Bu ay ki kotasını doldurduğu için alacağı ikramiye: ',format(ASGARI_UCRET/2,',.2f'),'TL')
    else:
        print(isim,'bu ay kotasını doldurmamıştır.')
    print('Bu ay alacağı toplam ücret: ',format(aylik_net_ucret,',.2f'),'TL')
    print('--------------------------')

print('Bu ay atılan komut sayısı:',top_konut_satilan, 'Kiralanan komut sayısı:',top_kira_konut,'Satılma oranı:','%',format(top_konut_satilan*100/(top_konut_satilan+top_kira_konut),',.2f'),'\n'
      'Bu ay satılan arsa sayısı:',top_arsa_satilan, 'Kiralanan arsa sayısı:',top_kira_arsa,'Satılma oranı:','%',format(top_arsa_satilan*100/(top_arsa_satilan + top_kira_arsa),',.2f'),'\n'
      'Bu ay satılan iş yeri sayısı:',top_isyeri_satilan, 'Kiralanan iş yeri sayısı:',top_isyer_kira, 'Satılma oranı:','%',format(top_isyeri_satilan*100/(top_isyeri_satilan + top_isyer_kira),',.2f'))

print('Bu ay satılan komut tipli emlakın satış bedellerinin toplamı:',format(top_konut_bedel,',.2f'),'TL', 've ortalamsı:',format(top_konut_bedel/top_konut_satilan,',.2f'),'TL','\n'
      'Bu ay satılan arsa tipli emlakın satış bedellerinin toplamı:',format(top_arsa_bedel,',.2f'),'TL','ve ortalamsı:',format(top_arsa_bedel/top_arsa_satilan,',.2f'),'TL','\n'
      'Bu ay satılan iş yeri tipli emlakın satış bedellerinin toplamı:',format(top_is_yer_bedel,',.2f'),'TL','ve ortalamsı:',format(top_is_yer_bedel/top_isyeri_satilan,',.2f'),'TL')

print('Bu ay en yüksek bedelle satılan emlak tipi:',MAX_TIP,'ve değeri:',format(MAX_BEDEL,',.2f'),'TL','Bu satışı gerçekleştiren danışman:',MAX_ISIM_SATIS)

print('Bu ay en yüksek bedelle kiralanan konutun bedeli:',format(MAX_TOP_KIRA_KONUT,',.2f'),'TL','Bu kiranı gerçekleştıren danışman:',MAX_KONUT_KIRALAYAN)

print('Bu ay kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı:',asgariden_buyuk_kira,'Kiralanan konutlar içindeki oranı:','%',format(asgariden_buyuk_kira*100/top_kira_konut,',.2f'))

print('Bu ay hiç satış yapamayan danışmanların sayısı:',satis_yapmayan_danisman,'Tüm danışmanlar içindeki oranı:','%',format(satis_yapmayan_danisman*100/danisman_say,',.2f'))

print('Bu ay satış adeti olarak en çok satış yapan danışmalın adı-soyadı:',MAX_ISIM,'sattıgı emlak sayıları:',MAX_SATIS_SAY,'Toplam bedeli:', format(MAX_SATILAN_BEDEL,',.2f'),'TL','\n'
      'Bu ay satış bedeli olarak en çok satış yapan danışmanın adı-soyadı:',MAX_BEDEL_DANISMAN,'Sattıklarının toplam satış bedelleri:',format(MAX_BEDEL_SATIS,',.2f'),'TL','Toplam sayi:',MAX_BEDEL_SAY)

print('Bu ay kotasını dolduran danışmanların sayısı:',kota_dolduran, 'Tüm danışmanlar içindeki oranı:','%',format(kota_dolduran*100/danisman_say,',.2f'))

print('BU ay primi maaşından yüksek olan danışmanların sayısı:',maasdan_cok_prim,'Tüm danışmanlar içindeki oranı:','%',format(maasdan_cok_prim*100/danisman_say,',.2f'))

print('Bu ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:',iyi_danisman)

print('Bu ay en yüksek prim alan danışman:',MAX_DANISMAN,'\n'
      ' - maaşı:',format(MAX_DANISMAN_MAAS,',.2f'),'TL','\n'
      ' - primi:',format(MAX_PRIM,',.2f'),'TL','\n'
      ' - aylık toplam ücreti:',format(MAX_TOP_UCRET,',.2f'),'TL','\n'
      'Bu ay en düşük prim alan danışman:',MIN_DANISMAN,'\n'
      ' - maaşı:',format(MIN_DANISMAN_MAAS,',.2f'),'TL','\n'                              
      ' - primi:',format(MIN_PRIM,',.2f'),'TL','\n'
      ' - aylık toplam ücreti:',format(MIN_TOP_UCRET,',.2f'),'TL')
print('Bu ay tüm satış danışmanlarına ödenecek toplam ücretlerin toplamı:',format(top_ucret,',.2f'),'TL', 'Ortalaması:',format(top_ucret/danisman_say,',.2f'),'TL')

print('Bu ay acentenin kazandığı toplam komisyon:',format(top_komisyon,',.2f'),'TL')
