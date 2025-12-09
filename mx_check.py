import dns.resolver

# ПОЛНЫЙ путь к файлу emails.txt на твоем рабочем столе:
EMAILS_FILE = r"C:\Users\win11pro\Desktop\emails.txt"

def check_domain(email):
    # Проверяем корректность формата email
    if "@" not in email:
        return "некорректный email"

    local, domain = email.split("@", 1)

    # Проверка существования домена
    try:
        dns.resolver.resolve(domain, "MX")
        return "домен валиден"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except:
        return "MX-записи отсутствуют или некорректны"


def main():
    try:
        with open(EMAILS_FILE, "r", encoding="utf-8") as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Ошибка: файл emails.txt не найден. Проверь путь!")
        return

    print("Проверка email-доменов:\n")

    for email in emails:
        result = check_domain(email)
        print(f"{email} — {result}")


if __name__ == "__main__":
    main()
