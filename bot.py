import telebot
bot = telebot.TeleBot('5693155563:AAEQFeJzyuocsQqrj1EL19eenGoYccV2_co')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('🟢 команда "за"', '🔴 команда "против"')
red = []
green = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Здравствуйте!\nДля перехода к голосованию нажмите соответствующую кнопку',reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def messages(message):
    text = message.text
    if text == '🟢 команда "за"':
        if green.count(message.chat.id)==0 and red.count(message.chat.id)==0:
            green.append(message.chat.id)
            bot.send_message(message.chat.id, 'Спасибо, ваш голос учтен')
        elif green.count(message.chat.id)!=0:
            bot.send_message(message.chat.id,'Ваш голос уже учтен')
        elif red.count(message.chat.id)!=0:
            bot.send_message(message.chat.id, 'Вы уже отдали голос другой команде')
        print('green: ',green)
    elif text == '🔴 команда "против"':
        if red.count(message.chat.id)==0 and green.count(message.chat.id)==0 :
            red.append(message.chat.id)
            bot.send_message(message.chat.id, 'Спасибо, ваш голос учтен')
        elif red.count(message.chat.id) != 0:
            bot.send_message(message.chat.id, 'Ваш голос уже учтен')
        elif green.count(message.chat.id) != 0:
            bot.send_message(message.chat.id, 'Вы уже отдали голос другой команде')
        print('red: ',red)
    percred = (len(red)/(len(red)+len(green)))*100
    percgreen = (len(green)/(len(red)+len(green)))*100
    bot.send_message('401213379','команда "за" ' + str(percgreen) + '% ' +'('+str(len(green))+')' + '\n' + 'команда "против" ' + str(percred) + '% ' +'('+ str(len(red))+')')
    # bot.send_message('579372261','команда "за" ' + str(percgreen) + '% ' +'('+str(len(green))+')' + '\n' + 'команда "против" ' + str(percred) + '% ' +'('+ str(len(red))+')')
bot.polling()