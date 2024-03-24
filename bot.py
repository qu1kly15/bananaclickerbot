import asyncio

from aiogram import Router, Bot, Dispatcher, F 
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Go to app", web_app=WebAppInfo(
            url="https://9ef5-109-236-81-168.ngrok-free.app"
        )
    )
    return builder.as_markup() 


router = Router() 

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Let's click bananas now!",
    reply_markup=webapp_builder())

async def main() -> None:
    bot = Bot("6874087731:AAGmxqffEJBZqZAXnDj_ILemzhEEFRGxMAk", default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
