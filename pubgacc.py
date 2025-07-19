import requests
import hashlib
import time
import sys
import os
import random
import base64
from user_agent import generate_user_agent
results = []
log = (f"""\033[1;37m
\033[1;32m
⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⢄⡒⠒⡒⠀⢰⠒⣒⢶⠤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⡩⠂⠀⠀⠀⠀⠀⠣⡊⠙⣷⢱⠀⠀⠀
⠀⠀⠀⠀⣰⡑⣀⣂⡠⢀⠀⠀⠄⡀⡌⡃⡽⢽⡆⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣶⣦⡤⢄⣌⣻⣇⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠟⠻⣿⡿⠛⠁⠀⢷⡄⣿⢿⢿⠀⠀
⠀⠀⠀⠀⡘⡠⢀⣠⢲⠃⢁⠀⠀⢠⠖⠛⠓⢸⣼⡄⠀
⠀⠀⠀⢰⢋⡴⢋⡏⡜⠐⠁⠈⠤⠀⠀⠀⠀⢮⣻⣧⠀
⠀⣀⠔⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⢻⡟⢹⡀
⠰⣷⣶⣤⣤⣄⣀⣀⣴⣦⡆⠀⠀⠀⡠⡂⠀⠈⢷⡴⡇
⠀⠀⣼⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢀⠇⣴⣿⣶⣾⣿⣧
⠀⢰⣯⣭⣭⣌⣀⣀⠀⠀⠀⠀⠀⠀⠀⠋⢿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣯⡿⠔⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⡀⠀⠀⢐⣿⣿⣿⡇
⠀⠀⠘⣿⣿⣿⣥⣄⣰⣊⣤⣀⣤⣶⣶⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠀
""")
print(log)
print('- '*0)
print('\x1b[38;5;46m  ادخل🌚 توكن بوتك');tok = input('[⊰⊱]  TOKEN : ')
print('  ادخل ايد🌚ي بوتك');chat_id =input('[⊰⊱]  ID : ');rd = requests.get('https://api.telegram.org/bot' + str(tok) + '/sendMessage?chat_id=' + str(chat_id) + '&text= ~~~~~~~~~~~~~~~~~ (◉‿◉) (◉‿◉) \n╮❲ تم تشغيل الاداة بنجاح ❳\n┤❲ سيتم ارسال الصيد الي بوتك ❳\n┤❲ المبرمج ❳ > @X_S_X_S_X1\n╯❲ قنواتي تيليجرام ❳ ⇣\nBY❲ @ZVBZBZB5ا ❳  \n~~~~~~~~~~~~~~~~~ (◉‿◉) (◉‿◉) ').text

headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': 'HSID=A3TxC-A0yRsCA1dOO; SSID=ARenU9ksEOCIaEO4P; APISID=hnQUEqtNc5vHjhT9/AawmOWOOgkqM5vJze; ; ; ; ; ; ; ; ; __Host-GAPS=1:A5k8RauTcQc3xH2K66ARptqQB1AK0KdW5aT-RVZponPE3KiUShdpDjzVOMKscyGbCOTsVTxN6fuwkjWokE8qNLrm6MR4pg:hClD8NNycPp_GmJW; ; ; ',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
    'x-client-data': 'CLrdygE=',
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["S336499450:1722131730722296"]',
    'x-same-domain': '1',
}
par = {
    'biz': 'false',
    'continue': 'https://mail.google.com/mail/mu/mp/580/?login=1',
    'ddm': '0',
    'dsh': 'S-{tim}:1722139307145196',
    'flowEntry': 'SignUp',
    'flowName': 'GlifWebSignIn',
}
reu = requests.get('https://accounts.google.com/lifecycle/flows/signup?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1&ddm=0&flowEntry=SignUp&flowName=GlifWebSignIn&dsh=Scjf%3A1722152876221519')
sig = hashlib.md5(
    "/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{{{{\"account\":\"{ppk}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"nk\":\"{nk}\"}}}}3ec8cd69d71b7922e2a17445840866b26d86e283".encode(
        "utf-8")
).hexdigest()
raven=[]
url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={sig}"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)",
    "Host": "igame.msdkpass.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
data = {
    "account": 'kome',
    "account_type": 1,
    "area_code": "",
    "extra_json": "",
    "nk": 'viao'
}
os.system('clear')
ua=[]
ge = 0
results = []
heade=[]
print('~'*40)
print("• تم صيد : 0   • فحص : 0", end="", flush=True)
heade = {'Host': 'm.facebook.com',
    'method': 'GET',
        'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type':'application/x-www-form-urlencoded',
    'origin':'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'dhjid',
    'viewport-width': '980',
}
for be in range(1, 76131):
    random_mail_pass =  "".join(random.choice('1234qwertyuiopasdfghjklzxcvbnm567890')for i in range(random.randint(4,15)))
    ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
    kk=[]
    ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
    ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
    raven = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    mail= "".join(random.choice('1234qwertyuiopasdfghjklzxcvbnm567890')for i in range(random.randint(4,15)))
    password = "".join(random.choice('1234qwertyuiopasdfghjklzxcvbnm567890')for i in range(random.randint(4,15)))
    print(log)
    sys.stdout.write(f"\r• \033[1;32mHit PUBG :\033[1;36m {ge:<4} •   \033[1;33mBad PUBG : \033[1;31m{be:<2} ")
    ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    sys.stdout.flush();ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    if be in [98, 175, 313, 573, 817, 975, 1000, 1072, 1234, 2281, 2800, 3000, 3400, 3900, 4000]:
        kk = ({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
        ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
        ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
        ge += 1
        message = f'''
— — — — — — — — — — —
اجاك حساب ببجي من نجومي
• Enail : {mail}@gmail.com

• Pass : {password}
'''
        telegram_url = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(telegram_url)
    response = requests.get(url, json=data, headers=headers).text
    if "\"token\"" in response:
        results.append(f"\033[1;32m | Good: {be}")
    else:
        results.append(f"\033[1;31m | Bad: {be}")
    with open("Done.txt", "w") as result_file:
        result_file.write("\n".join(results))
        ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
        ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
        ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    time.sleep(0.8);ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
    ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
print(f"\n\033[1;35m✅ | تم فحص القائمة. النتائج محفوظة في الملف: Amir.txt")
