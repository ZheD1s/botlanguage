import telebot
from telebot import types

bot = telebot.TeleBot('5592905135:AAF69v2M8QRCMH7ddbwxbTE9ahDBIfwNxK8')

name = ''
age = 0
language = ''

@bot.message_handler(content_types=['text'])
def getTextMessage(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'Hello, what`s your name?')
        bot.register_next_step_handler(message, getName)

def getName(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Your name is ' + name)
    bot.send_message(message.chat.id, 'How old are you?')
    bot.register_next_step_handler(message, getAge)

def getAge(message):
    global age
    try:
        age = int(message.text)
        bot.send_message(message.chat.id, 'Your age is ' + str(age))
        # keyboard = types.InlineKeyboardMarkup()
        # keyYes = types.InlineKeyboardButton('Yes', callback_data='yes')
        # keyNo = types.InlineKeyboardButton('No', callback_data='no')
        # keyboard.add(keyYes, keyNo)
        bot.send_message(message.chat.id, 'Do you love programming?')
        bot.register_next_step_handler(message, getFavouriteLanguage)

    except ValueError:
        bot.send_message(message.chat.id, 'Input only int numbers!')
        bot.register_next_step_handler(message, getAge)

def getFavouriteLanguage(message):
    keyboard = types.InlineKeyboardMarkup()
    keyPython = types.InlineKeyboardButton('Python', callback_data='python')
    keyCpp = types.InlineKeyboardButton('C++', callback_data='c++')
    keyJava = types.InlineKeyboardButton('Java', callback_data='java')
    keyRuby = types.InlineKeyboardButton('Ruby', callback_data='ruby')
    keyCsh = types.InlineKeyboardButton('C#', callback_data='c#')
    keyC = types.InlineKeyboardButton('C', callback_data='c')
    keyGo = types.InlineKeyboardButton('Go', callback_data='go')
    keyboard.add(keyPython, keyCpp, keyJava, keyRuby, keyCsh, keyC, keyGo)
    bot.send_message(message.chat.id, 'What`s your favourite language?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callbackHandler(call):
    global language
    if call.data == 'python':
        language = 'python'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'c++':
        language = 'c++'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'java':
        language = 'java'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'ruby':
        language = 'ruby'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'c#':
        language = 'c#'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'c':
        language = 'c'
        bot.send_message(call.message.chat.id, 'Your data is saved')
    elif call.data == 'go':
        language = 'go'
        bot.send_message(call.message.chat.id, 'Your data is saved')

bot.polling(non_stop=True, interval=0)