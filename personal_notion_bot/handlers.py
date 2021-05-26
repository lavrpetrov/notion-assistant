from loader import dp, bot
from aiogram import types
from config import ADMIN_ID
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

class waiting(StatesGroup):
	waiting_for_name = State()
	waiting_for_content = State()


async def send_to_admin(dp):
    await bot.send_message(chat_id = ADMIN_ID, text ="Bot is working")


@dp.message_handler(Command("new_page"), state = None)
async def Enterence(message:types.Message):
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
	await message.answer("Дело сделано!")
	
	await state.finish()


	#Вариант№2
	#await state.reset_state()

	#Вариант №3 без стирания данных в data
	##await state.reset_state(with_data=False)
