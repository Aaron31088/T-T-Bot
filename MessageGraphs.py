import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import MessagesJSONReader
import csv
from datetime import datetime
import discord
import io
from PIL import Image
from tqdm import tqdm

async def GraphMessages(ctx, client):
    try:
        Messages = MessagesJSONReader.ImportMessageData()

        f = open('MessageData.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(["Date", "Count"])
        DateList = []
        for Message in Messages:
            if int(Message.AuthorID) == int(ctx.message.author.id):
                try:
                    Date = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S.%f')
                except:
                    Date = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S')

                Date = Date.strftime("%Y-%m-%d")
                DateList.append(Date)

        DateList = sorted(DateList)

        my_dict = {i: DateList.count(i) for i in DateList}

        for i in my_dict:
            writer.writerow([i, my_dict[i]])

        f.close()

        MessageData = pd.read_csv("MessageData.csv", parse_dates=['Date'])

        MessageData['count_7day_ave'] = MessageData.Count.rolling(7).mean().shift(-3)

        # bigger plot elements suitable for giving talks
        sns.set_context("talk")
        # set figure size
        plt.margins(0)
        plt.figure(figsize=(20, 10))

        # Time series plot with Seaborn lineplot() with label
        sns.lineplot(x="Date", y="Count",
                     label="Daily", data=MessageData,
                     ci=None)
        # 7-day rolling average Time series plot with Seaborn lineplot() with label
        sns.lineplot(x="Date", y="count_7day_ave",
                     label="7-day Ave",
                     data=MessageData,
                     ci=None)
        # set axis labels
        plt.xlabel("Date", size=16)
        plt.ylabel("Messages", size=16)
        # save image as PNG file
        plt.savefig("Time_Series_Plot_with_7day_average_Seaborn.png",
                    format='png',
                    dpi=500)

        await ctx.send(file=discord.File("Time_Series_Plot_with_7day_average_Seaborn.png"))
    except Exception as e:
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")


async def GraphAllMessages(ctx, client):
    try:
        Messages = MessagesJSONReader.ImportMessageData()

        f = open('MessageData.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(["Date", "Count"])
        DateList = []
        for Message in tqdm(Messages):
            try:
                Date = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S.%f')
            except:
                Date = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S')

            Date = Date.strftime("%Y-%m-%d")
            DateList.append(Date)

        print("Sorting Dates")
        DateList = sorted(DateList)

        print("Getting Counts")
        my_dict = {i: DateList.count(i) for i in tqdm(DateList)}


        for i in tqdm(my_dict):
            writer.writerow([i, my_dict[i]])

        f.close()

        print("Writing")
        MessageData = pd.read_csv("MessageData.csv", parse_dates=['Date'])

        print("Calculating Rolling Average")
        MessageData['count_7day_ave'] = MessageData.Count.rolling(7).mean().shift(-3)

        # bigger plot elements suitable for giving talks
        sns.set_context("talk")
        # set figure size
        plt.margins(0)
        plt.figure(figsize=(20, 10))

        # Time series plot with Seaborn lineplot() with label
        sns.lineplot(x="Date", y="Count",
                     label="Daily", data=MessageData,
                     ci=None)
        # 7-day rolling average Time series plot with Seaborn lineplot() with label
        sns.lineplot(x="Date", y="count_7day_ave",
                     label="7-day Ave",
                     data=MessageData,
                     ci=None)
        # set axis labels
        plt.xlabel("Date", size=16)
        plt.ylabel("Messages", size=16)
        # save image as PNG file
        plt.savefig("Time_Series_Plot_with_7day_average_Seaborn.png",
                    format='png',
                    dpi=500)

        await ctx.send(file=discord.File("Time_Series_Plot_with_7day_average_Seaborn.png"))
    except Exception as e:
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")

