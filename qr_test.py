import telepot
import qrcode
from io import BytesIO

bot_token = '6617401844:AAFQgpNaW3DQlilluP2K8POXitk-rfpbZBQ'
bot = telepot.Bot(bot_token)

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    img_io = BytesIO()
    qr_img.save(img_io, format='PNG')
    img_io.seek(0)

    return img_io

def send_qr_code(chat_id, qr_data):
    qr_img = generate_qr_code(qr_data)
    bot.sendPhoto(chat_id, ('qr.png', qr_img), caption=f"QR code for scanning")

if __name__ == "__main__":
    user_chat_id = 'USER_CHAT_ID'  # Replace with the actual user's chat ID
    qr_data = "Hello, QR Code!"
    send_qr_code(user_chat_id, qr_data)