# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, ContextTypes

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton("Открыть WebApp", web_app={"url": "https://andjusyty.github.io/TelegramBot/"})]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text("Нажми кнопку, чтобы открыть WebApp:", reply_markup=reply_markup)

# app = Application.builder().token("7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70").build()
# app.add_handler(CommandHandler("start", start))
# app.run_polling()


# import json
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# API_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# # Reply-клавиатура с WebApp
# webapp_markup = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="📅 Выбрать дату", web_app=WebAppInfo(url="https://andjusyty.github.io/telegbot/"))]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True
# )

# @dp.message_handler(commands=["start"])
# async def send_welcome(message: types.Message):
#     await message.answer("Выберите дату и время:", reply_markup=webapp_markup)

# # Обработка данных из WebApp
# @dp.message_handler(content_types=["web_app_data"])
# async def handle_webapp(message: types.Message):
#     data = json.loads(message.web_app_data.data)
#     await message.answer(f"✅ Вы выбрали:\n📅 {data['formatted']}\n🌍 {data['timezone']}")

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)

import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"

# ✅ Вот тут правильная инициализация бота
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def cmd_start(message: Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Выбрать дату", web_app=WebAppInfo(url="https://andjusyty.github.io/telegbot/"))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Выберите дату и время:", reply_markup=markup)

@dp.message(content_types=["web_app_data"])
async def handle_webapp(message: Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(
        f"✅ Вы выбрали:\n📅 <b>{data['formatted']}</b>\n🌍 <i>{data['timezone']}</i>"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




