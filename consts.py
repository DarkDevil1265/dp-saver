from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
    welcome_msg = '''Hello π
I am a DP saver bot
Send me anyones instagram username or profile url to get their DP
 '''

    return welcome_msg


def acc_type(val):
    if(val):
        return "πPrivateπ"
    else:
        return "πPublicπ"


def create_caption(user):
    caption_msg = f'''π*Name*π: {es(user.full_name,version=2)} \nπ€©*Followers*π€©: {es(str(user.followers),version=2)} \nπ*Following*π: {es(str(user.followees),version=2)}\
        \nπ§*Account Type*π§: {acc_type(user.is_private)} \n\nThank You For Using The bot ππ'''

    return caption_msg


def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            try:
                data = data.split("?")
                return data[0]
            except Exception:
                return "incorrect format"
        return data
    except Exception:
        return "incorrect format"


ratingkey = [[InlineKeyboardButton(
    "Support me by rating π", url="https://t.me/Dpinstallbot/15")]]
