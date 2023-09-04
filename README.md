# Telegram bot to recognize images
Telegram token contained in files is used for demonstration purposes. It does not work.
## 0. Getting a telegram bot token
## 1. Data collecting. 
You can collect your training data by downloading sticker packs using the datadownloader.py file. 
- Start datadownloader.py file
- Send /start command to your bot
- Send /yes to download positive examples of stickers
- Send /no to download negative examples of stickers
- **Warning! Bot will download the whole sticker pack once you send it one sticker**

## 2. Data multiplication/conversion
If you downloaded animated stickers and your /yes(or no)/animated folder is not empty, run filesconverter.py file. It will divide animated .tgs stickers into .png frames. 
If you are worried that your dataset is too small, move it to the toprocess folder. Then run rotateandbackgroud.ipynb file. It will add rotations and non-transparent backgrounds so you will have multiple training examples from one sticker.

## 3. Model training
Go to model.ipynb file and follow instructions
