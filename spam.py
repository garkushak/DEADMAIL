import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init

init()
print(Fore.RED)
print("-[                    ]- 0% ")
time.sleep(1)
print("-[=====               ]- 25%")
time.sleep(1)
print("-[==========          ]- 50%")
time.sleep(1)
print("-[===============     ]- 75%")
time.sleep(3)
print("-[====================]- 100%")
time.sleep(1)
print(Fore.RED)
print("--|| Установка Завершена ||--")
print("Нажмите  ENTER для продолжения .....")
input()
os.system("clear")
os.system("CLS")

print("████████████████████████████████")
print("██████████▀▀▀▀▀▀▀▀▀▀▀███████████")
print("██████▀▀▀░░░░░░░░░░░░░▀▀████████")
print("███▀░░░░░░░▄▄▄░░░▄▄▄░░░░░░░▀████")
print("███░░░░░▄▄███████████▄▄▄░░░░░███")
print("███░░░░████▀▀▀▀▀▀▀▀▀█████▄░░░███")
print("████▄▄░█▀▀░░▄▄░░▄▄░░░░░██▀░░▄███")
print("████████░░▄▄█████████░░█████████")
print("████████▄▄██▀░░░░░▀█████████████")
print("█████████████▄░░░▄██████████████")
print("██████████████░░░███████████████")
print("██████████████░░░███████████████")
print("█████████████▀░░░▀██████████████")
print("███████▄▄████░░░░░████▄▄████████")
print("█████░▄▄░███░░░░░░░███░▄▄░██████")
print("█████░▀██▀▀░░░░░░░░░▀▀██▀░██████")
print("██████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄███████")
print("████████████████████████████████ ")


print("░▐█▀█▄░▐█▀▀░░▄█▀▄─░▐█▀█▄▒▐██▄▒▄██▌░░▄█▀▄─▐██▒██░░░")
print("░▐█▌▐█░▐█▀▀░▐█▄▄▐█░▐█▌▐█░▒█░▒█░▒█░░▐█▄▄▐█░█▌▒██░░░")
print("░▐█▄█▀░▐█▄▄░▐█─░▐█░▐█▄█▀▒▐█░░░░▒█▌░▐█─░▐█▐██▒██▄▄█")
print("                            РАЗРАБ:МАКАР ГАРЬКУША")
print("                                           ВЕРСИЯ 1.0")
def send_mail():
    login = input( 'Почта: ' )
    password = input( 'Пароль: ' )
    url = input( 'URL(здесь прописываем smtp.ваш сервис почты, к примеру smtp.mail.ru,smtp.yandex.ru,smtp.gmail.ru): ' )
    number = int( input( 'Кол-во сообщений: ' ) )
    toaddr = input( 'Кому: ' )
    topic = input( 'Тема: ' )
    message = input( 'Текст: ' )

    print("Атака началась! Hа " + toaddr)
    for value in range( number ):
        msg = MIMEMultipart()
 
        msg[ 'Subject' ] = topic
        msg[ 'From' ] = login
        body = message
 
        msg.attach( MIMEText( body, 'plain' ) )
 
        server = root.SMTP_SSL( url, 465 )
        server.login( login, password )
        server.sendmail( login, toaddr, msg.as_string() )
 
def main():
    send_mail()
 

if __name__ == '__main__':
    main()
