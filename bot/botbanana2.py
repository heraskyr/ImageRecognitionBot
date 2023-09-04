import os
import cv2
import telegram.ext

import telegram
from datetime import datetime
from filesconverter import getSingleFrame
import tensorflow as tf
from tensorflow import keras
import numpy as np

names = ['not banana', 'banana']
model = keras.models.load_model('./../newmodel.keras')
token = ""



def classify(path):
    image = tf.keras.utils.load_img(
        path, target_size=(256, 256)
    )
    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(score)
    return f"This is {names[np.argmax(score)]} with {round(100 * np.max(score), 2)} per cent probability."

async def start(update, context):
    await update.message.reply_text("Started")

async def react_to_sticker_animated(update, context):
    userid = update.effective_user.id
    chatid = update.effective_chat.id
    name = update.effective_user.first_name
    file = await update.message.sticker.get_file()
    timestr = "./files/temp/" + str(datetime.now()).replace(" ", "").replace(":", "").replace(".", "") + '.tgs'
    await file.download_to_drive(timestr)
    image = await getSingleFrame(timestr)
    await update.effective_chat.send_message(classify(image))
    os.remove(timestr)
    os.remove(timestr.replace('tgs', 'gif'))
    os.remove(timestr.replace('tgs', 'png'))


async def react_to_sticker_image(update, context):
    userid = update.effective_user.id
    chatid = update.effective_chat.id
    name = update.effective_user.first_name
    file = await update.message.sticker.get_file()
    timestr = "./../files/temp/" + str(datetime.now()).replace(" ", "").replace(":", "").replace(".", "") + '.webp'
    await file.download_to_drive(timestr)

    await update.effective_chat.send_message(classify(timestr))
    os.remove(timestr)


async def image_handler(update, context):
    print("caught image or photo")
    file = await update.message.document.get_file()
    timestr = "./../files/temp/" + str(datetime.now()).replace(" ", "").replace(":", "").replace(".", "") + '.png'
    await file.download_to_drive(timestr)
    await update.effective_chat.send_message(classify(timestr))
    os.remove(timestr)


async def photo_handler(update, context):
    photos = update.message.photo
    file= await photos[0].get_file()
    timestr = "files/temp/" + str(datetime.now()).replace(" ", "").replace(":", "").replace(".", "") + '.png'
    await file.download_to_drive(timestr)
    await update.effective_chat.send_message(classify(timestr))
    os.remove(timestr)


app = telegram.ext.Application.builder().token(token).build()
app.add_handler(telegram.ext.CommandHandler('start', start))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Sticker.STATIC, react_to_sticker_image))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Sticker.ANIMATED, react_to_sticker_animated))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.PHOTO, photo_handler))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Document.IMAGE, image_handler))


print("started")
app.run_polling()
