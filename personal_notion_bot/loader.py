import logging
import asyncio


from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import *


bot = Bot(token = BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


logging.basicConfig(level=logging.INFO)