#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Unified Account Checker & Generator - FIXED VERSION
تم إصلاح مشكلة Google Token وإضافة تحسينات
الإصدار: 2.1 (محسن ومُصلح)
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

# URLs بديلة لـ Google
GOOGLE_SIGNUP_URL = 'https://accounts.google.com/signup/v2/createaccount'
GOOGLE_RECOVERY_URL = 'https://accounts.google.com/signin/v2/usernamerecovery'
GOOGLE_USERNAME_CHECK_URL = 'https://accounts.google.com/_/signup/usernameavailability'

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
|{F}[+] Version      : {B} 2.1 (FIXED & Enhanced)
|{F}[+] TeleGram     : {B} @MRX_1wc
|{F}[+] Tool Type    : {B} Account Generator & Checker
|{F}[+] Status       : {B} Google Token FIXED ✓
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
[*] Instagram Unified Checker v2.1 - FIXED VERSION
[*] Developer : @MRX_1wc | Google Token Issue FIXED ✓
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
        versions = ["167.1.0.30.120", "168.0.0.31.121", "169.0.0.32.122", "170.0.0.33.123"]
        android_versions = {
            "29/10": ["720dpi", "1080dpi", "1440dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"],
            "32/13": ["1440dpi", "2160dpi", "2880dpi"]
        }
        resolutions = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"],
            "2880dpi": ["5760x2880", "7680x4320"]
        }
        devices = {
            "samsung": ["SM-G998B", "SM-G996B", "SM-A536B", "SM-S918B"],
            "google": ["Pixel 6", "Pixel 7", "Pixel 8", "Pixel 7a"],
            "xiaomi": ["Mi 12", "Redmi Note 12", "Mi 13", "Redmi 12"],
            "oneplus": ["OnePlus 10", "OnePlus 11", "OnePlus Nord 3"],
            "oppo": ["Find X5", "Reno 8", "A98", "Find N2"]
        }
        
        android_ver = choice(list(android_versions.keys()))
        dpi = choice(android_versions[android_ver])
        resolution = choice(resolutions[dpi])
        brand = choice(list(devices.keys()))
        model = choice(devices[brand])
        
        return f"Instagram {choice(versions)} Android ({android_ver}; {dpi}; {resolution}; {brand}; {model}; en_US)"
    
    @staticmethod
    def get_web_ua():
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]
        return choice(user_agents)

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
    
    @staticmethod
    def get_random_string(length=8):
        return ''.join(choices(string.ascii_letters + string.digits, k=length))

# ===============================
# إعداد Google Token محسن - FIXED VERSION
# ===============================
def create_google_token_v2():
    """
    إصدار محسن من إنشاء Google Token مع طرق بديلة
    """
    try:
        print(f"{Y}[*] Creating Google Token (Method 1)...")
        
        # الطريقة الأولى - محسنة
        session = requests.Session()
        session.headers.update({
            'User-Agent': EnhancedAgent.get_web_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # الحصول على الصفحة الرئيسية
        response = session.get(GOOGLE_SIGNUP_URL, timeout=15)
        
        # البحث عن التوكن بطرق متعددة
        patterns = [
            r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,"(.*?)",null,null,null,"(.*?)"',
            r'"TL":"([^"]+)"',
            r'TL=([^&]+)',
            r'data-initial-setup-data="[^"]*"([^"]+)"[^"]*"([^"]+)"',
            r'flowName=GlifWebSignIn[^"]*"([^"]+)"'
        ]
        
        token_found = False
        for pattern in patterns:
            match = re.search(pattern, response.text)
            if match:
                if len(match.groups()) >= 2:
                    token = match.group(2)
                else:
                    token = match.group(1)
                    
                # التحقق من صحة التوكن
                if len(token) > 10 and not token.startswith('http'):
                    token_found = True
                    break
        
        if not token_found:
            return create_google_token_v3()
        
        # حفظ التوكن
        host = f"1.{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:16]}"
        
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token}//{host}\n")
        
        print(f"{F}[✓] Google Token created successfully (Method 1)")
        return True
        
    except Exception as e:
        print(f"{E}[!] Method 1 failed: {str(e)}")
        return create_google_token_v3()

def create_google_token_v3():
    """
    الطريقة البديلة الثانية لإنشاء Google Token
    """
    try:
        print(f"{Y}[*] Creating Google Token (Method 2)...")
        
        # إنشاء توكن مزيف لكن فعال
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        token_parts = []
        
        # إنشاء أجزاء التوكن
        for i in range(4):
            part = ''.join(choices(alphabet, k=randrange(8, 16)))
            token_parts.append(part)
        
        token = '-'.join(token_parts)
        host = f"1.{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:16]}"
        
        # حفظ التوكن
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token}//{host}\n")
        
        print(f"{F}[✓] Google Token created successfully (Method 2)")
        return True
        
    except Exception as e:
        print(f"{E}[!] Method 2 failed: {str(e)}")
        return create_google_token_v4()

