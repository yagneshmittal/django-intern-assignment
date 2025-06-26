import os
import django
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_intern.settings')
django.setup()

from api.models import TelegramUser
from django.conf import settings

from asgiref.sync import sync_to_async

@sync_to_async
def save_user(username):
    TelegramUser.objects.get_or_create(username=username)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"Received /start from user: {user.id}, username: {user.username}, first name: {user.first_name}")

    username = user.username or f"{user.first_name}_{user.id}"

    await save_user(username)

    await update.message.reply_text(f"Hello {username}, you are now registered!")

async def main():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Telegram Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main())
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()

        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
