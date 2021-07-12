from loader import bot, memory_storage


async def on_shutdown(dp):
    await bot.close()
    await memory_storage.close()


if __name__ == "__main__":
    from aiogram import executor
    import handlers

    executor.start_polling(
        handlers.dispatcher, on_shutdown=on_shutdown, skip_updates=True
    )