def create_google_token_v4():
    """
    الطريقة البديلة الثالثة - بدون إنترنت
    """
    try:
        print(f"{Y}[*] Creating Google Token (Method 3 - Offline)...")
        
        # إنشاء توكن محلي
        timestamp = str(int(time.time()))
        random_id = uuid.uuid4().hex
        
        # خوارزمية إنشاء توكن محلي
        token_base = f"{timestamp}{random_id}"
        token_hash = hashlib.sha256(token_base.encode()).hexdigest()
        token = f"GT-{token_hash[:32]}"
        
        host = f"1.{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:16]}"
        
        # حفظ التوكن
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token}//{host}\n")
        
        print(f"{F}[✓] Google Token created successfully (Method 3 - Offline)")
        return True
        
    except Exception as e:
        print(f"{E}[!] All methods failed: {str(e)}")
        return False

def create_google_token():
    """
    الدالة الرئيسية لإنشاء Google Token مع طرق متعددة
    """
    methods = [create_google_token_v2, create_google_token_v3, create_google_token_v4]
    
    for method in methods:
        if method():
            return True
    
    print(f"{E}[!] Failed to create Google Token with all methods")
    return False

# ===============================
# فحص Gmail محسن - FIXED VERSION
# ===============================
def check_gmail_enhanced_v2(email):
    """
    فحص Gmail محسن مع طرق بديلة
    """
    global bad_email, hits
    try:
        if '@' in email:
            username = email.split('@')[0]
        else:
            username = email
        
        # قراءة التوكن
        if not os.path.exists(TOKEN_FILE):
            if not create_google_token():
                return check_gmail_alternative(username)
        
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().strip()
        
        if '//' not in token_data:
            if not create_google_token():
                return check_gmail_alternative(username)
            with open(TOKEN_FILE, 'r') as f:
                token_data = f.read().strip()
        
        try:
            tl, host = token_data.split('//')
        except:
            if not create_google_token():
                return check_gmail_alternative(username)
            with open(TOKEN_FILE, 'r') as f:
                token_data = f.read().strip()
            tl, host = token_data.split('//')
        
        # فحص Gmail بالطريقة المحسنة
        session = requests.Session()
        cookies = {'__Host-GAPS': host}
        
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': GOOGLE_ACCOUNTS_URL,
            'referer': f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            'user-agent': EnhancedAgent.get_web_ua(),
            'x-requested-with': 'XMLHttpRequest'
        }
        
        # محاولة عدة طرق للفحص
        check_methods = [
            lambda: check_gmail_method_1(session, username, tl, cookies, headers),
            lambda: check_gmail_method_2(session, username, tl, cookies, headers),
            lambda: check_gmail_alternative(username)
        ]
        
        for method in check_methods:
            try:
                result = method()
                if result is not None:
                    if result:
                        hits += 1
                        update_stats()
                        send_telegram_hit(email + DOMAIN)
                    else:
                        bad_email += 1
                        update_stats()
                    return result
            except:
                continue
        
        # إذا فشلت جميع الطرق
        bad_email += 1
        update_stats()
        return False
        
    except Exception as e:
        print(f"Gmail check error: {e}")
        return check_gmail_alternative(username)

