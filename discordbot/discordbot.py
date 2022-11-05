import discord
from discord.ui import Button, View
from discord.ext import commands

user = [0]
info = [[None, None, None], None, None]

token = ''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

# 더위 타는 정도 버튼
@bot.command()
async def info(ctx):
    less = Button(label="덜 타요", emoji="🤍")
    default = Button(label="보통이에요", emoji="🤍")
    more = Button(label="더 타요", emoji="🤍")

    async def less_callback(interaction):
        user[0] = -2
        await interaction.response.send_message("1")

    async def default_callback(interaction):
        user[0] = 0
        await interaction.response.send_message("1")

    async def more_callback(interaction):
        user[0] = 2
        await interaction.response.send_message("1")

    less.callback = less_callback
    default.callback = default_callback
    more.callback = more_callback

    view = View()
    view.add_item(less)
    view.add_item(default)
    view.add_item(more)
    await ctx.send(embed=discord.Embed(title="더위를 많이 타는 편 인가요?", description=""),view=view)
bot.run(token)