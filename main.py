from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7794264500:AAHxFvkTIXSPtobaDnFMHG9L7Yz1OPhEH10"
CORRECT_CODE = "linkhack hai link code bro"
HACK_LINK = "https://erlgswc83zsw.devv.app"

user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ Warning ‼️\n\n"
        "Before Using This Please Connect Your Game ID Server With Bot Otherwise You May Fall Into A Big Loss.\n\n"
        "|| THANK YOU AND A HUMBLE REQUEST FROM ADMIN ||"
    )

async def linkhack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = "awaiting_code"
    await update.message.reply_text(
        "🛠 This Is Your Hack Link\n✅ Open And Enjoy\n\n"
        "🔐 Please Enter Your Link Code:\n(This code is private. Only the Admin can give it to you.)"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_input = update.message.text.strip()

    if user_states.get(user_id) == "awaiting_code":
        if user_input.lower() == CORRECT_CODE.lower():
            await update.message.reply_text(f"🎯 Here Is Your Hack Link:\n{HACK_LINK}")
        else:
            await update.message.reply_text("❌ Wrong Code. Please contact admin @CLOWNMODS.")
        user_states[user_id] = None
    else:
        await update.message.reply_text("ℹ️ Unknown message. Type /start or /linkhack to begin.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("linkhack", linkhack))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
