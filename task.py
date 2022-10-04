
# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5507983823:AAFBabQJuVQXys283MD5DyiW11EzPHKl2ZI')
updater = Updater(token='5507983823:AAFBabQJuVQXys283MD5DyiW11EzPHKl2ZI')
dispatcher = updater.dispatcher

A = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\nВведите текст')

    return A


def delete(update, context):
    text = update.message.text
    if 'абв' in text.lower():
        context.bot.send_message(update.effective_chat.id, ' '.join(
            list(filter(lambda x: 'абв' not in x.lower(), text.split()))))
    else:
        context.bot.send_message(
            update.effective_chat.id, 'Слов, содержащих "абв" нет')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пока!')


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [delete_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
