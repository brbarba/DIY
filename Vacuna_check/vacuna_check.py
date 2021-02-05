import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'mivacuna.salud.gob.mx SITE IS DOWN!'
        body = 'El site de Registro de vacunacion NO esta Jalando'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, 'brbarba@outlook.com', msg)

try:
    r = requests.get('https://mivacuna.salud.gob.mx/', timeout=5)

    if r.status_code != 200:
        notify_user()
        print("el sitio no jala")

except Exception as e:

    notify_user()
    print("algo no jalo bien")
