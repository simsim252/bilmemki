import discord

from discord.ext import commands

from bot_mantik import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))


bot.run("MTE4MzA5NTYyMjM1MDQwNTgyMw.GXxW3x.yyB0tnGO8Nr7Dzbi8USnlwXMSSs9Ir-4ruMOSk")