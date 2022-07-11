const { Telegraf,Telegram } require('Telegraf')
const config = require("./config")
const telegram = new Telegram(config.token)
const bot = new Telegraf(config.token)

bot.command("start", (ctx) => {
 ctx.telegram.sendMessage(ctx.chat.id,''İ LOVE YOU BRO')
  })



process.once('SIGNINT', () => bot.stop('SIGNINT'))
process.once('SIGNTERM', () => bot.stop('SIGNTERM'))
