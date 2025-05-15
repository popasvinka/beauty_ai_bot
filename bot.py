import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from PIL import Image
import io

TOKEN = "7933646092:AAHf0W9gthyZJYQ1R4nWeCGXcXkcrN7xZqU"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я AI-бьюти-бот. Отправь мне селфи, и я дам рекомендации по уходу.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    photo_bytes = await photo_file.download_as_bytearray()
    img = Image.open(io.BytesIO(photo_bytes))

    # Пример анализа (заглушка)
    await update.message.reply_text("Спасибо! На фото заметна жирная кожа и воспаления. Рекомендую:\n\n— Bioderma Sébium\n— La Roche-Posay Effaclar Duo\n— The Ordinary Niacinamide 10%")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

if name == "__main__":
    app.run_polling()
