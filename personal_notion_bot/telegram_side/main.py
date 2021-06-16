from loader import bot, storage

async def on_shutdown(dp):
	await bot.close()
	await storage.close()

if __name__ == '__main__':
	from aiogram import executor
	import handlers

	executor.start_polling(handlers.dp, on_shutdown = on_shutdown, skip_updates=True)

