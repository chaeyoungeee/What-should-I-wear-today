import requests
from bs4 import BeautifulSoup

def time_temperature(location, leave_time, home_time):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={location}+날씨정보"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    data1 = soup.find('div', {'class':'graph_inner _hourly_weather'})
    data2 = data1.find_all('dt', attrs={'class': 'time'})
    data3 = data1.find_all('span', attrs={'class': 'num'})

    a = []
    b = []

    for d in data2: # 시간 정보
        try:
            t = d.get_text()[:2]
            a.append(int(t))
        except:
            a.append(24)

    for d in data3: # 기온 정보
            t = list(d.get_text())
            t = t[:len(t)-1]
            b.append(int(''.join(t)))

    temp = [0] * len(a) # index: 시간, value: 기온

    for i in range(len(a)):
        temp[a[i]] = b[i]
        if a[i] == home_time: break

    return temp[leave_time:home_time+1] # 출발 시간에서 귀가 시간까지 기온 return