import requests

# TOKEN Telegram-бота
BOT_TOKEN = "8449211858:AAGR5aKaGPFb2gtRCgXtjD4PRDtjtbwARZU"

# ID чата (обычно это твой user_id)
CHAT_ID = "6222262889"

#  ПОЛНЫЙ путь к текстовому файлу:
TEXT_FILE = r"C:\Users\win11pro\Desktop\message.txt"


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Сообщение отправлено успешно!")
    else:
        print("Ошибка отправки:", response.text)


def main():
    try:
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except FileNotFoundError:
        print("Ошибка: файл с текстом не найден.")
        return

    if not text:
        print("Файл пустой.")
        return

    print("Отправляю сообщение в Telegram...")
    send_message(text)


if __name__ == "__main__":
    main()
