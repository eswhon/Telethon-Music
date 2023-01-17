import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5016118641:AAESG4JAST4g2Koe24ff3d-_Fu9QWDf76iM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGkBu5sAch4vbdT8NUEZC22pfXLduhq4_V-5GxYwaMX-UqHrfeJ-qY13l1e_X4e8nrljS6Nzcm4ChX77SjGf7lkxle6uKBKshgsUxz5dA0XsVbwtUa2rE_lTdIpJFbfmx-Tf5WVWAoyBQrdOIFbHNmuDvfALfZTxgvfBZRDnuWDneuzXpSQIGoZwNV_CuTAmnR320OF_hTzRiiEf8iZ8nsaSj01lvEZrnbNSTCaVmYcxL5WtRDhDPU7KXuDxvkusH9r1ND7YWMq13vJEMG3mk-hXDQE9ouLhJREeeRpU14Px22u0RbzgQG37iIOiy6dsUjjPfMQxhNTcqd6mxvQfDeTdI9U=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "streaming_robot")
    SUPPORT = os.environ.get("SUPPORT", "TodayExecution") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "souwon") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5762134341")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
