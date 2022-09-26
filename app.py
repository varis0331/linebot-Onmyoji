from cgitb import text
from email.errors import NonPrintableDefect
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import random
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('i5jy7al+qSzvaSCGMzMfC7s2ZnmTTutWrHVtDnPKtdupii8rT/IDosCp0RofDo7cxXtFwt2q6LUroGrjr7gZo/GCjdQhlnl6Bka81KrVkqJ5LMZ8zCpVEEtIEK/7317HgmjSGrfejsTkllTXxPMwAgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8471fca35983b5bb8b346de831e46275')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#======讓heroku不會睡著======

import threading 
import requests
def wake_up_heroku():
    while 1==1:
        url = 'https://varis-linebot01.herokuapp.com/' + 'heroku_wake_up'
        res = requests.get(url)
        if res.status_code==200:
            print('喚醒heroku成功')
        else:
            print('喚醒失敗')
        time.sleep(28*60)

threading.Thread(target=wake_up_heroku).start()

#======讓heroku不會睡著======

# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '用戶訊息' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '逢魔'==msg in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)

#=====抽獎=====

    elif '抽獎' == msg :
        message = random.choice("pk","kp")
        line_bot_api.reply_message(event.reply_token,message)


#=====關鍵字查詢=====

    elif '關鍵字' == msg or '查詢關鍵字' in msg or '關鍵字查詢'  == msg :
   
        message = TextMessage(text="知憲負責的業務有以下關鍵字可提供查詢:\n\n1.請善用遊戲中神秘懸賞的關鍵字\n\n2.圖片關鍵字:多喝熱水、每日任務、每周任務、離譜、大雄、海豹、瞎狗眼、好慘喔、si、大佬\n\n3.影片關鍵字:c8\n\n4.關懷八尬小可愛:拉屎、拉完了是不是\n\n5.陰陽師活動關鍵字:活動\n\n6.逢魔關鍵字:電腦板請查詢逢魔pc，手機板請查詢逢魔")
        line_bot_api.reply_message(event.reply_token, message)

#=====圖片訊息=====

    elif '多喝熱水' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/RZmtbkc.jpg",
            preview_image_url="https://i.imgur.com/RZmtbkc.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '每日任務' == msg or '每日' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/Yssopll.jpg",
            preview_image_url="https://i.imgur.com/Yssopll.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '每周任務' == msg or '每週任務'== msg or '每周' == msg or '每週' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/TCA3L4i.jpg",
            preview_image_url="https://i.imgur.com/TCA3L4i.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '離譜' in msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/a7UHYCQ.jpg",
            preview_image_url="https://i.imgur.com/a7UHYCQ.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '大雄' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/PoiPLp2.jpg",
            preview_image_url="https://i.imgur.com/PoiPLp2.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '海豹' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/vzySAJW.jpg",
            preview_image_url="https://i.imgur.com/vzySAJW.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '瞎了狗眼' == msg or '瞎狗眼' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/4HB9uRk.jpg",
            preview_image_url="https://i.imgur.com/4HB9uRk.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '好慘喔' == msg or '好慘哦' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/RwGPuzG.jpg",
            preview_image_url="https://i.imgur.com/RwGPuzG.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif 'si' == msg or 'Si' == msg or 'SI' == msg or 'sI' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/XkDJPgl.jpg",
            preview_image_url="https://i.imgur.com/XkDJPgl.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '大佬' == msg :
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/SydpJHU.jpg",
            preview_image_url="https://i.imgur.com/SydpJHU.jpg")
        line_bot_api.reply_message(event.reply_token, message)
    elif '？'== msg or '問號' == msg:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/BF2HabK.jpg",
            preview_image_url="https://i.imgur.com/BF2HabK.jpg")
        line_bot_api.reply_message(event.reply_token, message)

#=====圖片訊息=====

#=====影片訊息=====

    elif 'C8' == msg or 'c8' ==msg or '西八' == msg:
        message = VideoSendMessage(
            original_content_url='https://i.imgur.com/5KLaZUp.mp4',
            preview_image_url='https://i.imgur.com/BPgTN1Z.jpg')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '汗' == msg:
        message = VideoSendMessage(
            original_content_url='https://i.imgur.com/fBtRb7s.mp4',
            preview_image_url='https://i.imgur.com/JdwRclO.jpg')
        line_bot_api.reply_message(event.reply_token, message)

