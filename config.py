# ========== 微信测试号 ==========
app_id     = "wx5a98c2f0de8c4db8"
app_secret = "bfe6a4efcad4f6e1e40c9a54e15ce79c"
user       = ["oGzGz2B-cC2AXyHf4s_DKQpddsC0"]          # 从测试号后台「用户列表」复制

# ========== 天气 ==========
tian_api_key = "4a1255b8e8997ca96df20a7ecd78304f"                  # 天行数据 key（源码里其实没用，保留即可）
province     = "江苏"                 # 必须写「省份」拼音或汉字，cityinfo 字典需要
city         = "南京"                 # 城市名（不带“市”）

# ========== 日期/推送时间 ==========
year           = 2025
month          = 1
day            = 6
post_Time      = "08:00"              # 每日天气推送时间
good_Night_Time = "23:00"             # 晚安心语推送时间

# ========== 模板ID（创建后填写） ==========
template_id1 = "5QYzukhL9PwdlSKFymriTIL8IDLXtQgxgJJwECoZvOE"   # 每日天气
template_id2 = ""   # 课程提醒
template_id3 = "Jdccz053D2DWFCKviTqBUjjRLxoXqgt-vyp7BvDxGZs"   # 晚安心语

# ========== 恋爱/生日倒计时 ==========
love_date = "2024-01-01"   # 格式 yyyy-mm-dd
birthday  = "2000-01-01"   # 生日（只用于倒计时，年份随意）

# ========== 课程表（不需要就留空或 False） ==========
ENABLE_CLASS_PUSH = False
classes = {}               # 空字典即可，源码里会判空

# 上课提醒时间轴（6 节课示例，可改）
time_table  = ["08:00:00", "09:00:00", "10:00:00",
               "14:00:00", "15:00:00", "16:00:00"]
course_Time = ["08:00", "09:00", "10:00",
               "14:00", "15:00", "16:00"]

# ========== 天行数据晚安心语接口 ==========
good_Night_Key = "4a1255b8e8997ca96df20a7ecd78304f"   # 去天行数据申请「晚安心语」接口后填 key

# ===== 情绪价值增强 =====
wind   = "西风 4-5级"       # 可继续用原接口字段，也可自定义
luck   = "幸运色：雾霾蓝｜贵人方位：东南"
tips   = "多云转凉，外套+围巾最稳妥"
note   = "周三小周末，喝杯热拿铁再出发～"



