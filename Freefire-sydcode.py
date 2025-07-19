import requests
import random
from user_agent import generate_user_agent

Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

id = input(f'{C} تويڪن ')
tok = input(f'{B} اﯾدﯾك')
	
while True:
	
	ali =''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(12))
	
	code = ali
	cookies = {
	    '_ga': 'GA1.1.975108908.1736786668',
	    'datadome': 'u1f_XcLTuhn8JeGhcs4ulKuPocq88dPrwgGRi8LwyFK6mAQLvg9s21PlWbCPXF1_hgVOvTJQejxJVrH4rdqo0jXHpfIpfWIk0kcgPAWo_3t1vmuWBEFjpj1TXREEKKpJ',
	    'apple_state_key': '1883e4ece01611efb7c6922ce10501a4',
	    '_ga_G8QGMJPWWV': 'GS1.1.1738357077.2.1.1738357170.0.0.0',
	    '_ga_Y1QNJ6ZLV6': 'GS1.1.1738357017.3.1.1738357172.0.0.0',
	}
	
	headers = {
	    'authority': 'prod-api.reward.ff.garena.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'access-token': '3a517500afc9ac7d03eea1dcc03e3df4ac003890f2b1d85d5021fde54effdb31',
	    'code': 'null',
	    'content-type': 'application/json',
	    # 'cookie': '_ga=GA1.1.975108908.1736786668; datadome=u1f_XcLTuhn8JeGhcs4ulKuPocq88dPrwgGRi8LwyFK6mAQLvg9s21PlWbCPXF1_hgVOvTJQejxJVrH4rdqo0jXHpfIpfWIk0kcgPAWo_3t1vmuWBEFjpj1TXREEKKpJ; apple_state_key=1883e4ece01611efb7c6922ce10501a4; _ga_G8QGMJPWWV=GS1.1.1738357077.2.1.1738357170.0.0.0; _ga_Y1QNJ6ZLV6=GS1.1.1738357017.3.1.1738357172.0.0.0',
	    'lang': 'ar',
	    'origin': 'https://reward.ff.garena.com',
	    'referer': 'https://reward.ff.garena.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': str(generate_user_agent()),
	}
	
	json_data = {
	    'serialno': code,
	}
	
	response = requests.post(
	    'https://prod-api.reward.ff.garena.com/redemption/api/game/ff/redeem/',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).json()
	
	if not 'error_invalid_serialno' in response:
		print(f'{R}GOOD CODE : {code}')
		
		tt = f''' 
				
↜ ↜ ↜ ↜ ↜ ↜ ↜ ↜ ↜ ↜ 

 عمك ديڤل جابلك ڪود فري فاير 

الڪود  : {code}

قناتي :@M02MMO

°^°^°^°^°^°^°^°^°^°^°^°^°^°^°^°		
		'''
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text="+str(tt))
		
		
	else:
		print(f'{Z}BAD CODE : {code}')
		
		
ali()
time.sleep(14)