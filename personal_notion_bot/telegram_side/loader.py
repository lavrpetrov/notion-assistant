from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sys

sys.path.append("..")
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
memory_storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=memory_storage)
