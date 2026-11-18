# Elektron ariza tizimi (L9 Laboratoriya - 20-variant uchun dastlabki kod)

ARIZALAR = []
MIN_MATN_UZUNLIGI = 5

def ariza_yaratish(f_ism, f_tel, m_matn, t_turi):
    # Yomon nomlangan parametrlar (Naming issue) va takroriy tekshiruvlar
    x = 100
    y = "unused_var"
    if f_ism == None or f_ism == "":
        print("Xato: Ism kiritilmadi")
        return False
    if f_tel == None or f_tel == "":
        print("Xato: Telefon kiritilmadi")
        return False
    if m_matn == None or len(m_matn) < MIN_MATN_UZUNLIGI:
        print("Xato: Ariza matni juda qisqa")
        return False

    yangi_id = len(ARIZALAR) + 1
    ariza = {
        "id": yangi_id,
        "ism": f_ism,
        "tel": f_tel,
        "matn": m_matn,
        "turi": t_turi,
        "holat": "Yangi"
    }
    ARIZALAR.append(ariza)
    print("Ariza saqlandi:", yangi_id)
    return True

def ariza_tahrirlash(a_id, f_ism, f_tel, m_matn):
    # Duplicate Code: yuqoridagi tekshiruvlar aynan takrorlangan
    if f_ism == None or f_ism == "":
        print("Xato: Ism kiritilmadi")
        return False
    if f_tel == None or f_tel == "":
        print("Xato: Telefon kiritilmadi")
        return False
    if m_matn == None or len(m_matn) < MIN_MATN_UZUNLIGI:
        print("Xato: Ariza matni juda qisqa")
        return False

    for a in ARIZALAR:
        if a["id"] == a_id:
            a["ism"] = f_ism
            a["tel"] = f_tel
            a["matn"] = m_matn
            print("Ariza yangilandi:", a_id)
            return True
    return False

def holatni_yangilash(a_id, h):
    if h == "Yangi":
        for a in ARIZALAR:
            if a["id"] == a_id:
                a["holat"] = "Yangi"
                return True
    else:
        if h == "Ko'rilmoqda":
            for a in ARIZALAR:
                if a["id"] == a_id:
                    a["holat"] = "Ko'rilmoqda"
                    return True
        else:
            if h == "Yakunlandi":
                for a in ARIZALAR:
                    if a["id"] == a_id:
                        a["holat"] = "Yakunlandi"
                        return True
    return False

def arizalarni_korish():
    for i in range(len(ARIZALAR)):
        print(ARIZALAR[i]["id"], "-", ARIZALAR[i]["ism"], "-", ARIZALAR[i]["holat"])
