from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

import send_page


class waiting(StatesGroup):
    waiting_for_name = State()
    waiting_for_content = State()


@dp.message_handler(Command("new_page"), state = None)
async def Entance(message:types.Message):
    await message.answer("Введите название новой страницы")
    await waiting.waiting_for_name.set()


@dp.message_handler(state = waiting.waiting_for_name)
async def name(message: types.Message, state:FSMContext):
    name = message.text
    await state.update_data(name  = name)
    await message.answer("Введите содержимое страницы")
    await waiting.next()

@dp.message_handler(state = waiting.waiting_for_content)
async def content(message: types.Message, state:FSMContext):
    data = await state.get_data()
    content = message.text
    name = data.get("name")

    send_page.func_send_page(name, content)

    await message.answer("Дело сделано!")

    await state.finish()
