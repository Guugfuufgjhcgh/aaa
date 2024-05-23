import telebot
import requests
import datetime

TOKEN = "6626020995:AAEnvONL4dC_grKk1kcsBJemS6r9UFH4ZFY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = """
اهلا بك في مقبرة GH YT. يرجى كتابة -- قبل أي ايدي وسوف يتم وضعه في المقبرة.
    /start --Player ID
    مثال:
    /start --1234567890
    """
    bot.send_message(message.chat.id, welcome_message)
    
    additional_message = """
    ➪ : @XMODHPG

    𝑨𝑳𝑳 𝑽𝑰𝑺𝑰𝑻𝑺 𝑯𝑨𝑽𝑬 𝑩𝑬𝑬𝑵 
    𝑺𝑬𝑵𝑻𖤐

    𓅓GH YT           ?𖤍 

    ┏━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃💡
    ┣━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃ 👀 
    ┃ 🔴 
    ┃ 🟢 
    ┣━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃ ✨ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙧𝙚𝙨𝙩𝙖𝙧𝙩 𝙜𝙖𝙢𝙚 
    ┃ 𝙖𝙣𝙙 𝙘𝙝𝙚𝙘𝙠 𝙫𝙞𝙨𝙞𝙩𝙨 ✨
    ┗━━━━━━━━━━━━━━━━━━━━━━━━┛

ضع قبل أي ايدي --'
    /start --Player ID
    مثال:
    /start --1234567890

    💻 تطوير: @https://t.me/XMODHPG

    /البوت خاص بي https://t.me/XMODHPG GH YT
    """
    bot.send_message(message.chat.id, additional_message)

@bot.message_handler(func=lambda message: True)
def get_player_info(message):
    if '--' in message.text:
        player_id = message.text.split('--')[1].strip()  # إزالة الفراغات الزائدة
        region = "me"

        url = f'https://freefireapi.com.br/api/search_id?id={player_id}&region={region}'
        response = requests.get(url)
        
        if response.status_code == 200:
            player_data = response.json()
            basic_info = player_data.get('basicInfo', {})
            social_info = player_data.get('socialInfo', {})
            clan_basic_info = player_data.get('clanBasicInfo', {})
            captain_basic_info = player_data.get('captainBasicInfo', {})

            name = basic_info.get('nickname', 'Name not found')
            level = basic_info.get('level', 'Level not found')
            player_id = basic_info.get('accountId', 'Player ID not found')
            exp = basic_info.get('exp', 'Experience not found')
            liked = basic_info.get('liked', 'Likes not found')
            last_login = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
            creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))
            rank_token = basic_info.get('rankingPoints', 'Rank token not found')
            rank_number = basic_info.get('rank', 'Rank number not found')
            language = social_info.get('language', 'Language not found')
            bio = social_info.get('signature', 'Bio not found')
            guild_id = clan_basic_info.get('clanId', 'Guild ID not found')
            admin_id = captain_basic_info.get('accountId', 'Admin ID not found')
            admin_name = captain_basic_info.get('nickname', 'Admin name not found')
            clan_level = clan_basic_info.get('clanLevel', 'Clan level not found')
            clan_capacity = clan_basic_info.get('capacity', 'Clan capacity not found')
            clan_max_capacity = clan_basic_info.get('memberNum', 'Clan maximum capacity not found')

            answer_message = (
                f"👑 معلومات اللاعب 👑\n\n"
                f"🔹 الإسم: {name}\n"
                f"🔹 المستوى: {level}\n"
                f"🔹 معرف اللاعب: #{player_id}\n"
                f"🔹 الخبرة: {exp} HP\n"
                f"🔹 الإعجابات: {liked}\n"
                f"🔹 آخر تسجيل دخول: {last_login}\n"
                f"🔹 تاريخ الإنشاء: {creation_date}\n"
                f"🔹 رمز التصنيف: {rank_token}\n"
                f"🔹 رقم التصنيف: {rank_number}\n"
                f"🔹 اللغة: {language}\n"
                f"🔹 السيرة الذاتية: {bio}\n"
                f"🔹 معرّف النقابة: {guild_id}\n"
                f"🔹 معرّف المسؤول: {admin_id}\n"
                f"🔹 اسم المسؤول: {admin_name}\n"
                f"🔹 مستوى العشيرة: {clan_level}\n"
                f"🔹 سعة العشيرة: {clan_capacity}\n"
                f"🔹 السعة القصوى للعشيرة: {clan_max_capacity}\n\n"
                f"بوت GH YT"
            )
            
            bot.reply_to(message, answer_message, parse_mode='HTML')
        else:
            bot.reply_to(message, """
            ████████╗███████╗███╗   ███╗     ██╗    ██╗ ██████╗ ██████╗      ██████╗  █████╗  ██████╗
            ╚══██╔══╝██╔════╝████╗ ████║     ██║    ██║██╔═══██╗██╔══██╗    ██╔═══██╗██╔══██╗██╔════╝
               ██║   █████╗  ██╔████╔██║     ██║ █╗ ██║██║   ██║██████╔╝    ██║   ██║███████║██║     
               ██║   ██╔══╝  ██║╚██╔╝██║     ██║███╗██║██║   ██║██╔═══╝     ██║   ██║██╔══██║██║     
               ██║   ███████╗██║ ╚═╝ ██║     ╚███╔███╔╝╚██████╔╝██║         ╚██████╔╝██║  ██║╚██████╗
               ╚═╝   ╚══════╝╚═╝     ╚═╝      ╚══╝╚══╝  ╚═════╝ ╚═╝          ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
            
            تم وضع هذا اللاعب في المقبرة
            تم وضع هذا اللاعب في المقبرة
            تم وضع هذا اللاعب في المقبرة
 تم وضع هذا العب في المقبرة    
  تم وضع هذا العب في المقبرة
   تم وضع هذا العب في المقبرة
   تم تعذيب العب
 تم تعذيب العب
 تم فشخ العب
 تم فشخ العب بنجاح         
            """)
    else:
        bot.reply_to(message, "تنسيق غير صالح. الرجاء استخدام -- رقم تعريف اللاعب.")

# استبدال محاولة التشغيل المستمرة بتشغيل البوت لمدة 24 ساعة
bot.infinity_polling()
