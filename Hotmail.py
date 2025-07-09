import requests
from uuid import uuid4
from secrets import token_hex
from user_agent import generate_user_agent
import re
import json
import random
import os
import string
import sys
import time
from pazok import tele_ms

o = "\033[38;5;208m"  
e = "\033[38;5;105m"  
E = "\033[38;5;250m"  
m = "\033[38;5;15m"   
f = "\033[38;5;82m"   
b = "\033[38;5;51m"   
y = "\033[38;5;226m"  
j = "\033[38;5;201m"  
x = "\033[38;5;196m"  
Z = "\033[38;5;196m"  # الأحمر  
C = "\033[38;5;250m"	  # الرمادي الفاتح  
e = "\033[38;5;206m"  # الوردي  

logo = """ 
            \u001b[38;5;220m                ⠑⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⢹⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⣾⣷⡀⠀⠀⣸⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⢻⣿⣿⣿⣾⣿⣿⣿⣿⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠈⣿⣿⣿⣿⣿⣿⣿⠟⠁⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣠⣾⣿⠃⠀⠀⠀⢹⣿⣿⣿⣿⠟⠁⠀⠀⢻⣧⣄⡀⠀⢸⣶⣄⠀⠀⠀⠀
            ⠀⠀⠀⣠⣾⣿⣿⠇⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⢸⣿⣿⣿⡄⠈⢿⣿⣦⠀⠀⠀
            ⠀⠀⣰⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⣿⣿⣿⣿⣷⣤⣠⣴⣿⣿⣿⣿⠇⠀⢸⣿⣿⡇⠀⠀
            ⠀⢀⣿⠟⣩⣬⣥⣭⣬⣤⣭⣤⣭⡉⢻⣿⣿⣿⣿⠉⢬⣥⣭⡍⠻⠀⢀⣾⠟⣩⣥⣤⡤
            ⠀⠨⠃⠴⠿⠿⠿⠿⠿⣿⣿⣿⠏⣸⣿⣿⣿⣿⣷⣄⠻⣿⣿⣧⡘⠻⢁⣾⣿⡿⠋⠀
            ⠀⠀⢳⣶⣶⣶⣶⠖⣠⣾⣿⡿⢡⣴⣿⣿⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣶⣿⣿⠟⠁⠀⠀
            ⠀⢠⣾⣿⣿⠟⢡⣾⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⣿⣿⣿⢁⣾⣷⡄⠀
            ⠀⣿⣿⡇⢀⣼⣿⣿⠏⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⢰⣾⣿⡿⠀
            ⠀⠙⢿⣷⣤⡀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⢠⣼⣿⠟⠁⠀
            ⠀⠀⡄⢹⣿⡷⠄⠀⠀⠀⠀⠈⠙⠛⠟⣹⣿⣏⠻⠛⠋⠁⠀⠀⠀⠀⠠⠿⣿⠏⣠⠀⠀
            ⠀⠀⣿⡄⣿⣾⣶⣦⣄⣀⣀⣀⠄⣠⣾⠟⠿⠻⣷⣄⡠⣀⣀⣀⣤⣶⣾⣿⣯⢰⣿⡀⠀
            ⢀⣼⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
            ⠀⠛⠿⣿⣿⡿⠿⠟⠛⣛⡻⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⢛⣉⡙⠛⠿⠿⢿⠿⠿⠋⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣾⣿⣿⣦⣴⣿⣦⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⢸⣿⢿⣿⣿⣿⡇⢀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⣿⠀⠸⣿⢸⣿⣿⣿⡇⢸⣿⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠀⠀⠀⠘⢿⣿⠋⠀⠈⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(logo) 

def type_writer(text, delay=0.05):  
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

message = f"""
      	         Welcome to our world - @QH_PJ
        
"""

type_writer(message, 0.02)

token = input(f"{E}[ {Z}➠ {E}] {e}𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍  {Z} : {E}")

id = input(f"{C}[ {Z}➠ {C}] {e}𝐄𝐍𝐓𝐄𝐑 𝐈𝐃 {Z}: {E}")


os.system("clear")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

god_hot = 0
bad_hot = 0
god_insta = 0
bad_insta = 0

def update_display(email):
    clear()
    text = f"""
        {j}━━━━━━━━━━ {m} @QH_PJ
        {j}┃
        {j}┣━ {o}Email: {f}{email}{j}
        {j}┣━ {o}Instagram (Good): {f}{god_insta}{j}
        {j}┣━ {o}Hotmail (Good): {f}{god_hot}{j}
        {j}┣━ {o}Instagram (Bad): {x}{bad_insta}{j}
        {j}┣━ {o}Hotmail (Bad): {x}{bad_hot}{j}
        {j}┗━ {x}Errors {E}: {x}{bad_hot + bad_insta}{m}
    """
    print(text)

def hro(text):
    ro = r'_*[]()~`>#+-=|{}.!'
    return ''.join('\\' + char if char in ro else char for char in text)
    
def insta(email):
    si = requests.Session()
    ag = generate_user_agent().replace("136.0.0.34.124", "6.12.1") \
        .replace("208061712", "").replace("en_US", "ar_EG_#u-nu-latn")
    
    try:
        csr = si.get(
            "https://www.instagram.com/accounts",
            headers={'User-Agent': ag}
        ).text.split('{"csrf_token":"')[1].split('"}')[0]

        mid = requests.get(
            "https://www.instagram.com/api/graphql",
            headers={'User-Agent': ag}
        ).headers.get("Set-Cookie", "").split("mid=")[1].split(";")[0]
        
        url = "https://i.instagram.com/api/v1/accounts/login/"
        
        headers = {
            'User-Agent': ag,
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Cookie2': "$Version=1",
            'Accept-Language': "ar-EG, en-US",
            'X-IG-Connection-Type': "WIFI",
            'X-IG-Capabilities': "AQ==",
            'Cookie': f"mid={mid}; csrftoken={csr}"
        }
        
        data = {
            'uuid': str(uuid4()),
            'password': '@QH_PJ',
            'username': email,
            'device_id': "android-" + token_hex(8),
            '_csrftoken': csr,
            'ig_sig_key_version': "4"
        }

        response = requests.post(url, data=data, headers=headers).json()
        if response.get("error_type") == "bad_password":
            return True
        elif response.get("error_type") == "invalid_user":
            return False
    except:
        return "error"

def hotmail(email):
    try:
        if "@hotmail.com" not in email:
            email += "@hotmail.com"

        response = requests.get('https://account.live.com/signup')
        cookies = response.cookies.get_dict()
        amsc = cookies.get('amsc', '')

        canary_match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if not canary_match:
            return "Error"

        canary = canary_match.group(1).encode('utf-8').decode('unicode_escape')

        url = "https://signup.live.com/API/CheckAvailableSigninNames"
        headers = {"Canary": canary, "Cookie": f"amsc={amsc}"}
        data = {"includeSuggestions": True, "signInName": email}

        response = requests.post(url, headers=headers, data=json.dumps(data)).json()
        return response.get("isAvailable")
    except:
        return "error"

while True:
    mea = string.ascii_lowercase + string.digits
    email = ''.join(random.choice(mea) for _ in range(12)) + "@hotmail.com"

    if insta(email) == True:
        god_insta += 1
    else:
        bad_insta += 1

    if hotmail(email) == True:
        god_hot += 1
    else:
        bad_hot += 1
    if insta and hotmail == True:
         meg = f"*Email* : `{hro(email)}`"
         mot = "المطور", "t.me/QH_PJ"
         tele_ms(token, id, meg, buttons=mot)
         update_display(email)

    update_display(email)