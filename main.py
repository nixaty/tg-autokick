import logging
import asyncio

from bot import bot
from dispatcher import dp

from handlers import router


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
