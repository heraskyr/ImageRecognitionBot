import os
import cv2
import telegram.ext
from PIL import Image

import telegram
from datetime import datetime

token = "6155680270:AAF5FPto8PY-7YdJM4doKINwZszSDUp9XKo"
root = "./../files/train/"
yes_no_path = ""
animated = "animated/"


async def start(update, context):
    await update.message.reply_text(
        "Hello. Send me command /yes or /no to download stickers thas contain banana or not.")


async def download_sticker_image(update, context):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    name = update.effective_user.first_name
    print("I caught sticker.\nDownloading the whole stickerpack")
    sticker_set = await app.bot.get_sticker_set(update.message.sticker.set_name)
    for stick in sticker_set.stickers:
        time_str = root + yes_no_path + str(datetime.now()).replace(" ", "").replace(":", "").replace(".", "") + '.webp'                                                                            ''
        file = await stick.get_file()
        await file.download_to_drive(time_str)
        im = Image.open(time_str).convert('RGB')
        im.save(time_str.replace('webp', 'png'), 'png')
    await update.effective_chat.send_message(f'Downloaded all your files to {yes_no_path}')


async def download_sticker_animated(update, context):
    userid = update.effective_user.id
    chatid = update.effective_chat.id
    name = update.effective_user.first_name
    print("I caught animated sticker.\nDownloading the whole stickerpack")
    sticker_set = await app.bot.get_sticker_set(update.message.sticker.set_name)
    for stick in sticker_set.stickers:
        file = await stick.get_file()
        time_str = root + yes_no_path + animated + str(datetime.now()).replace(" ", "").replace(":", "").replace(".",
                                                                                                                 "") + '.tgs'
        await file.download_to_drive(time_str)
        print(time_str)

    await update.effective_chat.send_message(f'Downloaded all your files to {yes_no_path}')


async def set_no_folder(update, context):
    global yes_no_path
    yes_no_path = "no/"
    if not os.path.exists(root+yes_no_path):
        if not os.path.exists(root):
            os.mkdir(root)
        os.mkdir(root+yes_no_path)
    await update.effective_chat.send_message("Ok! Send stickers that do not contain banana")


async def set_yes_folder(update, context):
    global yes_no_path
    yes_no_path = "yes/"
    if not os.path.exists(root+yes_no_path):
        if not os.path.exists(root):
            os.mkdir(root)
        os.mkdir(root+yes_no_path)
    await update.effective_chat.send_message("Ok! Send stickers that do contain banana")


app = telegram.ext.Application.builder().token(token).build()

app.add_handler(telegram.ext.CommandHandler('start', start))
app.add_handler(telegram.ext.CommandHandler('start', start))
app.add_handler(telegram.ext.CommandHandler('yes', set_yes_folder))
app.add_handler(telegram.ext.CommandHandler('no', set_no_folder))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Sticker.STATIC, download_sticker_image))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Sticker.ANIMATED, download_sticker_animated))


app.run_polling()
