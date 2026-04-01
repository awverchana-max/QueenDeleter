from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("8631056763:AAHpFpYVxt5vEJ5Ljkwgs15jFVjhjStsYJI")

TARGET_TEXT = "{{strategy.order.alert_message}}"

async def delete_filtered_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        message = update.channel_post

        if message.text and TARGET_TEXT in message.text:
            try:
                await message.delete()
                print("Deleted:", message.text)
            except Exception as e:
                print("Error:", e)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, delete_filtered_messages))

print("Bot running...")
app.run_polling()