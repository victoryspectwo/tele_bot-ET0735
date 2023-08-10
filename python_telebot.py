import sys
import time
import telepot
import datetime
import qrcode

drinks = [
    {'Drink': 'Milo', 'price': 1.40},
    {'Drink': 'Ice Lemon Tea', 'price': 1.20},
    {'Drink': 'Nescafe', 'price': 1.60},
    {'Drink': 'Coca-Cola', 'price': 1.40},
    {'Drink': 'Pepsi', 'price': 1.40},
    {'Drink': 'Sprite', 'price': 1.20},
    {'Drink': '100 Plus', 'price': 1.20},
    {'Drink': 'Green Tea', 'price': 1.40},
    {'Drink': 'Milk Tea', 'price': 1.60},

]
payment_options = ['QR', 'RFID']

bot_token = '6617401844:AAFQgpNaW3DQlilluP2K8POXitk-rfpbZBQ'
bot = telepot.Bot(bot_token)

def handle_msg(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/drinks':
        send_drinks_list(chat_id)
    elif command.startswith('/select'):
        drink_index = int(command.split()[-1])
        send_payment_options(chat_id, drink_index)
    elif command.startswith('/payment'):
        payment_type = command.split()[-1]
        process_order(chat_id, int(command.split()[1]), payment_type)

def send_drinks_list(chat_id):
    drinks_list = "\n".join([f"{index}. {drink['Drink']} (${drink['price']:.2f})" for index, drink in enumerate(drinks)])
    bot.sendMessage(chat_id, f"Please select a drink:\n{drinks_list}")

def send_payment_options(chat_id, drink_index):
    options = "\n".join([f"{index}. {option}" for index, option in enumerate(payment_options)])
    bot.sendMessage(chat_id, f"Please select a payment method for {drinks[drink_index]['Drink']}:\n{options}")

def process_order(chat_id, drink_index, payment_type):
    selected_drink = drinks[drink_index]['Drink']
    if payment_type == 'QR':
        generate_qr_and_send(chat_id, selected_drink)
    elif payment_type == 'RFID':
        bot.sendMessage(chat_id, f"You selected {payment_type} payment for {selected_drink}. (Not implemented)")
    else:
        bot.sendMessage(chat_id, "Invalid payment option.")

def generate_qr_and_send(chat_id, drink_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Drink: {drink_name}")
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Send the QR code image to the user
    bot.sendPhoto(chat_id, qr_img)

bot_token = '6617401844:AAFQgpNaW3DQlilluP2K8POXitk-rfpbZBQ'
bot.message_loop(handle_msg)

print("I am listening...")

while True:
    pass
