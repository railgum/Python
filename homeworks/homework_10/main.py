

from warnings import filters
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import datetime
from config import tg_bot_token, open_weather_token as wt
import xplay0
import new_year_days
import moon_phase
import weather

app = ApplicationBuilder().token(
    tg_bot_token).build()

print('Bot start')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/sum\n/days\n/moon\n/weather\n/help')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(f'{a} + {b} = {a+b}')


async def playX_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(xplay0.show_matrix())
    message = update.message.text.split()


async def daysBeforeNY(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(new_year_days.ny_days())


async def moonPhase(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    c = int(items[3])
    await update.message.reply_text(moon_phase.moon_phase(a, b, c))


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # await update.message.reply_text("Введите город, где хотите узнать погоду")
    await update.message.reply_text("Введите город, где хотите узнать погоду")
    return 1


async def weather_show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = update.message.text
    await update.message.reply_text(weather.get_weather(city, wt))
    return ConversationHandler.END
handler = ConversationHandler(
    entry_points=[CommandHandler("weather", weather_command)],
    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, weather_show)]
    },
    fallbacks=[]
)
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("play", playX_command))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("days", daysBeforeNY))
app.add_handler(CommandHandler("moon", moonPhase))
app.add_handler(handler)


app.run_polling()
print('Bot stop')
