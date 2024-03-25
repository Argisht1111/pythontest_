# import tkinter
#
# root = tkinter.Tk()
# root.geometry('500x200')
# root.resizable(False, False)
#
# test = tkinter.Label(root, text='GTA V')
# test.pack()
# test1 = tkinter.Button(root, width=40,height=5, text='GOOGLE')
# test1.pack()
#
# tkinter.mainloop()

import telebot
from telebot import types

bot = telebot.TeleBot('7007592847:AAGEFkjxNB14OJHlnAuIhT-xlxj3dxrg-8U')


@bot.message_handler(content_types=['photo'])
def test(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти ', url='https://www.youtube.com/'))
    bot.reply_to(message, 'зачем ты мне отправляешь фото',reply_markup = markup)


@bot.message_handler(commands=['site'])
def test(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти ', url='https://www.youtube.com/'))
    bot.reply_to(message, 'Ютуб',reply_markup = markup)



@bot.message_handler(commands=['start',])
def test(message):
    bot.send_message(message.chat.id,'<em>ВАЗ2107</em>', parse_mode='html')
@bot.message_handler(commands=['hello'])


def test(message):
    bot.send_message(message.chat.id,f'привет {message.from_user.first_name} {message.from_user.last_name}')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'как дела':
        bot.reply_to(message, f'нормально уцы у тебя как')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет  {message.from_user.first_name}')



bot.polling(none_stop=True)