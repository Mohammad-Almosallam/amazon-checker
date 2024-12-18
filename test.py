import asyncio
from telegram import Bot

async def send_telegram_message(bot_token, chat_id, message):
    try:
        bot = Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Replace with your bot's token and chat ID

bot_token = "7632824577:AAHQnlcqpi0ApgTT1kQyZ4ZGyqgm6PWN950"
chat_id = "582141473"

# Test message
test_message = "Hello! This is a test message from your Telegram bot."

# Run the async function
asyncio.run(send_telegram_message(bot_token, chat_id, test_message))
