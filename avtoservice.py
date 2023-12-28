import asyncio
import logging
import sys
from aiogram import F, types

from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.utils.markdown import hbold

from tugmalar import xizmatlar_button,xizmatlar1,tel_num
from inline_button import inline_number

TOKEN = '6560118733:AAEYKRJBeuYhYU2iIJ49Uv64pcfC3I13Cp4'
dp = Dispatcher()


@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("photo handler successful ")
    await message.answer(f"{message.photo[0].file_id}")

# @dp.message(Command('start'))
# async def command_start(msg: types.Message):
#     chat_id = msg.chat.id
#     await msg.answer(text=f"ASSALOMU ALAYKUM !   {msg.from_user.full_name}  🚘🚖🚙🛻🔧🪛 BIZNING AVTOSERVIZ BOTIMIZGA XUSH KELIBSIZ!" )
#     await msg.answer(text="",reply_markup=xizmatlar_button())


@dp.message(Command('start'))
async def start_hander(msg: Message) -> None:
    await msg.answer(f"Hello {hbold(msg.from_user.full_name)}")
    await msg.answer(f"ASSALOMU ALAYKUM ! 🚘🚖🚙🛻🔧🪛 BIZNING AVTOSERVIZ BOTIMIZGA  XUSH KELIBSIZ! ")
    await msg.answer(text=">>>", reply_markup=xizmatlar_button())

# @dp.message()
# async def echo_handler(msg: Message):
#     # await msg.answer()
#     print(msg)

@dp.message(lambda msg: msg.text == '🔧 XIZMATLAR')
async def one_hander(msg: Message):
    await msg.answer(text="O'ZINGIZGA KERAKLIGINI TANLANG ", reply_markup=xizmatlar1())


async def send_photo_on_button_press(message: Message, image_url: str, text: str):
    await message.answer(text=text, reply_markup=xizmatlar1())
    media = types.InputMediaPhoto(media=image_url)
    await message.answer_media_group([media])

# @dp.message
# async def echo_handler(msg: Message):
#     # await  msg.answer()
#     print(msg)

@dp.message(lambda msg: msg.text == 'JIGULI 011')
async def Jiguli_011_button(message: Message):
    image_url = 'AgACAgIAAxkBAAIClmVh5q3vZiGNyG2DcNAO4gj155DSAAKe1DEbv0MQS1QR5H1x9gJfAQADAgADcwADMwQ'
    text = "KALOTKA oli_ora \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n RUCHNOY TROS"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'JIGULI 06')
