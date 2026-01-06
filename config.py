# 公众号配置
# 公众号appId
app_id = "wx5a98c2f0de8c4db8"
# 公众号appSecret
app_secret = "bfe6a4efcad4f6e1e40c9a54e15ce79c"
# 模板消息id
# 每日消息
template_id1 = "55U3skkejHlOuM8ftZ3K84aXhx7qiayzS7q8lzw74lk"
# 课程消息,上课提醒
template_id2 = "loe1yHWr************************************"
# 晚安心语
template_id3 = "oGzGz2B-cC2AXyHf4s_DKQpddsC0"
# 接收公众号消息的微信号
# 微信用户配置（必填！）
user = ["沧桑男人"]  # 从测试号页面复制的用户微信号
# 信息配置
# 所在省份
province = "江苏"
# 所在城市
city = "南京"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2001-9-26"
# 在一起的日子，格式同上------------计时器
love_date = "2024-8-15"
# 天行数据晚安心语 key
good_Night_Key = "4a1255b8e8997ca96df20a7ecd78304f"
# 日期相关配置
year = 2025               # 当前年份（或留空用系统时间）
post_Time = "08:00"       # 推送时间（之前漏的也可能没写）
# ========== 课程表（不需要就留空或False） ==========
ENABLE_CLASS_PUSH = False
CLASS_SCHEDULE = {}      # 留空即可
# ===== 日期配置（必须） =====
year  = 2025
month = 1
day   = 6
post_Time = "08:00"
# -------------------------------------------------------------------------
# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}








