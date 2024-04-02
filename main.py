
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

TOKEN = '6589049081:AAGDsG2gS7hrbB2N21oQILXOtOunxvXmI5U'

def start(update,context):

    buttons =[
        [KeyboardButton(text='python')],
        [KeyboardButton(text='javaSkript')],
        [KeyboardButton(text='C')],
        [KeyboardButton(text='C_sharp')],
        [KeyboardButton(text='Paskal')]
    ]
    update.message.reply_text(text='Dasturlash tilini tanlang:',reply_markup = ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
    )

def start(update,context):
    update.message.reply_text('Assalomu alaykum , \nDasturlash tilini tanlang!!!')

def python(update,context):
    update.message.reply_text(text='Siz Python dasturchisisiz')

def javaSkript(update,context):
    update.message.reply_text('Siz JavaScript developersiz')

def C (update,context):
    update.message.reply_text('Siz C programmersiz')

def sharp_c(update,context):
    update.message.reply_text('Siz C# programmersiz')

def paskal(update,context):
    update.message.reply_text('Siz Pascal programmersiz')
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',start))

dispatcher.add_handler(MessageHandler(Filters.text('/start'),start))
dispatcher.add_handler(MessageHandler(Filters.text('python'),python))
dispatcher.add_handler(MessageHandler(Filters.text('javaSkript'),javaSkript))
dispatcher.add_handler(MessageHandler(Filters.text('C_sharp'),sharp_c))
dispatcher.add_handler(MessageHandler(Filters.text('C'),C))
dispatcher.add_handler(MessageHandler(Filters.text('Paskal'),paskal))


updater.start_polling()
updater.idle()

