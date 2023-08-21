import requests
from bs4 import BeautifulSoup


#A request is made to the url;
#the response for horoscope is parsed using Beautiful Soup,
#and the <p> data is returned within <div class="main-horoscope"></div>
#from the website being scraped from
def getHoroscopeByDay(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def getHoroscopeByWeek(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def getHoroscopeByMonth(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def getChineseHoroscopeByDay(animal, day):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/chinese/horoscope-chinese-daily-{day}.aspx?sign={animal}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def getChineseHoroscopeByWeek(animal):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/chinese/horoscope-chinese-weekly.aspx?sign={animal}")
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find("div", attrs={"class": "main-horoscope"})
    return data.p.text


def getChineseHoroscopeByMonth(animal):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/chinese/horoscope-chinese-monthly.aspx?sign={animal}")
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find("div", attrs={"class": "main-horoscope"})
    return data.p.text
