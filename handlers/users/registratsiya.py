from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import CHANNELS, ADMINS
from loader import dp, bot
from states.register import Royxat

@dp.message_handler(commands='vacancy', state=None)
async def start(msg: types.Message):
    await msg.answer("To'liq ismingizni kiriting (F.I.O)")
    await Royxat.ism.set()

@dp.message_handler(state=Royxat.ism)
async def step1(msg: types.Message, state:FSMContext):
    ism=msg.text
    await state.update_data({
        'ism':ism
    })
    await msg.answer("Yoshingizni kiritng")
    await Royxat.next()

@dp.message_handler(state=Royxat.yosh)
async def step2(msg: types.Message, state:FSMContext):
    yosh=msg.text
    await state.update_data({
        'Yosh':yosh
    })
    await msg.answer("Telefon no'meringizni kiriting")
    await Royxat.next()

@dp.message_handler(state=Royxat.tel)
async def step3(msg: types.Message, state:FSMContext):
    tel=msg.text
    await state.update_data({
        'Tel':tel
    })
    await msg.answer("Kasbingiz kiriting\nAgar dasturchi bo'lsangiz misol uchun(Python, node JS, Django, Aiogram) ")
    await Royxat.next()

@dp.message_handler(state=Royxat.tillar)
async def step4(msg: types.Message, state:FSMContext):
    tillar=msg.text
    await state.update_data({
        'Texnologiya':tillar
    })
    await msg.answer("Narhni kiriting")
    await Royxat.next()
    
@dp.message_handler(state=Royxat.narh)
async def step6(msg: types.Message, state:FSMContext):
    narh=msg.text
    await state.update_data({
        'Narh':narh
    })
    await msg.answer("Hududingizni kiriting")
    await Royxat.next()

@dp.message_handler(state=Royxat.shahar)
async def step7(msg: types.Message, state:FSMContext):
    hudud=msg.text
    await state.update_data({
        'hudud':hudud
    })
    await msg.answer("O'zingiz haqingizda ma'lumtni kiriting kiritng")
    await Royxat.next()

@dp.message_handler(state=Royxat.bio)
async def step8(msg: types.Message, state:FSMContext):
    malumot=msg.text
    await state.update_data({
        "Malumot":malumot
    })

    data = await state.get_data()
    xabar=f"👨‍💻 Ism: {data['ism']}\n"\
        f"🗓 Yosh: {data['Yosh']}\n"\
        f"📞 Telefon: {data['Tel']}\n"\
        f"🐍 Tillar: {data['Texnologiya']}\n"\
        f"🏘 Shahar: {data['hudud']}\n"\
        f"💸 Narh: {data['Narh']}\n"\
        f"📑 ma'lumoti: {data['Malumot']}"
    await msg.answer("Xabar Kanalga Joylandi")
    await bot.send_message(chat_id="-1001733164373",text=xabar)
    await state.finish()
