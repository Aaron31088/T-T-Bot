import discord
import random
import time
import TwinkCoin

async def slotsgame(ctx, client):
    Coins = TwinkCoin.getUserCoinBalance(ctx.message.author.id)
    if Coins == 0:
        await ctx.send(f"you outta coins bro\n Balance: {Coins} Coins")
        return
    if Coins < 0:
        await ctx.send(f"you in debt bro\n Balance: {Coins} Coins")
        return

    Message = await ctx.send("🎰")
    OutMessage = ""
    EmojiList = ["🍆", "<:twinkCoin:937536799000125490>", "🍒", "<:Oliver:794392427871207464>"]

    Multiplier = 1

    input = ctx.message.content
    input = input.replace('.Slots ', '')
    if input.isnumeric():
        Multiplier = int(input)

    await TwinkCoin.serverGiveCoin(-Multiplier, ctx.message.author.id, client)

    for i in range(3):
        Position1 = random.choice(EmojiList)
        Position2 = random.choice(EmojiList)
        Position3 = random.choice(EmojiList)
        OutMessage = f"{Position1}{Position2}{Position3}"
        await Message.edit(content=OutMessage)
        time.sleep(1)

    for i in range(3):
        Position2 = random.choice(EmojiList)
        Position3 = random.choice(EmojiList)
        OutMessage = f"{Position1}{Position2}{Position3}"
        await Message.edit(content=OutMessage)
        time.sleep(1)

    for i in range(3):
        Position3 = random.choice(EmojiList)
        OutMessage = f"{Position1}{Position2}{Position3}"
        await Message.edit(content=OutMessage)
        time.sleep(1)

    Winnings = 0
    if Position1 == Position2 and Position1 == Position3:
        OutMessage += "\n<:twinkCoin:937536799000125490><:twinkCoin:937536799000125490><:twinkCoin:937536799000125490>YOU WIN<:twinkCoin:937536799000125490><:twinkCoin:937536799000125490><:twinkCoin:937536799000125490>"
        Winnings = Multiplier*10
        await TwinkCoin.serverGiveCoin(Multiplier*10, ctx.message.author.id, client)
        if Position1 == "🍆":
            OutMessage += "\n🏆🏆🏆JACKPOT🏆🏆🏆"
            Winnings += Multiplier*20
            await TwinkCoin.serverGiveCoin(Multiplier*20, ctx.message.author.id, client)
        if Position1 == "<:Oliver:794392427871207464>":
            OutMessage += "\nlol jk"
            Winnings -= Multiplier*20
            await TwinkCoin.serverGiveCoin(-Multiplier*10, ctx.message.author.id, client)


        OutMessage += f"\n{Winnings} TwinkCoins!"
        await Message.edit(content=OutMessage)
    else:
        OutMessage += "\nYou Lose"
        await Message.edit(content=OutMessage)


