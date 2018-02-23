import telebot
from telebot import types

TOKEN = '543576604:AAH0GQH3N1AD_AFUT8bBF-etVc9Lff9QUa8'

bot = telebot.TeleBot(TOKEN)


description = 'This is description'

@bot.message_handler(commands=['start', 'help'])
def enter_point(message):
    bot.send_message(message.chat.id, description)
    keyboard = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Boost your channel')
    bot.send_message(message.chat.id, "Lets do this", reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = message.text
    if answer == 'Boost your channel':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Back')
        msg = bot.send_message(message.chat.id, "Enter your telegram channel", reply_markup=markup)
        bot.register_next_step_handler(msg, send_ch)

def send_ch(message):
    answer=message.text
    print(message.text)
    bot.send_message(chat_id='511164919', text=answer)
    keyboard = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Boost your channel')
    bot.send_message(message.chat.id, "Lets do this", reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)