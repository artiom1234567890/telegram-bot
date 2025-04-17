from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салом, ман боти Telegram ҳастам!")

app = ApplicationBuilder().token("7997452866:AAFJtRMsxO0eZKMqfPEnS4uM5uhcXESFQkM").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
