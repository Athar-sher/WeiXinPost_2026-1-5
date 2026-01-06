import cityinfo, config
import time
from time import localtime
from requests import get, post
from datetime import datetime, date


# ---------- 微信 ----------
def get_access_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={config.app_id}&secret={config.app_secret}"
    return get(url).json()['access_token']


# ---------- 天气 ----------
def get_weather(province, city):
    city_id = cityinfo.cityInfo[province][city]["AREAID"]
    t = int(round(time.time() * 1000))
    headers = {
        "Referer": f"http://www.weather.com.cn/weather1d/{city_id}.shtml",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = f"http://d1.weather.com.cn/dingzhi/{city_id}.html?_={t}"
    response = get(url, headers=headers)
    response.encoding = "utf-8"
    weather_json = eval(response.text.split(";")[0].split("=")[-1])
    info = weather_json["weatherinfo"]
    return info["weather"], info["temp"], info["tempn"]


# ---------- 推送 ----------
moyu_resp = post("http://api.tianapi.com/moyu/index", params={"key": config.tian_api_key}).json()
if moyu_resp["code"] == 200 and moyu_resp["newslist"]:
    item = moyu_resp["newslist"][0]
else:
    item = {
        "content": "今日暂无摸鱼数据，喝杯热水继续打工！",
        "holidaycountdown": "距周末还有未知天",
        "tip": "冷知识：多喝水能缓解打工焦虑～"
    }

# ---------- 主入口 ----------
if __name__ == '__main__':
    accessToken = get_access_token()
    user = config.user
    province, city = config.province, config.city
    weather, max_t, min_t = get_weather(province, city)
    send_message(user, accessToken, city, weather, max_t, min_t)
    print("每日天气推送完成！")



