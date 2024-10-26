import requests
from bs4 import BeautifulSoup
import schedule
import time
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder
# Telegram bot setup
TELEGRAM_TOKEN = '7713171054:AAF4sL1XxoU6yyMCZftuj870n5iQPGj-nxo'
CHAT_ID = '109194797'
bot = Bot(token=TELEGRAM_TOKEN)

# List of websites to monitor
WEBSITES = [
    'https://www.extraloppan.is/',
    'https://riteil.is/collections/vorur-i-riteil'
]

# Keywords to search on the websites
KEYWORDS = ['Stone Island', 'Ganni']

async def send_message(text):
    await app.bot.send_message(chat_id=CHAT_ID, text=text)

async def check_website(url):
    try:
        print(f"Checking website: {url}")  # Debugging statement
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text().lower()

        for keyword in KEYWORDS:
            if keyword.lower() in page_text:
                message = f"Keyword '{keyword}' found on {url}"
                await send_message(message)
                print(f"Notification sent for {url} with keyword '{keyword}'")
                return

    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
    finally:
        print(f"Finished checking: {url}")  # Debugging statement

async def check_websites():
    for website in WEBSITES:
        await check_website(website)

def schedule_checks():
    asyncio.run(check_websites())

# Schedule the task to run every 6 hours
schedule.every(6).hours.do(schedule_checks)

print("Starting website monitor...")

# Keep the script running and execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
2. Common Issues
Slow Network or Unresponsive Websites: If any of the websites you're checking are slow to respond or down, it may cause your script to hang. To avoid this, you can set a timeout for your requests:

python
Copy code
response = requests.get(url, timeout=10)  # 10-second timeout
Infinite Loop or Blocked Event Loop: Make sure that your event loop isn't being blocked. If the requests are synchronous (as they are in the example), the script will wait for each request to complete before moving to the next one. If you have many websites, consider using asynchronous requests with aiohttp.

Check for Exceptions: The script might be running into an exception that you’re not catching. Ensure all potential errors are handled properly.

Print Statements: Make sure to have print statements before and after significant actions (like checking a website) to trace where the script might be getting stuck.

3. Example of Asynchronous Requests
To further optimize and prevent blocking, you can use aiohttp for asynchronous HTTP requests. Here's an example of how you could modify your check_website function to use aiohttp:

python
Copy code
import aiohttp
import asyncio

async def check_website(url):
    async with aiohttp.ClientSession() as session:
        try:
            print(f"Checking website: {url}")  # Debugging statement
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                page_text = soup.get_text().lower()

                for keyword in KEYWORDS:
                    if keyword.lower() in page_text:
                        message = f"Keyword '{keyword}' found on {url}"
                        await send_message(message)
                        print(f"Notification sent for {url} with keyword '{keyword}'")
                        return

        except Exception as e:
            print(f"Error accessing {url}: {e}")
        finally:
            print(f"Finished checking: {url}")  # Debugging statement