#=====八尬語錄=====

    elif '拉屎' == msg or '八尬要拉屎' in msg :
        message = TextMessage(text="記得查廁紙...避免拉屎又沒紙")
        line_bot_api.reply_message(event.reply_token, message)
    elif '拉完了是不是' == msg or '拉完了484' == msg :
        line_bot_api.reply_message(event.reply_token, [TextMessage(text="記得用紙,擦屁股"),TextMessage(text="但要先有紙")]) 
        
#=====寮任提醒=====
    elif '寮任' == msg :
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/NvxBwxX.jpg",
            preview_image_url="https://i.imgur.com/NvxBwxX.jpg")
        line_bot_api.reply_message(event.reply_token, message)

#=====活動更新專區=====
    elif '活動' == msg :
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/XX141Jr.jpg",
            preview_image_url="https://i.imgur.com/XX141Jr.jpg")
        line_bot_api.reply_message(event.reply_token, message)

# api限制圖片五張
    # elif '活動' == msg  in msg :
    #     line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/Ts54RZn.jpg',preview_image_url='https://i.imgur.com/Ts54RZn.jpg'),
    #                                                     ImageSendMessage(original_content_url='https://i.imgur.com/dunNcxU.jpg',preview_image_url='https://i.imgur.com/dunNcxU.jpg'),
    #                                                     ImageSendMessage(original_content_url='https://i.imgur.com/sChi5L6.jpg',preview_image_url='https://i.imgur.com/sChi5L6.jpg')])

#=====逢魔攻略專區=====

    elif '逢魔pc' == msg or '逢魔PC' == msg:
        message = TextMessage(text="親估唷~知憲想問你要查哪一個?\n鬼靈歌伎、荒骷髏、蜃氣樓、地震鯰，還是土蜘蛛,或者朧車呢?")
        line_bot_api.reply_message(event.reply_token, message)
    elif '鬼靈歌伎' == msg  in msg :
        line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/3SEkPO9.jpg',preview_image_url='https://i.imgur.com/3SEkPO9.jpg'), 
                                                        ImageSendMessage(original_content_url='https://i.imgur.com/3PZAnT5.jpg',preview_image_url='https://i.imgur.com/3PZAnT5.jpg')])
    elif '荒骷髏' == msg  in msg :    
        line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/U5bWN5j.jpg',preview_image_url='https://i.imgur.com/U5bWN5j.jpg'), 
                                                        ImageSendMessage(original_content_url='https://i.imgur.com/LpDGoje.jpg',preview_image_url='https://i.imgur.com/LpDGoje.jpg')])
    elif '土蜘蛛' == msg  in msg :
        line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/xcB9lSU.jpg',preview_image_url='https://i.imgur.com/xcB9lSU.jpg'), 
                                                        ImageSendMessage(original_content_url='https://i.imgur.com/POJxFOU.jpg',preview_image_url='https://i.imgur.com/POJxFOU.jpg')])
    elif '地震鯰' == msg  in msg :
        line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/jCsjZMQ.jpg',preview_image_url='https://i.imgur.com/jCsjZMQ.jpg'), 
                                                        ImageSendMessage(original_content_url='https://i.imgur.com/zYlcaUq.jpg',preview_image_url='https://i.imgur.com/zYlcaUq.jpg')])
    elif '蜃氣樓' == msg  in msg :
        line_bot_api.reply_message(event.reply_token,  [ImageSendMessage(original_content_url='https://i.imgur.com/rYWVYRp.jpg',preview_image_url='https://i.imgur.com/rYWVYRp.jpg'), 
                                                        ImageSendMessage(original_content_url='https://i.imgur.com/VBqpP9C.jpg',preview_image_url='https://i.imgur.com/VBqpP9C.jpg')])
    elif '朧車' == msg  in msg :
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/wM8WGiM.jpg",
            preview_image_url="https://i.imgur.com/wM8WGiM.jpg")
        line_bot_api.reply_message(event.reply_token, message)
        
#=====極土逢魔系列=====
    elif '極土' == msg :
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tJGsPNQ.png',
            preview_image_url='https://i.imgur.com/tJGsPNQ.png')
        line_bot_api.reply_message(event.reply_token, message)

    
