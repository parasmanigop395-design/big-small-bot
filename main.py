import asyncio, random, os
from datetime import datetime, timezone, timedelta
from telegram import Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    print("Bot Started")
    IST = timezone(timedelta(hours=5, minutes=30))
    while True:
        now_ist = datetime.now(IST)
        now_utc = now_ist.astimezone(timezone.utc)
        date_str = now_ist.strftime("%Y%m%d")
        utc_minutes = now_utc.hour * 60 + now_utc.minute + 1
        period = f"{date_str}10001{utc_minutes:04d}"
        pred = random.choice(["BIG","SMALL"])
        emoji = "🟢 BIG" if pred=="BIG" else "🔴 SMALL"
        msg = f"🔥 BIG SMALL SIGNAL 🔥\n\n📊 Period: `{period}`\n🎯 Prediction: **{pred}** {emoji}"
        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode='Markdown')
        except Exception as e:
            print(e)
        await asyncio.sleep(60)
if __name__ == "__main__":
    asyncio.run(start_bot())
