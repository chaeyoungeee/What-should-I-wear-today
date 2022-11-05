import discord
from discord.ui import Button, View
from discord.ext import commands
import time

user = [0]
information = [None, None]

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
    view = View()

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

    view.add_item(less)
    view.add_item(default)
    view.add_item(more)
    await ctx.send(embed=discord.Embed(title="더위를 많이 타는 편 인가요?", description=""),view=view)

# 외출 장소 선택 버튼
@bot.command()
async def where(ctx):
    view = View()

    gangnam = Button(label="강남구", emoji="🤍")
    async def gangnam_callback(interaction):
        information[0] = "gangnam"
        await interaction.response.send_message("###")
    gangnam.callback = gangnam_callback
    view.add_item(gangnam)

    gangdong = Button(label="강동구", emoji="🤍")
    async def gangdong_callback(interaction):
        information[0] = "gangdong"
        await interaction.response.send_message("###")
    gangdong.callback = gangdong_callback
    view.add_item(gangdong)

    gangbuk = Button(label="강북구", emoji="🤍")
    async def gangbuk_callback(interaction):
        information[0] = "gangbuk"
        await interaction.response.send_message("###")
    gangbuk.callback = gangbuk_callback
    view.add_item(gangbuk)

    gangseo = Button(label="강서구", emoji="🤍")
    async def gangseo_callback(interaction):
        information[0] = "gangseo"
        await interaction.response.send_message("###")
    gangseo.callback = gangseo_callback
    view.add_item(gangseo)

    gwanak = Button(label="관악구", emoji="🤍")
    async def gwanak_callback(interaction):
        information[0] = "gwanak"
        await interaction.response.send_message("###")
    gwanak.callback = gwanak_callback
    view.add_item(gwanak)

    gwangjin = Button(label="광진구", emoji="🤍")
    async def gwangjin_callback(interaction):
        information[0] = "gwangjin"
        await interaction.response.send_message("###")
    gwangjin.callback = gwangjin_callback
    view.add_item(gwangjin)

    guro = Button(label="구로구", emoji="🤍")
    async def guro_callback(interaction):
        information[0] = "guro"
        await interaction.response.send_message("###")
    guro.callback = guro_callback
    view.add_item(guro)

    geumcheon = Button(label="금천구", emoji="🤍")
    async def geumcheon_callback(interaction):
        information[0] = "geumcheon"
        await interaction.response.send_message("###")
    geumcheon.callback = geumcheon_callback
    view.add_item(geumcheon)

    nowon = Button(label="노원구", emoji="🤍")
    async def nowon_callback(interaction):
        information[0] = "nowon"
        await interaction.response.send_message("###")
    nowon.callback = nowon_callback
    view.add_item(nowon)

    dobong = Button(label="도봉구", emoji="🤍")
    async def dobong_callback(interaction):
        information[0] = "dobong"
        await interaction.response.send_message("###")
    dobong.callback = dobong_callback
    view.add_item(dobong)

    dongdaemun = Button(label="동대문구", emoji="🤍")
    async def dongdaemun_callback(interaction):
        information[0] = "dongdaemun"
        await interaction.response.send_message("###")
    dongdaemun.callback = dongdaemun_callback
    view.add_item(dongdaemun)

    dongjak = Button(label="동작구", emoji="🤍")
    async def dongjak_callback(interaction):
        information[0] = "dongjak"
        await interaction.response.send_message("###")
    dongjak.callback = dongjak_callback
    view.add_item(dongjak)

    mapo = Button(label="마포구", emoji="🤍")
    async def mapo_callback(interaction):
        information[0] = "mapo"
        await interaction.response.send_message("###")
    mapo.callback = mapo_callback
    view.add_item(mapo)

    seodaemun = Button(label="서대문구", emoji="🤍")
    async def seodaemun_callback(interaction):
        information[0] = "seodaemun"
        await interaction.response.send_message("###")
    seodaemun.callback = seodaemun_callback
    view.add_item(seodaemun)

    seocho = Button(label="서초구", emoji="🤍")
    async def seocho_callback(interaction):
        information[0] = "seocho"
        await interaction.response.send_message("###")
    seocho.callback = seocho_callback
    view.add_item(seocho)

    seongdong = Button(label="성동구", emoji="🤍")
    async def seongdong_callback(interaction):
        information[0] = "seongdong"
        await interaction.response.send_message("###")
    seongdong.callback = seongdong_callback
    view.add_item(seongdong)

    seongbuk = Button(label="성북구", emoji="🤍")
    async def seongbuk_callback(interaction):
        information[0] = "seongbuk"
        await interaction.response.send_message("###")
    seongbuk.callback = seongbuk_callback
    view.add_item(seongbuk)

    songpa = Button(label="송파구", emoji="🤍")
    async def songpa_callback(interaction):
        information[0] = "songpa"
        await interaction.response.send_message("###")
    songpa.callback = songpa_callback
    view.add_item(songpa)

    yangcheon = Button(label="양천구", emoji="🤍")
    async def yangcheon_callback(interaction):
        information[0] = "yangcheon"
        await interaction.response.send_message("###")
    yangcheon.callback = yangcheon_callback
    view.add_item(yangcheon)

    youngdeungpo = Button(label="영등포구", emoji="🤍")
    async def youngdeungpo_callback(interaction):
        information[0] = "youngdeungpo"
        await interaction.response.send_message("###")
    youngdeungpo.callback = youngdeungpo_callback
    view.add_item(youngdeungpo)

    yongsan = Button(label="용산구", emoji="🤍")
    async def yongsan_callback(interaction):
        information[0] = "yongsan"
        await interaction.response.send_message("###")
    yongsan.callback = yongsan_callback
    view.add_item(yongsan)

    eunpyeong = Button(label="은평구", emoji="🤍")
    async def eunpyeong_callback(interaction):
        information[0] = "eunpyeong"
        await interaction.response.send_message("###")
    eunpyeong.callback = eunpyeong_callback
    view.add_item(eunpyeong)

    jongro = Button(label="종로구", emoji="🤍")
    async def jongro_callback(interaction):
        information[0] = "jongro"
        await interaction.response.send_message("###")
    jongro.callback = jongro_callback
    view.add_item(jongro)

    jung = Button(label="중구", emoji="🤍")
    async def jung_callback(interaction):
        information[0] = "jung"
        await interaction.response.send_message("###")
    jung.callback = jung_callback
    view.add_item(jung)

    jungrang = Button(label="중랑구", emoji="🤍")
    async def jungrang_callback(interaction):
        information[0] = "jungrang"
        await interaction.response.send_message("###")
    jungrang.callback = jungrang_callback
    view.add_item(jungrang)

    await ctx.send(embed=discord.Embed(title="외출하실 장소를 선택해주세요!", description=""),view=view)

bot.run(token)
