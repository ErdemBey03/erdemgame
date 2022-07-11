bot=Client(
    "Sample Bot",
    api_id = 17586299
    api_hash = d3438b8f8cfff705c7cd1eb0ee0053dc
    bot_token = 5374270506:AAHr5M4wbDdY8RX_zNJStGejS6fv1IxRbrI
)

@bot.on_message(filter.command("start"))
async def start(client, message)
await bot.send_message("BURUH")


bot.run()