#=====神秘懸賞資料=====

    elif '羽毛'== msg or'笛子'== msg or'扇'== msg or'大翅膀' == msg or'大天狗' == msg:
        message = TextMessage(text="大天狗\n線索：大翅膀/風/羽毛/笛子/扇\n\n【御魂】 巫女大蛇悲鳴帶1個，第十層帶2個，第四層帶1個;\n\n【第十八章】 第一個三尾狐帶1個，BOSS大天狗帶1個;\n\n【第十五章】提燈小僧3個 數量1個\n\n【暴風之巔】第一至第十層數量1個\n\n【傘劍的守護-第四層】數量1個")
        line_bot_api.reply_message(event.reply_token, message)
    elif '妖豔'== msg or'紅尾'== msg or'櫻花樹'== msg or'紅色' == msg:
        message = TextMessage(text="三尾狐\n線索：妖艷/紅尾/櫻花樹/紅色\n\n【暴風之巔】 一到四層各帶4個，五到六層各帶3個，第九層帶1個;\n\n【妖刀之秘籍】 第四層帶3個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '單眼'== msg or'石鎚'== msg or'怪力' == msg:
        message = TextMessage(text="山童\n線索：單眼/石鎚/怪力\n\n【山兔大暴走】 一到十層各帶3個;\n\n【第十六章】三個餓鬼各帶2個;\n\n【河畔童謠】第二層帶3個;\n\n【暴風之巔】 第三層帶3個; \n\n【狐生百魅】 第四層4隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '黑鐮'== msg or'短刀' == msg:
        message = TextMessage(text="鬼使黑\n線索：黑鐮/短刀\n\n【河畔童謠】  第六層帶3個;\n\n【第二十八章】  閰魔帶2個,面靈氣（覺醒後）帶1個;\n\n【第二十四章】  三個青姬各帶2個；\n\n【妖氣封印】  鬼使黑帶3個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '金剛經'== msg or'石菩薩' == msg:
        message = TextMessage(text="獨眼小僧\n線索：金剛經/石菩薩\n\n【第二十五章】第二個巫蠱師帶1個，第二個以津真天帶2個;\n\n【第十一章】第二個武士之靈帶3個，兩個獨眼小僧各帶2個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '花'== msg or'舞' == msg:
        message = TextMessage(text="桃花妖\n線索：花/舞 \n\n【御魂】 第三層帶1個; \n\n【妖刀之秘籍】 第六/十層各帶1個; \n\n【暴風之巔】 第八層各帶5個; \n\n【河畔童謠】 第五層帶1個，第十層帶2個；\n\n【雪之回憶】 第六層帶2隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '羽衣'== msg or'幼女' == msg or'童女' == msg:
        message = TextMessage(text="童女\n線索：翅膀/羽衣/幼女\n\n【第三章】最後一個天邪鬼黃帶3個;\n\n【荒川之怒】第二層帶3個;\n\n【第十二章】第一個童女帶1個，第二個童女帶3個，第二個童男帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '薙刀'== msg or'翅膀'== msg or'面具' == msg:
        message = TextMessage(text="鴉天狗\n線索：薙刀/翅膀/面具\n\n【荒川之怒】第四層帶4個;\n\n【暴風之巔】第五層帶4個;\n\n【山兔大暴走】第二層帶3個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '鬼火'== msg or'角'== msg or'財富'== msg or'幸運' == msg:
        message = TextSendMessage(text="座敷童子\n線索：鬼火/角/財富/幸運\n\n【雨女的等候】第一層帶3個;\n\n【第二十三章】兩個盜墓小鬼各帶2個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '海'== msg or'鬍鬚'== msg or'杖' == msg:
        message = TextMessage(text="海坊主\n線索：海/鬍鬚/杖\n\n【第二十七章推薦】  兩個金魚姬各帶3個, 兩個海坊主各帶1個;\n\n【第二十四章】  兩個吸血姬各帶3個;\n\n【妖氣封印】 海坊主帶3個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '紙扇'== msg or'書生' == msg:
        message = TextMessage(text="妖狐\n線索：紙扇/書生/面具\n\n【第七章】BOSS帶2個；\n\n【御魂】 第二層帶1個；\n\n【狐生百魅】 一到十層各帶1個；\n\n【暴風之巔】 第八層各帶4個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '鼓' == msg:
        message = TextMessage(text="天邪鬼黃\n線索：鼓\n\n【鮮血之月】第三層帶3個;\n\n【意志的覺醒】第一層帶3個;\n\n【妖氣封印】海坊主帶3個，椒圖帶2個，跳跳哥哥帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '人偶'== msg or'模擬' == msg:
        message = TextMessage(text="傀儡師\n線索: 人偶/模擬\n\n【第二十八章】  兩個傀儡師各帶3個;\n\n【第二十七章】  兩個海坊主各帶3個;\n\n【第十章】  兩個丑時之女各帶1個，兩個傀儡師各帶1個;\n\n【御魂】 第五層帶1個;\n\n【浪客遠道】 第三層帶7個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '釘耙'== msg or'錘' == msg:
        message = TextMessage(text="鐮鼬\n線索：錘/釘耙\n\n【御魂】 第五層帶1個; \n\n【河畔童謠】 第四層帶1個; \n\n【夏之風物師】 第七層帶2個;第十層帶3個;\n\n【安夢奇緣】 第六層3隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '劍'== msg or'堅甲'== msg or'石化' == msg:
        message = TextMessage(text="兵俑\n線索：劍/堅甲/石化\n\n【雨女的等候】 第七層帶4個;\n\n【第二十一章】 第二個煙煙羅帶1個，第二三個食髮鬼各帶1個;\n\n【第二十五章】 三個兵俑各帶1個;\n\n【安夢奇緣】 第五層3隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '鈴鐺'== msg or'噩夢' == msg:
        message = TextMessage(text="食夢貘\n線索：鈴鐺/噩夢\n\n【第十四章】 最後一個塗壁帶1個，BOSS食夢貘帶5個;\n\n【御魂】 第四層帶2個，第九層帶1個;\n\n【安夢奇緣】 第一層5隻;\n\n【浪客遠道】 第一層6隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '青皮膚'== msg or'風箏' == msg:
        message = TextMessage(text="天邪鬼青\n【第二章】BOSS座敷童子帶1個;\n\n【第五章】BOSS食發鬼帶2個;\n\n【第六章】兩個天邪鬼青各帶1個;\n\n【第八章】兩個天邪鬼綠各帶1個，BOSS桃花妖帶1個;\n\n【第十章 推薦】兩個丑時之女各帶2個;\n\n【第十一章】BOSS鬼女紅葉帶2個;\n\n【禦魂第一層】第一回合1個;\n\n【妖氣封印】二口女帶3個，海坊主帶1個，跳跳哥哥帶3個;\n\n【妖刀之秘笈 推薦】一到三層各帶4個，四到九層各帶3個，十層帶2個;\n\n【夏之風物詩】第四層帶3個，第五層帶1個;\n\n【意志的覺醒】第二層帶3個;\n\n【海怪的溫柔】第五層帶1個;\n\n【青燈百物語】第四層帶2個;\n\n【鮮血之月】第三層帶2個;\n\n【狐生百魅】第五層帶3個；\n\n【挑戰副本】第九章天邪鬼青帶14個，做任務有點浪費，不推薦。")
        line_bot_api.reply_message(event.reply_token, message)
    elif '石'== msg or'牆'== msg or'青苔'== msg or'石牆' == msg:
        message = TextMessage(text="塗壁\n線索：石/牆/青苔\n\n【第十四章】 三個塗壁各帶6個;\n\n【山兔大暴走】 一到九層各帶4個，第十層帶3個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '水球'== msg or'水流'== msg or'荷葉' == msg:
        message = TextMessage(text="河童\n線索:水球/水流/荷葉\n\n【第二十三章】 兩個盜墓小鬼各帶1個;\n\n【第二十七章】 鯉魚精帶3個, 兩個河童各帶1個;\n\n【荒川之怒】 四到六層各帶3個;\n\n【夏之風物詩】七層帶4個;\n\n【雨女的等候】八層帶5個;\n\n【海怪的溫柔】 第三和五層5隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '治癒'== msg or'蒲公英' == msg:
        message = TextMessage(text="螢草\n線索：蒲公英/治愈/叮\n\n【業原火】帶4個，三種難度一樣;\n\n【第二十三章】BOSS螢草帶3個；\n\n【御魂】第二/九/十層各帶1個；\n\n【山兔大暴走】第一四七各帶2個；\n\n【暴風之巔】第七層帶4個；\n\n【夏之風物師】第八層帶5個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '二筒'== msg or'瓷'== msg or'出千' == msg:
        message = TextMessage(text="青蛙瓷器\n線索：二筒/瓷/出千\n\n【御魂】 第三層帶1個;\n\n【青燈百物語】 第五層帶2個;\n\n【山兔大暴走】 第一到九層各帶1個，第十層帶2個;\n\n【河畔童謠】 第九層帶3個;\n\n【雨女的等候】 第十層帶5個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '小妖精'== msg or'手鼓'== msg or'可愛' == msg:
        message = TextMessage(text="蝴蝶精\n線索：手鼓/小妖精/可愛\n\n【妖刀之秘籍】第二層帶3個;\n\n【荒川之怒】四到六層各帶3個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '湯碗'== msg or'琴'== msg or'牙牙' == msg or '孟婆' == msg:
        message = TextMessage(text="孟婆\n線索：湯碗/琴/牙\n\n【第二十三章】 三個孟婆各帶1個;\n\n【御魂】 第五層帶2個，第六層帶1個;\n\n【河畔童謠】 第五層帶1個;\n\n【安夢奇緣】 第四層2隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '柴犬'== msg or'守護'== msg or'屋'== msg or'雀' == msg:
        message = TextMessage(text="犬神\n線索：劍/柴犬/雀/屋/守護\n\n【御魂】第四層帶1只;\n\n【第十章】第二個覺帶1個，第二個傀儡師帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '尾巴'== msg or'扇子'== msg or'貝殼' == msg or'椒圖' == msg:
        message = TextMessage(text="椒圖\n線索：尾巴/扇子/貝殼\n\n【第二十五章】 第一、二個兵俑各帶1個；\n\n【御魂】 第三、八、九、十層各帶1個；\n\n【叢原火】 貪、嗔、癡各帶1個；\n\n【海怪的溫柔】 第二層帶1個；\n\n【山兔大暴走】 第三層、第六層各帶1個；\n\n【暴風之巔】 第四、五層各帶1個；\n\n【雪之回憶】 第五層帶1個；\n\n【征服世界】 第五層帶1個；\n\n【妖氣封印】 帶3個，但幾乎沒有人開妖氣車，要等很久；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '冥界'== msg or'雲'== msg or'鬼面' == msg:
        message = TextMessage(text="閻魔\n線索：雲/鬼面/冥界\n\n【第二十八章】 閰魔帶1個;\n\n【御魂】 第六層帶1個；\n\n【碎片，發現鬼王】閻魔帶3個；\n\n【夏之風物詩】第六層帶1個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '獻祭' == msg:
        message = TextMessage(text="童男\n線索：翅膀/羽衣/獻祭\n\n【河畔童謠】第一層帶3個;\n\n【第十二章】 兩個童男各帶1個;\n\n【青燈百物語】第三層帶3個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '稻草人'== msg or'咒錐' == msg:
        message = TextMessage(text="丑時之女\n線索：稻草人/咒錐\n\n【第二十一章】 第一個食髮鬼帶3個，後面兩個食髮鬼各帶2個;\n\n【河畔童謠】 第四層帶2個；")
        line_bot_api.reply_message(event.reply_token, message)
    elif '白'== msg or'奪命'== msg or'面具' == msg:
        message = TextMessage(text="鬼使白\n線索：冥界/白/奪命\n\n【暴風之巔】 第六層帶2個;\n\n【第二十四章】 三個青姬各帶1個，BOSS帶1個;\n\n【安夢奇緣】 第三層2隻;\n\n【第二十八章】 面靈氣（覺醒後）帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '紅鬼'== msg or'拍屁股' == msg:
        message = TextMessage(text="天邪鬼赤\n線索：紅鬼/拍屁股\n\n【第十四章】三個帚神各帶3個，BOSS食夢貘帶3個;\n\n【夏之風物詩】第二層帶3個;\n\n【意志的覺醒】第三層帶3個，第六層帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '雨'== msg or'淚珠'== msg or'傘' == msg:
        message = TextMessage(text="雨女\n線索：淚珠/雨/傘\n\n【妖刀之秘籍】 第三層帶3個;\n\n【紅葉的羈絆】 第六層帶2個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '血'== msg or'蝙蝠' == msg:
        message = TextMessage(text="吸血姬\n線索：血/蝙蝠\n\n【第二十四章】 兩個吸血姬各帶1個;\n\n【御魂】 第二層帶1個；\n\n【雨女的等候】 第十層帶5個；\n\n【暴風之巔】 第十層帶5個；\n\n【傘劍的守護】 第十層帶2個；\n\n【雪之回憶】 第六層帶2隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '棺材'== msg or'蠟燭' == msg:
        message = TextMessage(text="跳跳哥哥\n線索：蠟燭/棺材\n\n【第二十四章】 兩個絡新婦各帶3個;\n\n【御魂】 第五層帶1個;\n\n【青燈百物語】 第六層帶3個;\n\n【妖氣封印】 跳跳哥哥帶3個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '跳跳犬'== msg:
        message = TextMessage(text="跳跳犬\n【道成夙怨】 第一層帶13個\n\n【第二十八章】 跳跳妹妹帶3個;\n\n【第七章】 前兩個提燈小僧各帶3個，第三個提燈小僧帶1個，最後一個河童帶2個;\n\n【第一章】(困難) 天邪鬼綠1 數量2個\n\n【海怪的溫柔-第二層】數量3個\n\n【青燈百物語-第一層】數量3個\n\n【鮮血之月-第五層】數量3個\n\n【雪之回憶-第一層】數量3個")
        line_bot_api.reply_message(event.reply_token, message)
    elif '水泡'== msg or'鯉魚精' == msg or '水池'== msg:
        message = TextMessage(text="鯉魚精\n線索：水池/尾巴\n\n【第二十七章】 兩個河童帶各3個 鯉魚精帶1個;\n\n【第七章】 第一個鯉魚精帶3個，第二個鯉魚精帶1個，第一個河童帶1個，最右邊的提燈小僧帶2個;\n\n【青燈百物語】 第六層帶2個;\n\n【海怪的溫柔】 第四層4隻;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '怨恨' == msg or '骷髏' == msg or '骨女'== msg:
        message = TextMessage(text="骨女\n線索：骷髏/怨恨/劍\n\n【雨女的等候】 第四層帶4個;\n\n【妖氣封印】 骨女帶3個;\n\n【御魂】 第六層帶2個;\n\n【第二十三章】 兩個骨女各帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '白' == msg or '鬼使白'== msg:
        message = TextMessage(text="鬼使白\n線索：冥界/白/奪命\n\n【暴風之巔】 第六層帶2個;\n\n【第二十四章】 三個青姬各帶1個，BOSS帶1個;\n\n【安夢奇緣】 第三層2隻;\n\n【第二十八章】 面靈氣（覺醒後）帶1個;")
        line_bot_api.reply_message(event.reply_token, message)
    elif '蠱' == msg or '蟲子' == msg or '迷魂' == msg or '巫蠱師' == msg  :
        message = TextSendMessage(text="巫蠱師\n線索：蠱/迷魂\n\n【夏之風物詩】 第三層帶3個;\n\n【御魂】 第六層帶1個;")
        line_bot_api.reply_message(event.reply_token, message)        

#=====神秘懸賞資料=====        

    else:
        message = TextSendMessage(text="")
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):

    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'\U0001F91A{name}\n\n歡迎加入邪教團賴群！\n請先 `去記事本留ID` 喔！（搜尋「對照」就好）\n\n注意事項-\n1. 寮內不準開車，但可以在邊緣試探(記得收回）\n2. `週寮任要60` ，不達標的就送你機票出去環遊平安京^^\n3. 每3萬寮勳發10禮包\n4. `多解寮30` ，鼓勵每日完成不強迫:D（只要肯喊一定有人陪你解）\n\n活動時間-\n1. 黑蛋宴會：周三周日晚上10點\n2. 首領退治：周六晚上10點\n3. 麒麟：周一到周四晚上7:30不限傷，結束後可能會開逢魔車（看心情：D）')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
