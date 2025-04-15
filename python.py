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


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Открыть WebApp", web_app=WebAppInfo(url="https://andjusyty.github.io/TelegramBot/"))]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Выберите дату и время:", reply_markup=markup)

@dp.message_handler(content_types=["web_app_data"])
async def webapp_handler(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f"Вы выбрали:\n📅 {data['formatted']}")

