import asyncio
from threading import Thread

# import MessageGeneration
import OnReaction
import Quote
import Messages
import MessageDataMethods
import CommandPermissions
import OnMessage
import MessageGraphs
import Generator
import Games
import TwinkCoin
import discord

intents = discord.Intents.all()
intents.members = True
intents.reactions = True
from discord.ext import commands
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def getMessageData(ctx):
    if not CommandPermissions.isAaron(ctx):
        await ctx.send("This command is for Aaron only")
        return
    await Messages.GetMessages(client)

@client.command()
async def quote(ctx):
    await Quote.Quote2(ctx, client)

@client.command()
async def MostReactions(ctx):
        await MessageDataMethods.MostReactions(ctx, client)

@client.command()
async def OldestMessage(ctx):
        await MessageDataMethods.OldestMessage(ctx, client)

# @client.command()
# async def BiggestGap(ctx):
#         await MessageDataMethods.BiggestGap(ctx, client)

@client.command()
async def GraphMessages(ctx):
        await MessageGraphs.GraphMessages(ctx, client)


@client.command()
async def GraphAllMessages(ctx):
    if not CommandPermissions.isAaron(ctx):
        await ctx.send("This command is for Aaron only")
        return
    await MessageGraphs.GraphAllMessages(ctx, client)

@client.command()
async def giveTwinkCoin(ctx):
    if not CommandPermissions.isAaron(ctx):
        await ctx.send("This command is for Aaron only")
        return
    channel = ctx.channel
    Input = ctx.message.content.split()
    await TwinkCoin.serverGiveCoin(Input[2], Input[1], client)

@client.command()
async def CoinBalance(ctx):
    await TwinkCoin.CoinBalance(ctx)

@client.command()
async def CoinBoard(ctx):
    await TwinkCoin.CoinBoard(ctx, client)


@client.command()
async def Slots(ctx):
    await Games.slotsgame(ctx, client)

# @client.command()
# async def whatwouldisay(ctx):
#     thread = Thread(target=MessageGeneration.GenerateText, args=(ctx,))
#     thread.start()

@client.command()
async def generate(ctx):
    OutMessage = await Generator.SetMessage(ctx, "Generating Image\nThis will take a few minutes\n```Starting```", None)
    thread = Thread(target=Generator.generate2, args=(ctx, OutMessage,))
    thread.start()

@client.command()
async def generatephoto(ctx):
    OutMessage = await Generator.SetMessage(ctx, "Generating Image\nThis will take a few minutes\n```Starting```", None)
    thread = Thread(target=Generator.generatePhoto, args=(ctx, OutMessage,))
    thread.start()

@client.event
async def on_reaction_add(reaction, user):
    await OnReaction.onReactionAdd(reaction, user, client)

@client.event
async def on_reaction_remove(reaction, user):
    await OnReaction.onReactionRemove(reaction, user, client)

@client.event
async def on_message(ctx):
    await OnMessage.OnMessage(ctx, client)
    await client.process_commands(ctx)

client.run('NzI3NjQ2NzAzOTEzNjY0NTgy.Xvu3zQ.eK4W__kuVz_LZWvQBKM1bPlHp6A')
