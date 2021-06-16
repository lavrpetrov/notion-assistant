import sys; sys.path.append("..")
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN


bot = Bot(token = BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

