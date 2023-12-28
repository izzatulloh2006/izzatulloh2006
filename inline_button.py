from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

def inline_number():
    btn1 = InlineKeyboardButton(text='<<< ENTER >>>', url='https://t.me/Sadullo_1979')
    desing = [
        [btn1]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=desing)
    return ikm