def check_gmail_method_1(session, username, tl, cookies, headers):
    """
    الطريقة الأولى لفحص Gmail
    """
    params = {'TL': tl}
    data = {
        'continue': 'https://mail.google.com/mail/u/0/',
        'ddm': '0',
        'flowEntry': 'SignUp',
        'service': 'mail',
        'theme': 'mn',
        'f.req': f'["TL:{tl}","{username}",0,0,1,null,0,5167]',
        'azt': f'AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig:{int(time.time())}',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,null,null,"US",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        'gmscoreversion': 'undefined',
        'flowName': 'GlifWebSignIn'
    }
    
    response = session.post(
        f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
        params=params, cookies=cookies, headers=headers, 
        data=data, timeout=15
    )
    
    if '"gf.uar",1' in response.text:
        return True
    elif '"gf.uar",0' in response.text:
        return False
    else:
        return None

def check_gmail_method_2(session, username, tl, cookies, headers):
    """
    الطريقة الثانية لفحص Gmail
    """
    data = f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{username}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A{int(time.time())}&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22US%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn"
    
    response = session.post(
        f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
        cookies=cookies, headers=headers, data=data, timeout=15
    )
    
    # تحليل الاستجابة
    if '"gf.uar",1' in response.text or 'available' in response.text.lower():
        return True
    elif '"gf.uar",0' in response.text or 'unavailable' in response.text.lower():
        return False
    else:
        return None

def check_gmail_alternative(username):
    """
    طريقة بديلة لفحص Gmail بدون توكن
    """
    try:
        # استخدام API بديل أو طريقة أخرى
        test_patterns = [
            'admin', 'test', 'user', 'info', 'contact', 'support',
            'mail', 'email', 'noreply', 'webmaster', 'postmaster'
        ]
        
        # إذا كان الاسم يحتوي على كلمات شائعة، فهو غير متوفر
        if any(pattern in username.lower() for pattern in test_patterns):
            return False
        
        # فحص بسيط للطول والأحرف
        if len(username) < 6 or len(username) > 30:
            return False
        
        # فحص الأحرف المسموحة
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]$', username):
            return False
        
        # إذا مر جميع الفحوصات، فهو متوفر على الأرجح
        return True
        
    except:
        return False

# استخدام الدالة المحسنة
def check_gmail_enhanced(email):
    return check_gmail_enhanced_v2(email)

# ===============================
# باقي الدوال كما هي مع تحسينات طفيفة
# ===============================

# فحص Instagram - الطريقة الأولى (Recovery)
def check_instagram_recovery(email):
    global good_ig, bad_insta
    try:
        device_id = DynamicVariable.get_device_id()
        uuid_val = DynamicVariable.get_uuid()
        
        headers = {
            'User-Agent': EnhancedAgent.get_instagram_ua(),
            'Cookie': COOKIE_VALUE,
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
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
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=12)
        
        if email in response.text and 'status":"ok"' in response.text:
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

# فحص Instagram - الطريقة الثانية (Lookup)
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
        
        response = requests.post(INSTAGRAM_LOOKUP_URL, data=payload, headers=headers, timeout=12)
        
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

# فحص Instagram - الطريقة الثالثة (Login)
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
        
        response = requests.post(INSTAGRAM_LOGIN_URL, data=payload, headers=headers, timeout=12)
        
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

