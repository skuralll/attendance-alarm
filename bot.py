# coding: utf-8

# import
import discord
from discord.ext import tasks
from datetime import datetime
import os
import yaml

# リソースの読み込み
AUDIO_PATH = os.getcwd() + os.path.sep + "resources" + os.path.sep + "audio.wav"

# クライアントオブジェクトを生成
client = discord.Client()
# 設定ファイルの読み込み
path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "config.yml"
with open(path, 'r', encoding="utf-8") as file:
    ymlobj = yaml.safe_load(file)
    # 一般的な設定項目
    TOKEN = ymlobj['bot-token']
    GUILD_ID = ymlobj['server-id']
    CHANNEL_TEXT = ymlobj['server-channel-text']
    CHANNEL_VOICE = ymlobj['server-channel-voice']
    DEV_DEBUG_MODE = ymlobj['dev-debug-mode']
    DEV_CHANNEL_TEXT = ymlobj['dev-channel-text']
    DEV_CHANNEL_VOICE = ymlobj['dev-channel-text']  # not implemented
    TEMPLATE = ymlobj['template']  # 通知メッセージのテンプレート
    PLAYING = ymlobj['playing']
    STOPPED = ymlobj['stopped']
    DISCONNECTED = ymlobj['disconnected']

# 時間割定義(仮置) # TODO:時間割設定ファイルを作成、そこから読み込むようにする
timetable = [
    [    # 月曜日
        {'time': '09:00', 'role': 0},
        {'time': '10:40', 'role': 0},
        {'time': '13:00', 'role': 0},
        {'time': '14:40', 'role': 0},
        {'time': '16:20', 'role': 0}
    ],
    [    # 火曜日
        {'time': '09:00', 'role': 0},
        {'time': '10:40', 'role': 0},
        {'time': '13:00', 'role': 0},
        {'time': '14:40', 'role': 0},
        {'time': '16:20', 'role': 0}
    ],
    [    # 水曜日
        {'time': '09:00', 'role': 0},
        {'time': '10:40', 'role': 0},
        {'time': '13:00', 'role': 0},
        {'time': '14:40', 'role': 0},
        {'time': '16:20', 'role': 0}
    ],
    [    # 木曜日
        {'time': '09:00', 'role': 0},
        {'time': '10:40', 'role': 0},
        {'time': '13:00', 'role': 0},
        {'time': '14:40', 'role': 0},
        {'time': '16:20', 'role': 0}
    ],
    [    # 金曜日
        {'time': '09:00', 'role': 0},
        {'time': '10:40', 'role': 0},
        {'time': '13:00', 'role': 0},
        {'time': '14:40', 'role': 0},
        {'time': '16:20', 'role': 0}
    ],
    [],  # 土曜日
    [    # 日曜日
        {'time': '07:11', 'role': 0},
        {'time': '07:12', 'role': 0},
        {'time': '07:13', 'role': 0},
    ]
]
DAY_NAMES = ["月", "火", "水", "木", "金", "土", "日"]
# デバッグ用曜日
DEV_DAY = 6

# DEV_DEBUG_MODE が有効だった場合、ボットの起動時に config を表示する
if DEV_DEBUG_MODE:
    print("> ボットの設定 ▼")
    print("> TOKEN: " + TOKEN)
    print("> GUILD_ID: " + str(GUILD_ID))
    print("> CHANNEL_TEXT: " + str(CHANNEL_TEXT))
    print("> CHANNEL_VOICE: " + str(CHANNEL_VOICE))
    print("> DEV_CHANNEL_TEXT: " + str(DEV_CHANNEL_TEXT))
    print("> DEV_CHANNEL_VOICE: " + str(DEV_CHANNEL_VOICE))

# グローバル変数の初期化
voice = None
player = None


# 起動通知
@client.event
async def on_ready():
    print("ボットを起動しました。discord.py バージョン", discord.__version__)  # 起動確認メッセージ
    if PLAYING is not None:
        await client.change_presence(activity=discord.Game(name=PLAYING))  # __ をプレイ中


# メッセージ受信時
@client.event
async def on_message(message):
    pass  # 一時的にデバッグモード削除(処理変更のため)


# タスク
@tasks.loop(seconds=1)
async def loop():
    if client.is_ready():
        weekday = DEV_DAY if DEV_DEBUG_MODE else datetime.now().weekday()  # デバッグモードなら曜日はDEV_DAYに設定
        now = datetime.now().strftime('%H:%M')
        for lesson in range(len(timetable[weekday])):  # その日のコマ数分ループさせる
            if timetable[weekday][lesson]['time'] == now:  # lessonコマ目の開始時刻が現在の時刻と一致していたら
                global voice, player  # グローバル変数であることを明示
                await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role=timetable[weekday][lesson]['role'], weekday=DAY_NAMES[weekday], time=(lesson+1)))  # 出席通知を送信
                break


# ループ開始
loop.start()

client.run(TOKEN)
