import os
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Get token from environment variable
TOKEN = os.environ.get('8347501026:AAGLWDJ3UMpYMk8I98za6EiNXevYZ4OTaM4')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """🎉 Welcome to Clicker App! 🎉

Get ready to tap your way to satisfaction! Click the button below to start playing!

How to play:
• Tap the "CLICK ME!" button
• Each tap adds +1 to your total
• Your score is saved automatically

Ready to build your clicking legacy? Let's begin!"""

    # Use your MINI APP URL (not regular web URL)
    await update.message.reply_text(
        welcome_text,
        reply_markup={
            "inline_keyboard": [[
                {
                    "text": "Play Clicker Game 🎮",
                    "web_app": WebAppInfo(url="https://t.me/clickerminiapptestingorg_bot/Clicker?startapp=clicker")
                }
            ]]
        }
    )

def main():
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add command handler
    application.add_handler(CommandHandler("start", start))
    
    # Start the bot
    print("Bot starting...")
    application.run_polling()
    print("Bot stopped")

if __name__ == "__main__":
    main()