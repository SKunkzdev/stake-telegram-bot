from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")  # Read from environment variable

# Sample prediction function (replace with your API)
def get_prediction():
    try:
        response = requests.post("https://soulapi.vercel.app/predict", json={
            "game": "mines",
            "model": "v2",
            "mines": 3
        }, headers={"Content-Type": "application/json"})
        data = response.json()
        if "mines" in data:
            return " ".join([f"[{i}]" for i in data["mines"]])
        else:
            return "Prediction failed."
    except Exception as e:
        return f"Error: {str(e)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Welcome to Stake Predictor Bot\nUse /predict to get your Mines prediction.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prediction = get_prediction()
    await update.message.reply_text(f"🟩 Safe Tiles:\n{prediction}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))

if __name__ == "__main__":
    app.run_polling()
