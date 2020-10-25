import discord
from discord.ext import commands
import json
import random


bot = commands.Bot(command_prefix= '')
bot.remove_command("help")
@bot.event
async def on_ready():
    print('三小機器人已上線喔')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')

@bot.command()
async def say(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message)
   
@bot.command()
@commands.is_owner()
async def clean(ctx,num:int):
    await ctx.channel.purge(limit=num+1)
    

@bot.command()
async def pixiv(ctx, world):
    await ctx.send(F'https://www.pixiv.net/search.php?word={world}&s_mode=s_tag')   

@bot.command()
async def smart(ctx): 
    await ctx.send(f'你的智商 :{random.randint(0,200)}')
    
@bot.command()
async def stupid(ctx): 
    await ctx.send(f'你今天的運氣是:{random.randint(0,200)}點')

@bot.command()
async def n(ctx, nhen):
    await ctx.send(F'https://nhentai.net/g/{nhen}/')   

@bot.command()
@commands.is_owner()
async def dm_user(ctx, id: int, *, text):
    user = await bot.fetch_user(id)
    await user.create_dm()
    await user.dm_channel.send(text)
    dm_user=discord.Embed(title='私訊', color=0x00ff40)
    dm_user.add_field(name='私訊人', value=f'{user.mention}', inline=False)
    dm_user.add_field(name='訊息', value=f'{text}', inline=False)
    await ctx.send(embed=dm_user)

@bot.command()
@commands.is_owner()
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=rename_to)
            print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
    print ("Action Completed: rall")

@bot.command()
@commands.is_owner()
async def mall(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"已寄送訊息給{user.name}")
        except:
            print(f"無法寄送訊息給{user.name}")
    print("完成寄送訊息")


@bot.command()
@commands.is_owner()
async def kick(ctx, member, reason):
    await ctx.send('是否確定踢出該成員？kick yes 或是 no')

    msg = await bot.wait_for('message')

    if msg.content == 'yes':
        await member.kick(reason=reason) 
        await ctx.send('成功')
    else:
        await ctx.send('取消')
        pass


@bot.command()
async def rn(ctx):
    hentai=random.randint(0,330156)
    await ctx.send(F'https://nhentai.net/g/{hentai}/')   


bot.run('NjI0OTk0ODQ3MjY2NDM5MTcw.XYZFzw.yIymgYZhxqMKIaeWkFpsfW1liTI')