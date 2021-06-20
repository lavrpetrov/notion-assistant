from loader import dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
import sys

sys.path.append("..")


class Waiting(StatesGroup):
    waiting_for_name = State()
    waiting_for_content = State()


@dispatcher.message_handler(Command("new_page"), state=None)
async def entrance(message: types.Message):
    await message.answer("Введите название новой страницы")
    await Waiting.waiting_for_name.set()


@dispatcher.message_handler(state=Waiting.waiting_for_name)
async def name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Введите содержимое страницы")
    await Waiting.next()


@dispatcher.message_handler(state=Waiting.waiting_for_content)
async def content(message: types.Message, state: FSMContext):
    data = await state.get_data()
    content = message.text
    name = data.get("name")

    # send_page.post_page(name, content)

    await message.answer("Дело сделано!")

    await state.finish()
