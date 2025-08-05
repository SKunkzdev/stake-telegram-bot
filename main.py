from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

import os

# You should set this securely via environment variables
TOKEN = os.getenv("8217176942:AAFBB2PDBpFUkjEKDjLLosx5bZdogPFacj8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Stake Predictor Bot Activated ✅")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
