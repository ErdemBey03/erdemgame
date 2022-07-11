bot=Client(
    "Sample Bot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@bot.on_message(filter.command("start"))
async def start(client, message)
await bot.send_message("BURUH")
