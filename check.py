import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio  # Import asyncio to run asynchronous tasks


# Function to check if the specified class exists in the HTML
def check_stock(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for the specific class in the HTML
        if soup.find("div", class_="a-section a-spacing-none aok-align-center aok-relative"):
            return True
        return False
    except Exception as e:
        print(f"Error checking stock for {url}: {e}")
        return False

# Function to send a notification via Telegram to multiple chat IDs
async def send_notification_telegram(message, bot_token, chat_ids):
    try:
        bot = Bot(token=bot_token)
        for chat_id in chat_ids:  # Iterate through each chat ID
            await bot.send_message(chat_id=chat_id, text=message)  # Await the coroutine
        print("Telegram notifications sent!")
    except Exception as e:
        print(f"Failed to send Telegram notification: {e}")

# Product URL to monitor
product_url = "https://www.amazon.sa/-/en/AMD-9800X3D-16-Thread-Desktop-Processor/dp/B0DKFMSMYK?sr=8-1"
# product_url = "https://www.amazon.sa/-/en/AMD-RyzenTM-9900X-24-Thread-Processor/dp/B0D6NN87T8/ref=sr_1_1?sr=8-1&ufe=app_do%3Aamzn1.fos.495cb95e-fb22-4946-8f40-b4235b181a9a"


# Headers for the HTTP request (to mimic a browser request)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Telegram bot credentials
bot_token = "7632824577:AAHQnlcqpi0ApgTT1kQyZ4ZGyqgm6PWN950"
chat_ids = ["179789859", "582141473"]  # List of chat IDs

# Periodic stock checking
while True:
    print(f"Checking stock for {product_url}...")
    if check_stock(product_url, headers):
        # Use asyncio to call the async notification function
        asyncio.run(
            send_notification_telegram(
                message=f"The product is available! Check it here: {product_url}",
                bot_token=bot_token,
                chat_ids=chat_ids
            )
        )
        break  # Exit the loop after finding the product in stock

    print("Waiting for 30 seconds before the next check...")
    time.sleep(30)  # Wait for 30 seconds before the next check
