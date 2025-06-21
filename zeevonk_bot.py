from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7773065799:AAE_l6uXQymuea5SZo8th25JiVdSWR8GQvg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌊 Welkom bij ZeevonkRadar!\n"
        "Gebruik /voorspelling om de actuele zeevonk-kans te bekijken.\n"
        "Gebruik /melding om een waarneming te melden."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

async def voorspelling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Simulatie of API-koppeling hier
    await update.message.reply_text("🔮 Vandaag is er 72% kans op zeevonk bij Noordwijk.")

app.add_handler(CommandHandler("voorspelling", voorspelling))

async def melding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Wil je een melding doen? Stuur locatie en beschrijving via onze site:\nhttps://zeevonkradar.nl/melden")