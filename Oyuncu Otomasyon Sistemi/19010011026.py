#19010011026 uğur DÜLGER

A_list = []
Son_Id = 100
Id = 100
Dosya = open("19010011026.txt","a")
Dosya.close()

def Oyuncu_Ekle():
    global Id
    global A_list
    global Dosya

    def SonIdBul():
        global Id
        global Son_Id
        global Dosya
        kontol = []
        with open("19010011026.txt","r+") as Dosya:
            U = Dosya.readlines()
            for C in U:
                D = C.split(" ")
                K = D[0]
                Son_Id = int(K)
                kontol.append(Son_Id)
                Son_Id = Son_Id + 1
        Id = Son_Id
        for i in range(len(kontol)):
            if i != len(kontol) - 1:
                u = kontol[i]
                c = kontol[i+1]
                d = c - u
                if d > 1:
                    Id = kontol[x]+1
        if kontol[0] != 100:
             Id =100

    with open("19010011026.txt", "r") as Dosya:
        x = Dosya.readlines()
        for a in x:
            if a != "":
                SonIdBul()
    print("-"*80)
    Oyuncu_Adi = input("Oyuncu Adını Giriniz :")
    Oyun_Adi = input("Oyun Adını Giriniz :")
    Harcanan_Para = input("Oyunda Harcanan Parayı Giriniz :")
    Harcanan_Sure= input("Oyunda Harcanan Süreyi Giriniz :")
    print("-"*80)

    A_list.append(Id)
    A_list.append(Oyuncu_Adi)
    A_list.append(Oyun_Adi)
    A_list.append(Harcanan_Para)
    A_list.append(Harcanan_Sure)

    with open("19010011026.txt", "a") as Dosya:
        for A in A_list:
            Dosya.writelines("{} ".format(A))
        Dosya.writelines("\n")

    A_list.clear()

    def Id_Sirala():

        global Dosya
        IdSirala_List = []
        Ind = 0
        with open("19010011026.txt", "r") as Dosya:
            A = Dosya.readlines()
            for B in A:
                if B != "":
                    C = B.split(" ")
                    IdSirala_List.append(list())
                for x in range(len(C)):
                    if x != 5:
                        IdSirala_List[Ind].append(C[x])
                Ind = Ind + 1
        IdSirala_List.sort()
        with open("19010011026.txt", "w") as Dosya:
            for A in IdSirala_List:
                for B in range(len(A)):
                    Dosya.writelines("{} ".format(A[B]))
                Dosya.writelines("\n")
    Id_Sirala()


def Oyuncu_Guncelle():

    global Dosya
    Guncel_list = []
    print("-" * 80)
    Guncel_Id = input("Güncellemek İstediğiniz İd'yi Giriniz : ")
    Oyuncu_Adi = input("Yeni Oyuncu Adını Giriniz :")
    Oyun_Adi = input("Yeni Oyun Adını Giriniz :")
    Harcanan_Para = input("Yeni Oyunda Harcanan Parayı Giriniz :")
    Harcanan_Sure= input("Yeni Oyunda Harcanan Süreyi Giriniz :")
    print("-" * 80)

    G_list = []
    G_list.append(Guncel_Id)
    G_list.append(Oyuncu_Adi)
    G_list.append(Oyun_Adi)
    G_list.append(Harcanan_Para)
    G_list.append(Harcanan_Sure)
    def DosyaOku(G_list,Guncel_list):
        global Dosya
        ind = 0
        with open("19010011026.txt","r+") as Dosya:
            Oyuncular = Dosya.readlines()
            for i in Oyuncular:
                if i != "":
                    A = i.split(" ")
                    Guncel_list.append(list())
                for j in range(len(A)):
                    if j != 5 :
                        Guncel_list[ind].append(A[j])
                ind += 1
        for k in range(len(Guncel_list)):
            if G_list[0] == Guncel_list[k][0]:
                Guncel_list[k]= G_list
        with open("19010011026.txt","w") as Dosya:
            for i in Guncel_list:
                for j in range(len(i)):
                    Dosya.writelines("{} ".format(i[j]))
                Dosya.writelines("\n")
    DosyaOku(G_list,Guncel_list)
    G_list.clear()
    Guncel_list.clear()

