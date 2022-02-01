import MessagesJSONReader
from datetime import timedelta

async def MostReactions(ctx, client):
    try:
        Messages = MessagesJSONReader.ImportMessageData()
        MostReactedMessage = Messages[0]
        MinCount = 0

        for Message in Messages:
            if int(Message.AuthorID) == int(ctx.message.author.id):
                ReactionSum = 0
                for Reaction in Message.Reactions:
                    ReactionSum += int(Reaction['Count'])
                if ReactionSum > MinCount:
                    MostReactedMessage = Message
                    print(Message.Content)
                    MinCount = ReactionSum

        Output = f"{MinCount} Reactions\n"
        Output += f"\n> {MostReactedMessage.Content}\n"
        Output += MostReactedMessage.JumpURL
        await ctx.send(Output)

    except Exception as e:
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")

from datetime import datetime

async def OldestMessage(ctx, client):
    try:
        Messages = MessagesJSONReader.ImportMessageData()
        OldestMessageObject = Messages[0]
        OldestDate = datetime.strptime(Messages[0].CreatedUTC, '%Y-%m-%d %H:%M:%S.%f')

        for Message in Messages:
            if int(Message.AuthorID) == int(ctx.message.author.id):
                try:
                    date_time_obj = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S.%f')
                except:
                    date_time_obj = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S')
                if date_time_obj < OldestDate:
                    OldestDate = date_time_obj
                    OldestMessageObject = Message

        Output = OldestDate.strftime("%A %B %d, %Y")
        Output += f"\n> {OldestMessageObject.Content}\n"
        Output += OldestMessageObject.JumpURL

        await ctx.send(Output)

    except Exception as e:
        await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")

# async def BiggestGap(ctx, client):
#     try:
#         Messages = MessagesJSONReader.ImportMessageData()
#         OldestMessageObject = Messages[0]
#
#         UserDates = []
#         for Message in Messages:
#             if int(Message.AuthorID) == int(ctx.message.author.id):
#                 try:
#                     Date1 = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S.%f')
#                 except:
#                     Date1 = datetime.strptime(Message.CreatedUTC, '%Y-%m-%d %H:%M:%S')
#                 UserDates.append(Date1)
#
#         FinalDate1 = None
#         FinalDate2 = None
#         UserDates = sorted(UserDates)
#         DateGap = timedelta(0)
#         Date1 = UserDates[0]
#         for Date in UserDates:
#             Date2 = Date
#
#             if Date2 - Date1 > DateGap:
#                 DateGap = Date2 - Date1
#                 FinalDate1 = Date1
#                 FinalDate2 = Date2
#                 print(f"FOUND GAP {DateGap.days}")
#                 Output = FinalDate1.strftime("%A %B %d, %Y\n")
#                 Output += FinalDate2.strftime("%A %B %d, %Y")
#                 print(Output)
#             Date1 = Date2
#
#
#         Output = FinalDate1.strftime("%A %B %d, %Y\n")
#         Output += FinalDate2.strftime("%A %B %d, %Y")
#
#         await ctx.send(Output)
#
#     except Exception as e:
#         await ctx.send(f"OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!\n<@561776295353253889>\n```{e}```")
