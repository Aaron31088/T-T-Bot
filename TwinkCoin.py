import discord
import sys
import json

class TwinkCoin:
  def __init__(self, UserID, Amount):
    self.UserID = UserID
    self.Amount = Amount


def giveCoin(amount, UserID):
    CoinList = ImportTwinkCoin()
    if any(str(Coin.UserID) == str(UserID) for Coin in CoinList):
        for Coin in CoinList:
            if str(Coin.UserID) == str(UserID):
                Coin.Amount = int(Coin.Amount) + int(amount)
    else:
        CoinList.append(TwinkCoin(UserID, amount))
    CreateTwinkCoinJSON(CoinList)

async def serverGiveCoin(amount, UserID, client):
    try:
        channel = await client.fetch_channel(695734889567354932)
        user = await client.fetch_user(UserID)
        CoinList = ImportTwinkCoin()
        if any(str(Coin.UserID) == str(UserID) for Coin in CoinList):
            for Coin in CoinList:
                if str(Coin.UserID) == str(UserID):
                    Coin.Amount = int(Coin.Amount) + int(amount)
        else:
            CoinList.append(TwinkCoin(UserID, amount))
        CreateTwinkCoinJSON(CoinList)

        print(f"{user.name} has been given {amount} TwinkCoin")
        Balance = getUserCoinBalance(UserID)
        if Balance % 10 == 0:
            await channel.send(f"{user.mention} has reached {Balance} TwinkCoins <:twinkCoin:937536799000125490>")
    except Exception as e:
        e = "Error"
        await channel.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")

async def CoinBalance(ctx):
    try:
        CoinList = ImportTwinkCoin()
        if any(str(Coin.UserID) == str(ctx.message.author.id) for Coin in CoinList):
            for Coin in CoinList:
                if str(Coin.UserID) == str(ctx.message.author.id):
                    await ctx.send(f"Your TwinkCoin Balance is {Coin.Amount}")
        else:
            await ctx.send("You don't have any TwinkCoins <:twinkCoin:937536799000125490>")
    except Exception as e:
        e = "Error"
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")

def getUserCoinBalance(UserID):
    try:
        CoinList = ImportTwinkCoin()
        if any(str(Coin.UserID) == str(UserID) for Coin in CoinList):
            for Coin in CoinList:
                if str(Coin.UserID) == str(UserID):
                    return int(Coin.Amount)
        else:
            return 0
    except Exception as e:
        e = "Error"


async def CoinBoard(ctx, client):
    try:
        CoinList = ImportTwinkCoin()
        guild = client.get_guild(694355736901320705)
        CoinList.sort(key=lambda Coin: int(Coin.Amount))
        CoinList.reverse()
        Output = ""
        Counter = 0
        for Coin in CoinList:
            Counter += 1
            print(Coin.UserID)
            try:
                member = await guild.fetch_member(Coin.UserID)
                if member.nick:
                    name = member.nick
                else:
                    name = member.name
                Output += f"{name} : {Coin.Amount}\n"
                if Counter == 10:
                    break
            except Exception as e:
                print(e)
        Output += "<:twinkCoin:937536799000125490>"

        await ctx.send(Output)
    except Exception as e:
        e = "Error"
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")


def ImportTwinkCoin():
    f = open('TwinkCoin.json')
    data = json.load(f)
    CoinList = []
    for i in data['TwinkCoin']:
        NewCoin = TwinkCoin(i['UserID'], i['Amount'])
        CoinList.append(NewCoin)
    # # Closing file
    f.close()
    return CoinList


def CreateTwinkCoinJSON(CoinList):
    JSONData = {"TwinkCoin": []}
    for Coin in CoinList:
        CoinData = {"UserID": str(Coin.UserID),
                    "Amount": str(Coin.Amount)}

        JSONData["TwinkCoin"].append(CoinData)
    print("WRITING")
    with open('TwinkCoin.json', 'w') as f:
        json.dump(JSONData, f)
    return




