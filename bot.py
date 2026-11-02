import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

SAVASLAR = {
    "malazgirt": "1071 Malazgirt",
    "canakkale": "1915 Canakkale",
    "istanbul": "1453 Fetih",
    "mohac": "1526 Mohac",
    "sakarya": "1921 Sakarya"
}

async def start(update, context):
    await update.message.reply_text("Calisiyor /savas Malazgirt")

async def savas(update, context):
    isim = " ".join(context.args).lower()
    await update.message.reply_text(SAVASLAR.get(isim, "Bulamadim"))

TOKEN = os.getenv("TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("savas", savas))

app.run_polling()