async def Jiguli_06_button(message: Message):
    image_url = 'AgACAgIAAxkBAAICqmVh6AL0F9b7i65t9NwTON3OBMLoAAJm1TEbv0MQSyXFjNALRsL7AQADAgADcwADMwQ'
    text = """KALOTKA oldi-orqa 
     AMARTIZATOR oldi-orqa  
     PODSHIMNIK : oldi-orqa  
     SEPLENIYA TROS 
     RUCHNOY TROS
     DISTEPLENIYA
     GLAVNINY SILINDR
     
     """
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'JIGULI 07')
async def Jiguli_07_button(message: Message):
    image_url = 'AgACAgIAAxkBAAICwmVh6LeYaRUzXpIk2xAzDRCAkw98AAJp1TEbv0MQS3tpEey65oTEAQADAgADcwADMwQ'
    text = """KALOTKA oldi-orqa 
     AMARTIZATOR oldi-orqa 
     PODSHIMNIK : oldi-orqa 
     SEPLENIYA TROS 
     
     """
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'MATIZ 3 tali')
async def Matiz_3_handler(message: Message):
    image_url = 'AgACAgIAAxkBAAICxWVh6StWyjK1K-BeVyKZnGzwyw-XAAJs1TEbv0MQSzP74a1KUM3GAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n PODSHIMNIK : oldi-orqa \n SEPLENIYA TROS "
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'MATIZ Best')
async def Matiz_best(message: Message):
    image_url = 'AgACAgIAAxkBAAIC1mVh6h47sMIHdS4pngvPBKhPQI75AAJx1TEbv0MQS-22dd35XQp0AQADAgADcwADMwQ'
    text = """KALOTKA oldi-orqa 
    AMARTIZATOR oldi-orqa 
    Podshipnik : oldi-orqa 
    SEPLENIYA TROS 
    DISTEPLENIYA"""
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'MATIZ Evro')
async def Matiz_evro(message: Message):
    image_url = 'AgACAgIAAxkBAAIC2WVh6oCcCZjq06vv0Exe5bRVVcg0AAJz1TEbv0MQSyZJ95rVNbUxAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS "
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'MATIZ Avtomat')
async def matiz_avtomat(message: Message):
    image_url = 'AgACAgIAAxkBAAIDAmVh829yHlrDIMurraXurw9AZsLuAAK01TEbv0MQS_hKmugAAdWQkwEAAwIAA3MAAzME'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS "
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'SPARK 1.25')
async def spark_1(message: Message):
    image_url = 'AgACAgIAAxkBAAIDBWVh8905G2-saK6kbexmK-RTlKshAAK41TEbv0MQS1NTQZmRqpcHAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa  \n Podshipnik : oldi-orqa \n SEPLENIYA TROS  \n SKORS TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'SPARK /  MEHANIKA')
async def spark_mehanika(message: Message):
    image_url = 'AgACAgIAAxkBAAIEGGVrVrOUI2kJFMYhzabdMhGTsFJWAAJ92DEbyNtZS_EBp8J-wGUaAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS  \n SKORS TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'SPARK / AVTOMART')
async def spark_avtomat(message: Message):
    image_url = 'AgACAgIAAxkBAAIEG2VrV3qVeyxjyn07H4dpHNK9Ekp4AAKF2DEbyNtZS7SbSyrqtqtTAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS  \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)

@dp.message(lambda msg: msg.text == 'NEXIA 1')
async def nexia_1(message: Message):
    image_url = 'AgACAgIAAxkBAAIEHmVrWATDjfHAW3pMg2orbIlUAk3CAAKL2DEbyNtZSwuCDNojp9VBAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)

@dp.message(lambda msg: msg.text == 'NEXIA 2')
async def nexia_2(message: Message):
    image_url = 'AgACAgIAAxkBAAIEIWVrWOLTFPtTB4AXzZwsP1czbf0eAAKV2DEbyNtZSz8CxovAIHEAAQEAAwIAA3MAAzME'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'NEXIA 3')
async def nexia_03(message: Message):
    image_url = 'AgACAgIAAxkBAAIEU2VrdwJRt9ZzUaeEy88t-r1M1hhTAAKczzEbyNthSxGSn2I3QQdOAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'DAMAS')
async def damas(message: Message):
    image_url = 'AgACAgIAAxkBAAIEr2VuHwx7JkSGQNYAAQ7-4pDNq2jphgACg9AxGwABhnFLgk0LiAIufqEBAAMCAANzAAMzBA'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'LABO')
async def labo_handler(message: Message):
    image_url = 'AgACAgIAAxkBAAIEvmVuIvp1GAhhNyi2aoPzn4MnoT90AAK10DEbAAGGcUs8WcqInALzaAEAAwIAA3MAAzME'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa  \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA) \n PECHKA"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'KOBALT')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFFGVu4J5mt0V13EemMKHwP2r3eMGLAALEzzEb6Rt4SwmLT-Bt0LPAAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'LASETTI 1.8')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFQWVu7VIM7Y_x7oOJ5kUOV588qpZwAAIW0DEb6Rt4Sz6xvkBui7AwAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'JENTRA 1.5')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFF2Vu4aDBhPEiZHykXxT1DLMX7dI-AALIzzEb6Rt4SxSBW18sUWSHAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'KAPTIVA')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFRGVu7tbIRtW9RpJL7bWPmlhLPZyUAAI30DEb6Rt4SzHV26M8mJ7kAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'MALIBU')
