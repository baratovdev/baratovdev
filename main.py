from translate import translate
import telebot

TOKEN = "6879571415:AAEy77TiwbjHuwCAxV8y9LjHUclXQWFJ5OE"
tarjimonbot = telebot.TeleBot(token=TOKEN)

@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu aleykum, tarjimon botiga xush kelibsiz!"
    xabar += '\nMatningizni yuboring.'
    tarjimonbot.reply_to(message, xabar)

@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))

tarjimonbot.polling()