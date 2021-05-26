from loader import bot,storage

async def on_shutdown(dp):
	await bot.close()
	await storage.close()

if __name__ == '__main__':
	from aiogram import executor
	from handlers import dp, send_to_admin

	executor.start_polling(dp,on_startup = send_to_admin,on_shutdown = on_shutdown, skip_updates=True)
