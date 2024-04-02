

from telegram import KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import (Updater,CommandHandler,MessageHandler,Filters,ConversationHandler)

TOKEN = '6589049081:AAGDsG2gS7hrbB2N21oQILXOtOunxvXmI5U'


FULLNAME,CONTACT,COURSES = range(3)

def start(update,context):
    update.message.reply_text('Salom!')
    update.message.reply_text('Ismingizni kiriting:')
    return FULLNAME
def full_name(update,context):
    name = update.message.text
    context.user_data['full_name'] = name
    keyboard = [
        [KeyboardButton(text="Backend"),KeyboardButton(text='Fullstack'),
         KeyboardButton(text='Frontend'),KeyboardButton(text='Mobile')],
    ]
    update.message.reply_text(
        text="Kurs turini tanlang!",
        reply_markup=ReplyKeyboardMarkup(keyboard)
    )
    return COURSES
def courses(update,context):

    context.user_data['courses'] = update.message.text
    update.message.reply_text(text=f"""
    FISH: {context.user_data['full_name']},
    KURS:{context.user_data['courses']}
    Tel:{context.user_data['sizning kontaktingiz']}

""")
#     update.message.text

    button = [[KeyboardButton(text='Share contact',request_contact=True)]]

    update.message.reply_text(text='kontakt share',
                              reply_markup=ReplyKeyboardMarkup(button,resize_keyboard=True,one_time_keyboard=True))


    return CONTACT


def contact(update,context):
    update.message.reply_text(text =f'sizning kontaktingiz{update.message.contact.phone_number}')


updeter = Updater(token=TOKEN)
dp = updeter.dispatcher

dp.add_handler(ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states = {
        FULLNAME:[MessageHandler(Filters.text,full_name)],
        COURSES:[MessageHandler(Filters.text,courses)],
        CONTACT:[MessageHandler(Filters.text,contact)]
    },
    fallbacks=[],
))

updeter.start_polling()