async def spark_1(message: Message):
    image_url = 'AgACAgIAAxkBAAIDH2Vh9bbWY20xcBQ9fOk4OqkVtuiyAALF1TEbv0MQS8DYIlBN7btvAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa  \n AMARTIZATOR oldi-orqa"
    await send_photo_on_button_press(message, image_url, text)


@dp.message(lambda msg: msg.text == 'LADA GRANTA')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFT2Vu8fvsAhZ4eewlzyrLUCgpj5hZAAJO0DEb6Rt4S8EMHvpnnqapAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa  \n  AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa \n SEPLENIYA TROS \n TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == 'MERCEDES-BENZ')
async def kobalt(message: Message):
    image_url = 'AgACAgIAAxkBAAIFUmVu8qZ5GuPYsSuQve5-E8Ua2cbzAAJX0DEb6Rt4SxA_uY6AApwuAQADAgADcwADMwQ'
    text = "KALOTKA oldi-orqa \n AMARTIZATOR oldi-orqa \n  Podshipnik : oldi-orqa \n SEPLENIYA TROS \n  TERMOSTAT \n SUV NASOS (POMPA)"
    await send_photo_on_button_press(message,image_url,text)


@dp.message(lambda msg: msg.text == '🔙 ORQAGA QAYTISH')
async def lacation_hander(msg: Message):
    await msg.answer(text="Orqaga qaytish 🔙" , reply_markup=xizmatlar_button())



""" ---------------------------------- aloqa ---------------------------------------------- """

@dp.message(lambda msg: msg.text == '📞 TELEFON')
async def one_hander(msg: Message):
    await msg.answer(text="OZINGIZGA KERAKLIGINI TANLANG", reply_markup=tel_num())


@dp.message(lambda msg : msg.text == 'TELEGRAM AKAUNT')
async def tel_handler(msg: Message):
     await msg.answer(text="Telegram akaunt" , reply_markup=inline_number())

@dp.message(lambda msg: msg.text == 'TELEFON  ☎️ RAQAM')
async def one_hander(msg: Message):
    await msg.answer(text="""
📞 (90) 333 - 15 - 41
📞 (98) 304 - 97 - 87
📞 (99) 615 - 82 - 62
""")


@dp.message(lambda msg: msg.text == 'LAKATSIYA 📍')
async def lacation_hander(msg: Message):
    await msg.answer_location(41.365966920325, 69.23161914963357)


@dp.message(lambda msg: msg.text == '🔙 ORQAGA QAYTISH')
async def lacation_hander(msg: Message):
    await msg.answer(text="Orqaga qaytish 🔙" , reply_markup=xizmatlar_button())


""" ---------------------------------- ish vaqti ---------------------------------------------- """


@dp.message(lambda msg: msg.text == '🗓 ISH JADVALI')
async def lacation_hander(msg: Message):
    await msg.answer(text="""
ISH VAQTLARI :
DUSHANBA      8:00 DAN   |  OBED  13:00   |   9:00 GACHAM
SESHANBA      8:00 DAN   |  OBED  13:00   |   9:00 GACHAM
CHORSHANBA    8:00 DAN   |  OBED  13:00   |   9:00 GACHAM
PAYSHANBA     8:00 DAN   |  OBED  13:00   |   9:00 GACHAM
JUMA          8:00 DAN   |  OBED  13:00   |   9:00 GACHAM
SHANBA        8:00 DAN   |  OBED  13:00   |   10:00 / 11:00 GACHAM
YAKSHANBA     8:00 DAN   |  OBED  13:00   |   10:00 / 11:00 GACHAM 
""" , reply_markup=xizmatlar_button())



async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
