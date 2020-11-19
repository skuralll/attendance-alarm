# [yudete](https://github.com/yudete) / attendance-alarm
講義の開始時にメンションを飛ばし、アラームまで鳴らす Discord ボット

## 必要なもの
* [discord.py](https://discordpy.readthedocs.io/ja/latest/) *voice モジュール込み。*
    ```
    pip install discord.py[voice]
    ```
* [PyNaCl](https://pypi.org/project/PyNaCl/)
    ```sss
    pip install pynacl
    ```
* [PyYaml](https://pypi.org/project/PyYAML/)
    ```
    pip install pyyaml
    ```
* libffi-dev
    ```
    sudo apt install libffi-dev
    ```
* libnacl-dev
    ```
    sudo apt install libnacl-dev
    ```

## 動かし方
1. まず、`resource/config.example.yml` を `resources/config.yml` にコピーし、これを編集します。  
   Botのトークンや使用するチャンネルのID等を記述してください。
    ```yml
    # Bot Setting
    bot-token: Please-Replace-Here-To-Bot-Token #botのトークンをここに書いてください
    # Server Setting
    server-id: 0 #Server-ID
    server-channel-text: 0 #Alarm-Channel(Text)-ID
    server-channel-voice: 0 #Alarm-Channel(Voice)-ID
    #Dev Setting
    dev-debug-mode: false #debug-mode(true|false)
    dev-channel-text: 0 #Dev-Alarm-Channel(Text)-ID
    dev-channel-voice: 0 #Dev-Alarm-Channel(Text)-ID
    ```
1. 上記の「必要なもの」に従って、必須パッケージをインストールします。  
1. `python bot.py` 等で実行します。
    正常な動作にはソースコード中のチャンネルIDやロールIDが稼働させるサーバー内のものと一致している必要があるため、多くの改変が必要になる場合があります。

## このリポジトリの構造
* [bot.py](https://github.com/yudete/attendance-alarm/blob/main/bot.py)  
ボット本体のソースコード。
* [attendance-alarm.service](https://github.com/yudete/attendance-alarm/blob/main/attendance-alarm.service)  
Systemd 向けのユニットファイル。Linux 等でデーモン化する際に使用します。
* [resources](https://github.com/yudete/attendance-alarm/blob/main/resource)  
設定ファイルや音声ファイルを入れるディレクトリ
    * [audio.wav](https://github.com/yudete/attendance-alarm/blob/main/resource/audio.wav)  
    アラームに使われる音声ファイル。
    * [logo.png](https://github.com/yudete/attendance-alarm/blob/main/resource/logo.png)  
    ファイル名を見なさい
    * [config.yml](https://github.com/yudete/attendance-alarm/blob/main/resource/config.yml)  
    トークンやチャンネルIDを設定するためのファイル

## ライセンス
このプロジェクトは画像や音声などのアセットファイルなどを除き、[MIT License](https://opensource.org/licenses/MIT)に従ってライセンスされています。