def Oyuncu_Ara():
    global Dosya
    Gecici_liste = []
    ind = 0
    with open("19010011026.txt","r") as Dosya:
        oyuncular  = Dosya.readlines()
        for i in oyuncular:
            if i != "":
                gecici = i.split(" ")
                Gecici_liste.append(list())
            for j in range(len(gecici)):
                if j != 5:
                    Gecici_liste[ind].append(gecici[j])
            ind += 1
    knrtl =0
    while knrtl ==0:
        print("-" * 80)
        aranacak_id = input("Aramak İstediğiniz Oyuncunun Id'sini Giriniz : ")
        print("-" * 80)
        sart = 0

        for i in range(len(Gecici_liste)):
             if aranacak_id == Gecici_liste[i][0]:
                print("-" * 80)
                print("Oyuncu Id = {}\nOyunucu Adı = {}\nOyunu = {}\nHarcanan Para = {}\nHarcanan Süre = {}".format(Gecici_liste[i][0],Gecici_liste[i][1],Gecici_liste[i][2],Gecici_liste[i][3],Gecici_liste[i][4]))
                print("-" * 80)
                sart += 1
                knrtl +=1


        if sart == 0:
            print("-"*80)
            print("Aradığınız Id'de Oyuncu Bulunmadı")
            print("-" * 80)
            continue

    Gecici_liste.clear()

def Oyuncu_Sil():
    global Dosya
    silinecek_Id = input("Silmek İstediğiniz Oyuncun Id'sini Giriniz : ")
    sil_list = []
    ind = 0

    with open("19010011026.txt","r+") as Dosya:
        oyuncular = Dosya.readlines()
        for i in oyuncular:
            if i != "":
                C = i.split(" ")
                sil_list.append(list())
            for j in range(len(C)):
                if j != 5 :
                    sil_list[ind].append(C[j])
            ind += 1
    indis = 0

    for i in sil_list:
        if i[0] == silinecek_Id:
            del(sil_list[indis])
        indis +=1
    with open("19010011026.txt","w") as Dosya:
        for i in sil_list:
            for j in range(len(i)):
                Dosya.writelines("{} " .format(i[j]))
            Dosya.writelines("\n")
def Oyunculari_Listele():
    global Dosya
    with open("19010011026.txt","r") as Dosya:
        oyuncular = Dosya.readlines()
    oyuncudict = dict()
    for i in oyuncular:
        oyuncu_bilgi = i.split(" ")
        tempdict = dict()

        tempdict["Oyuncu Adı ->"] = oyuncu_bilgi[1]
        tempdict["Oyun Adı ->"] = oyuncu_bilgi[2]
        tempdict["Harcanan süre ->"] = int(oyuncu_bilgi[3])
        tempdict["Harcanan Para ->"] = int(oyuncu_bilgi[4])

        oyuncudict[int(oyuncu_bilgi[0])] = tempdict
    print("-" * 80)
    print(oyuncudict)
    print("-" * 80)

def Saat_Basi_Harcama():
    global Dosya
    HarcananPara = []
    HarcananSaat = []

    with open("19010011026.txt","r") as Dosya:
        oyuncular = Dosya.readlines()
        for i in oyuncular:
            if i != "":
                C = i.split(" ")
                H1 = C[4].replace("\n","")
                H2 = C[3].replace("\n","")
                HarcananPara.append(H1)
                HarcananSaat.append(H2)

    SaatBasıHarcama =[]
    ind = 0
    for i in range(len(HarcananPara)):
        harcama = int(HarcananSaat[ind])/int(HarcananPara[ind])
        SaatBasıHarcama.append(harcama)
        ind +=1
    print("-"*80)
    for j in range(len(HarcananPara)):
        print("{}. Oyuncun Saat Başı Harcaması --> {}".format(j+1,str(round(SaatBasıHarcama[j],2))))
    print("-"*80)


def Menu():
    print("--Oyuncu Kayıt Otomasyonuna Hoşgeldiniz-- ")
    Menusart = 0
    while Menusart == 0:
        print("--------- MENU ----------","1 --> Oyuncu Ekle","2 --> Oyuncu Guncelle","3 --> Oyuncu Listele","4 --> Oyuncu Sil","5 --> Oyuncu Ara","6 --> Saat Başı Harcama Hesapla","7 --> Cikis", sep="\n")
        print("-" * 80)
        Menusecim = int(input("Lütfen Yapmak İstediğiniz İşlemin Nurmarasını Giriniz -> "))
        print("-" * 80)
        if Menusecim == 1:
            Oyuncu_Ekle()
        elif Menusecim == 2:
            Oyuncu_Guncelle()
        elif Menusecim == 3 :
            Oyunculari_Listele()
        elif Menusecim == 4 :
            Oyuncu_Sil()
        elif Menusecim == 5 :
            Oyuncu_Ara()
        elif Menusecim == 6:
            Saat_Basi_Harcama()
        elif Menusecim == 7:
            print("-" * 80)
            print(">> Cikisiniz Yapılmıstır>>")
            print("-" * 80)
            Menusart +=1
        else:
            print("-"*30)
            print(">> Yanlış Numara Girdiniz >>")
            print("-"*30)
Menu()
