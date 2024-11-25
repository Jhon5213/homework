def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('massage','vasyok1337@gmail.com')
send_email('massage', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('massage', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('massage', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
