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
def send_message(to_user, access_token, city, weather, max_t, min_t):
    url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}"
    today = date.today()
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week = week_list[today.weekday()]

    data = {
        "touser": to_user[0],
        "template_id": config.template_id1,
        "data": {
            "date": {"value": f"{today} {week}", "color": "#00FFFF"},
            "city": {"value": city, "color": "#808A87"},
            "weather": {"value": weather, "color": "#ED9121"},
            "max_temperature": {"value": max_t, "color": "#FF6100"},
            "min_temperature": {"value": min_t, "color": "#00FF00"}
        }
    }
    resp = post(url, json=data)
    print("微信回执：", resp.text)


# ---------- 主入口 ----------
if __name__ == '__main__':
    accessToken = get_access_token()
    user = config.user
    province, city = config.province, config.city
    weather, max_t, min_t = get_weather(province, city)
    send_message(user, accessToken, city, weather, max_t, min_t)
    print("每日天气推送完成！")
