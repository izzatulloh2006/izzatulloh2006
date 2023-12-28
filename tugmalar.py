from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def xizmatlar_button():
    n1 = KeyboardButton(text="🔧 XIZMATLAR")
    n2 = KeyboardButton(text="📞 TELEFON")
    n3 = KeyboardButton(text="🗓 ISH JADVALI")

    design = [
        [n1, n2],
        [n3]
    ]

    tkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return tkm

def tel_num():
    n1 = KeyboardButton(text="TELEFON  ☎️ RAQAM")
    n2 = KeyboardButton(text="TELEGRAM AKAUNT")
    n3 = KeyboardButton(text="LAKATSIYA 📍")
    n4 = KeyboardButton(text="🔙 ORQAGA QAYTISH")
    design1 = [
        [n1 , n2],
        [n3 , n4]
    ]
    tkm2 = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True, one_time_keyboard=True)
    return tkm2


def xizmatlar1():
    n1 = KeyboardButton(text="JIGULI 011")
    n2 = KeyboardButton(text="JIGULI 06")
    n3 = KeyboardButton(text="JIGULI 07")
    n4 = KeyboardButton(text="MATIZ 3 tali")
    n5 = KeyboardButton(text="MATIZ Best")
    n6 = KeyboardButton(text="MATIZ Evro")
    n7 = KeyboardButton(text="MATIZ Avtomat")
    n8 = KeyboardButton(text="SPARK 1.25")
    n9 = KeyboardButton(text="SPARK /  MEHANIKA")
    n10 = KeyboardButton(text="SPARK / AVTOMART")
    n11 = KeyboardButton(text="NEXIA 1")
    n12 = KeyboardButton(text="NEXIA 2")
    n13 = KeyboardButton(text="NEXIA 3")
    n14 = KeyboardButton(text="DAMAS")
    n15 = KeyboardButton(text="LABO")
    n16 = KeyboardButton(text="KOBALT")
    n17 = KeyboardButton(text="LASETTI 1.8")
    n18 = KeyboardButton(text="JENTRA 1.5")
    n19 = KeyboardButton(text="KAPTIVA")
    n20 = KeyboardButton(text="MALIBU")
    n21 = KeyboardButton(text="LADA GRANTA")
    n22 = KeyboardButton(text="MERCEDES-BENZ")
    n23 = KeyboardButton(text="🔙 ORQAGA QAYTISH")

    design1 = [
        [n1],
        [n2, n3],
        [n4, n5],
        [n6, n7],
        [n8, n9],
        [n10, n11],
        [n12, n13],
        [n14, n15],
        [n16, n17],
        [n18, n19],
        [n20, n21],
        [n22 , n23]


    ]

    tkm1 = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True, one_time_keyboard=True)
    return tkm1