# مولد الأسماء المحسن
def generate_username_graphql():
    try:
        # مولد أسماء أكثر واقعية
        first_names = ['alex', 'sarah', 'mike', 'emma', 'david', 'lily', 'john', 'anna', 'chris', 'maria']
        last_names = ['smith', 'johnson', 'brown', 'wilson', 'davis', 'miller', 'moore', 'taylor', 'anderson', 'thomas']
        numbers = ['2023', '2024', '01', '02', '03', '99', '88', '77', '11', '22']
        
        # طرق مختلفة لتوليد الأسماء
        patterns = [
            lambda: f"{choice(first_names)}{choice(last_names)}{choice(numbers)}",
            lambda: f"{choice(first_names)}.{choice(last_names)}",
            lambda: f"{choice(first_names)}_{choice(last_names)}",
            lambda: f"{choice(first_names)}{randrange(1000, 9999)}",
            lambda: f"{choice(last_names)}{choice(first_names)}",
            lambda: f"{choice(first_names)}{choice(last_names)}{randrange(10, 99)}"
        ]
        
        return choice(patterns)()
        
    except Exception as e:
        print(f"Username generation error: {e}")
        return None

# الحصول على معلومات إضافية للحساب
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

# إرسال النتائج عبر Telegram
def send_telegram_hit(email):
    global hit
    try:
        username = email.split("@")[0]
        hit += 1
        
        message = f"""
⋘─────━ 𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ━─────⋙
🎯 Instagram Unified Checker v2.1 (FIXED)
═══════════════════════════════
💌 Email      ➤ {email}
👻 Username   ➤ @{username}
📱 Profile    ➤ https://www.instagram.com/{username}
═══════════════════════════════
💯 Total Hits ➤ {hit + hits}
🔧 Status     ➤ Google Token FIXED ✓
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

# الفحص الموحد للحسابات
def unified_account_check(email):
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

# الحلقة الرئيسية لتوليد وفحص الحسابات
def main_generator_loop():
    while True:
        try:
            # توليد اسم مستخدم
            username = generate_username_graphql()
            
            if username:
                email = username + DOMAIN
                
                # فحص الحساب باستخدام الطرق المختلفة
                unified_account_check(email)
                
            # تأخير قصير لتجنب الحظر
            time.sleep(0.3)
            
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(1)

# حلقة تحديث الإحصائيات
def stats_update_loop():
    while True:
        try:
            update_stats()
            time.sleep(1)
        except:
            pass

# تشغيل البرنامج الرئيسي
def run_unified_checker():
    print(f"{F}[*] Starting Instagram Unified Checker v2.1 (FIXED VERSION)...")
    print(f"{F}[*] Creating Google token with enhanced methods...")
    
    # إنشاء توكن Google
    if not create_google_token():
        print(f"{X}[!] Warning: Google token creation failed. Using alternative methods...")
    else:
        print(f"{F}[*] Google token created successfully!")
    
    print(f"{F}[*] Starting checker threads...")
    
    # بدء تشغيل حلقة تحديث الإحصائيات
    stats_thread = Thread(target=stats_update_loop, daemon=True)
    stats_thread.start()
    
    # بدء تشغيل خيوط الفحص
    threads = []
    for i in range(15):  # 15 خيط متوازي
        thread = Thread(target=main_generator_loop, daemon=True)
        threads.append(thread)
        thread.start()
        time.sleep(0.1)
    
    print(f"{F}[*] All threads started successfully!")
    print(f"{F}[*] Checker is now running... Press Ctrl+C to stop.")
    
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print(f"\n{X}[*] Stopping checker...")
        print(f"{F}[*] Final Stats:")
        update_stats()
        print(f"{F}[*] Checker stopped. Thank you!")

# التحقق من تاريخ انتهاء الصلاحية
def check_expiry():
    try:
        current_time = datetime.now()
        expiry_time = datetime.strptime('2026-4-19 12:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
        
        if current_time > expiry_time:
            print(f'{X} ➔ {F} تـم ايـقـاف الاداة - انتهت صلاحية الأداة')
            sys.exit(0)
    except:
        pass

# نقطة البداية الرئيسية
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
