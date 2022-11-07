import discord
from discord.ui import Button, View
from discord.ext import commands
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawling import temperature_crawling

user = [0] # 더위 타는 정도
information = [None, None, None] # 외출 장소, 출발 시간, 귀가 시간
clothes = [ # 외투, 상의, 하의, 악세사리
            [None, ("민소매", "반팔티"), ("반바지"), None], # 0
            [None, ("반팔티","반팔 셔츠"), ("반바지", "린넨 바지"), None], # 1
            [("얇은 가디건"), ("반팔티", "반팔 니트"), ("면바지", "청바지"), None], # 2
            [("얇은 가디건"), ("셔츠", "긴팔티"), ("청바지", "얇은 슬랙스"), ("캡모자")], # 3
            [("가디건"), ("얇은 니트", "맨투맨", "긴팔티"), ("청바지", "얇은 슬랙스"), ("캡모자")], # 4
            [("가디건", "면자켓"), ("맨투맨", "후드티", "니트"), ("청바지", "슬랙스"), ("캡모자")], #5
            [("바람막이", "청자켓", "항공 점퍼"), ("후드티", "니트"), ("슬랙스"), ("비니")], # 6
            [("가죽 자켓", "트렌치 코트", "야상"), ("후드티", "니트"), ("슬랙스", "히트텍"),("비니")], # 7,
            [("코트","가죽 자켓", "플리스"), ("기모 맨투맨", "기모 후드티", "울니트"), ("기모 바지", "히트텍"), ("장갑")], # 8
            [("코트", "숏패딩", "양털 자켓", "플리스"), ("기모 후드티", "기모 맨투맨", "울니트", "히트텍"), ("기모 바지", "히드텍"), ("장갑", "귀마개")], # 9
            [("롱패딩", "울코트", "털 플리스", "패딩 조끼"), ("융털 후드티", "융털 맨투맨", "울니트", "히트텍"), ("기모 바지", "히트텍"), ("장갑", "귀마개", "털모자")] # 10
]

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
        user[0] = 2
        await interaction.response.send_message("외출할 때 입을 옷을 추천해드릴게요")
        await where(ctx)

    async def default_callback(interaction):
        user[0] = 0
        await interaction.response.send_message("외출할 때 입을 옷을 추천해드릴게요")
        await where(ctx)

    async def more_callback(interaction):
        user[0] = -2
        await interaction.response.send_message("외출할 때 입을 옷을 추천해드릴게요")
        await where(ctx)

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
        information[0] = "강남구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gangnam.callback = gangnam_callback
    view.add_item(gangnam)

    gangdong = Button(label="강동구", emoji="🤍")
    async def gangdong_callback(interaction):
        information[0] = "강동구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gangdong.callback = gangdong_callback
    view.add_item(gangdong)

    gangbuk = Button(label="강북구", emoji="🤍")
    async def gangbuk_callback(interaction):
        information[0] = "강북구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gangbuk.callback = gangbuk_callback
    view.add_item(gangbuk)

    gangseo = Button(label="강서구", emoji="🤍")
    async def gangseo_callback(interaction):
        information[0] = "강서구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gangseo.callback = gangseo_callback
    view.add_item(gangseo)

    gwanak = Button(label="관악구", emoji="🤍")
    async def gwanak_callback(interaction):
        information[0] = "관악구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gwanak.callback = gwanak_callback
    view.add_item(gwanak)

    gwangjin = Button(label="광진구", emoji="🤍")
    async def gwangjin_callback(interaction):
        information[0] = "광진구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    gwangjin.callback = gwangjin_callback
    view.add_item(gwangjin)

    guro = Button(label="구로구", emoji="🤍")
    async def guro_callback(interaction):
        information[0] = "구로구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    guro.callback = guro_callback
    view.add_item(guro)

    geumcheon = Button(label="금천구", emoji="🤍")
    async def geumcheon_callback(interaction):
        information[0] = "금천구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    geumcheon.callback = geumcheon_callback
    view.add_item(geumcheon)

    nowon = Button(label="노원구", emoji="🤍")
    async def nowon_callback(interaction):
        information[0] = "노원구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    nowon.callback = nowon_callback
    view.add_item(nowon)

    dobong = Button(label="도봉구", emoji="🤍")
    async def dobong_callback(interaction):
        information[0] = "도봉구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    dobong.callback = dobong_callback
    view.add_item(dobong)

    dongdaemun = Button(label="동대문구", emoji="🤍")
    async def dongdaemun_callback(interaction):
        information[0] = "동대문구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    dongdaemun.callback = dongdaemun_callback
    view.add_item(dongdaemun)

    dongjak = Button(label="동작구", emoji="🤍")
    async def dongjak_callback(interaction):
        information[0] = "동작구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    dongjak.callback = dongjak_callback
    view.add_item(dongjak)

    mapo = Button(label="마포구", emoji="🤍")
    async def mapo_callback(interaction):
        information[0] = "마포구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    mapo.callback = mapo_callback
    view.add_item(mapo)

    seodaemun = Button(label="서대문구", emoji="🤍")
    async def seodaemun_callback(interaction):
        information[0] = "서대문구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    seodaemun.callback = seodaemun_callback
    view.add_item(seodaemun)

    seocho = Button(label="서초구", emoji="🤍")
    async def seocho_callback(interaction):
        information[0] = "서초구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    seocho.callback = seocho_callback
    view.add_item(seocho)

    seongdong = Button(label="성동구", emoji="🤍")
    async def seongdong_callback(interaction):
        information[0] = "성동구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    seongdong.callback = seongdong_callback
    view.add_item(seongdong)

    seongbuk = Button(label="성북구", emoji="🤍")
    async def seongbuk_callback(interaction):
        information[0] = "성북구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    seongbuk.callback = seongbuk_callback
    view.add_item(seongbuk)

    songpa = Button(label="송파구", emoji="🤍")
    async def songpa_callback(interaction):
        information[0] = "송파구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    songpa.callback = songpa_callback
    view.add_item(songpa)

    yangcheon = Button(label="양천구", emoji="🤍")
    async def yangcheon_callback(interaction):
        information[0] = "양천구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    yangcheon.callback = yangcheon_callback
    view.add_item(yangcheon)

    youngdeungpo = Button(label="영등포구", emoji="🤍")
    async def youngdeungpo_callback(interaction):
        information[0] = "영등포구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    youngdeungpo.callback = youngdeungpo_callback
    view.add_item(youngdeungpo)

    yongsan = Button(label="용산구", emoji="🤍")
    async def yongsan_callback(interaction):
        information[0] = "용산구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    yongsan.callback = yongsan_callback
    view.add_item(yongsan)

    eunpyeong = Button(label="은평구", emoji="🤍")
    async def eunpyeong_callback(interaction):
        information[0] = "은평구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    eunpyeong.callback = eunpyeong_callback
    view.add_item(eunpyeong)

    jongro = Button(label="종로구", emoji="🤍")
    async def jongro_callback(interaction):
        information[0] = "종로구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    jongro.callback = jongro_callback
    view.add_item(jongro)

    jung = Button(label="중구", emoji="🤍")
    async def jung_callback(interaction):
        information[0] = "중구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    jung.callback = jung_callback
    view.add_item(jung)

    jungrang = Button(label="중랑구", emoji="🤍")
    async def jungrang_callback(interaction):
        information[0] = "중랑구"
        await interaction.response.send_message(embed=discord.Embed(title="출발시간과 귀가시간을 입력해주세요!", description="?when 출발시간 도착시간\n(ex)?when 9 19"))
    jungrang.callback = jungrang_callback
    view.add_item(jungrang)

    await ctx.send(embed=discord.Embed(title="외출하실 장소를 선택해주세요!", description=""),view=view)

# 출발 시간, 귀가 시간 입력
@bot.command()
async def when(ctx, arg1, arg2):
    if int(arg1) < time.localtime().tm_hour or int(arg2) < int(arg1) or int(arg1) > 24 or int(arg2) > 24 or int(arg1) < 0 or int(arg2) < 0:
        await ctx.send("시간을 잘못 입력했어요! 다시 입력해주세요.")
    else:
        information[1], information[2] = int(arg1), int(arg2)

    await what(ctx)

@bot.command()
async def what(ctx):
    await ctx.send(information[0])
    await ctx.send(information[1])
    await ctx.send(information[2])
    temp = temperature_crawling.time_temperature(information[0], information[1], information[2]) # 기온 정보 크롤링
    temp_avg = sum(temp) / len(temp) # 외출 시간 동안 기온 평균
    user_temp = temp_avg + user[0]  # 사용자 고려 기온
    print(*temp)

bot.run(token)
