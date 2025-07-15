import requests
import threading
import random
import datetime
from user_agent import generate_user_agent as x
from SignerPy import sign,get
import os
import sys
import ST4,secrets
import time
import uuid
from urllib.parse import urlencode
from os import urandom
import binascii
from os import system 
import hsopyt 
import string
import time,hashlib
import string,secrets
from urllib.parse import urlencode
import random,uuid
import json
import binascii
import os
from SignerPy import sign, get
from random import choice,randrange,randint
from os import urandom
from threading import Thread as F400
from concurrent.futures import ThreadPoolExecutor as F300
import datetime
import sys
import re

from ST4 import HOTMAIL as nothing
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
Y="\033[1;33m" # Yellow
class HSO:
    def __init__(self):
        self.logo= ''' 
        '''
        self.id=input(f"{G}[ + ] id : {M} ")
        self.token=input(f"{G}[ + ] Token  : {M} ")
        os.system("cls" if os.name == "nt" else "clear")
        self.hit=0
        self.gt=0
        self.bt=0
        self.ge=0
        self.be=0
        self.secret=secrets.token_hex(16)
        self.ses=requests.Session()
        self.colors = [BR, AH2, AS2, MJ, MJ2, MJ3, MJ4, ma]
        self.random_color = random.choice(self.colors)
        self.q=(self.random_color+self.logo)
        for i in self.q.splitlines():
            print(i)
            time.sleep(0.05)
        self.name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
        self.keyword= random.choice(
    [
    'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',  
    '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
    'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
    'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
    'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
    'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
    'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    ]
    )
        self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
        self.select()
    def select(self):
        ii = '''
[ 1 ] = Random Gmail
[ 2 ] = Random Hotmail
[ 3 ] = Check List Gmail
[ 4 ] = Check List Hotmail
'''
        print(ii)
        try:
            self.sec = int(input("Choice Numper  : "))
        except Exception as e:
            print(e)
            exit("Error Input ")
        if self.sec == 1:
            try:
                self.max = int(input("input Numper For Threading 1-50  :  "))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            for i in range(self.max):
                threading.Thread(target=self.serch_gm).start()
        elif self.sec ==2:
            try:
                self.max = int(input("input Numper For Threading 1-50"))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            for i in range(self.max):
                threading.Thread(target=self.Serch_hotmail).start()
        elif self.sec ==3:
            self.file = input("File Name > ")
            try:
                self.max = int(input("input Numper For Threading 1-50"))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_gmail()
        elif self.sec ==4:
            self.file = input("File Name > ")
            try:
                self.max = int(input("input Numper For Threading 1-50"))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_hotmail()

    def check_hotmai(self , email):
        try:
            data = nothing.CheckEmail(email)['data']['status']
            if data == True : 
                self.ge+=1
                self.info(email)
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()
                
            elif data == False:
                self.be +=1
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()
        except :
            pass
    def signn(self, params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
             x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
             data=payload
             if not unix: unix = int(time.time())
             return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : hsopyt.Ladon.encrypt(unix, license_id, aid),"x-argus"   : hsopyt.Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
    def info(self,email):
            self.hit+=1

            user= email.split("@")[0]
            patre = {
    "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"
        }
            tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=patre).text
            try:
                getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                id = str(getting.split('id":"')[1]).split('",')[0]
                name = str(getting.split('nickname":"')[1]).split('",')[0]
                bio = str(getting.split('signature":"')[1]).split('",')[0]
                country = str(getting.split('region":"')[1]).split('",')[0]
                private = str(getting.split('privateAccount":')[1]).split(',"')[0]
                followers = str(getting.split('followerCount":')[1]).split(',"')[0]
                following = str(getting.split('followingCount":')[1]).split(',"')[0]
                like = str(getting.split('heart":')[1]).split(',"')[0]
                video = str(getting.split('videoCount":')[1]).split(',"')[0]
                B = bin(int(id))[2:]
                L, BS = 0, ""
                while L < 31:
                    BS += B[L]
                    L += 1
                Date = datetime.datetime.fromtimestamp(int(BS, 2)).strftime('%Y')
                ff=f'''
— — — — — — — — — — — — —
Hit : {self.hit}
name :{name}
username : {user}
email : {email}
id :{id}
following : {following}
followers :{followers}
like : {like}
video : {video}
date : {Date}
privte : {private}
flag :{self.country_code_to_flag(country)}
country : {country}
prog : @b_azo
— — — — — — — — — — — — —
    '''
                with open("TIKTOK.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
                
            except Exception as e:
                print(e)
                ff=f'''
— — — — — — — — — — — — —
hit :{self.hit}
username : {user}
email  : {email}
prog : @b_azo
— — — — — — — — — — — — —
    '''
                with open("TIKTOK - BROKIN.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
    def API_CH(self , email ):
        cookies ={
            "passport_csrf_token": self.secret,
            "passport_csrf_token_default": self.secret,
            "sessionid":random.choice(['336a32fd882ea7a9a209f5f6f1001aec', 'fe087743cb83b87fe511c4dcc2b54b9e', '0a0fef60a9c37390453fd0a2f5eae084', 'c5913e6c105f88b19e4a6da96225b0a5', '686a259b53d792a96eb099e6326536f3', 'd2906ee6e5024de40be103e937e66bb1', '5e1078840499161441c8a8ca40295fb1', '46bfa28933895ace05a96a0ba0608476', '2b5abd2c94b5e57fa57d2d792fcd958b', '78cd438e41a1be9f27434a7ecb45d1f6', 'befcea68deff3c0877b5f632281d0e5c', '28797e6bb6e3b4a2924bdd17d5ac2c9d', 'ecbce30174a3109533e8c9db2b400e9f', 'de296140fdf052974d313dffaeac39a8', '9fddad156790a04d6dc9f6e150d7cc5e', '10b30da78a13e426e7c2f2019195fb07', '6805b2b6487750f8a9ed74661eca0a18', 'def6f7881ea24c7c6e2f2faafd749e33', '5d46a008e884feab7008d237231e7c2a', '611254e09febca06d81e7f4ee9acf739', '994be4fc2df6c999579844375cc4eb05', 'a452e90fde70ea9e9083d06ad000d69b', '86fd5bd98326e1478e6eec4aeb581640', '5cd2eb39aadf7c11bc741131fefe8352', 'd81b5f29f47c0f621848a5bed9906205', 'ad597479d1c78c6d7c07135b98883ec7', 'e2b90094da6ff546902b52c7cbcea7bb', 'b9d8b79367847fd9dfb8647bb96edd41', '38df69157cd19f89825ad86e40533b3e', 'eb3fa50f60dd60f3a415f4d57d5c368d', 'e3f82adbd81c7e3fb02160526497f0d5', '8a9e4778c7074dc6497bce8fbc3e7be6', '6fcad57feb38a57155455fadf8fb8caa', '7872475d47b25e925845cb90e42e4c31', 'dc38c5c297ad483b59e13181b21cc0e8', '78f01b752b0e291c4177e2319871e5cd', 'f99638331ea251eba1dfae6ad3e331cd', 'c79eddc5e5f2f71fee0ab13cc7095483', '9bb881516b14276d1506c5b13201a641', '1d5a8ad70fe1273483834fd99ba1cdee', '531e7ed1aa699a929b313b8960677c07', 'a3b5391061c14c5bea994a67ecba701a', '8b8e6c66621495028a8736288d4b9f60', '36726a0145f85571c4d7919a564a330d', '3572063b01656d663061a7ed0888dd30', '3e99fe2e40577af27dc4fb15f9b438f7', 'c075d398cbf3a2b2c07684df36984341', '80b98f6c3b0e9eb1737f0fb96cb73e1d', '51ccd10042f16e1768008a7e7de06abc', '99b2c615978200c679b321f04d314d49', 'e6be1a32ae14b07e95a33d79e907ab75', '6452b4925edad1b34284d9cf4887d281', '85bae7724ff412e6416add3975d7578f', '8a127cc4be5a9cfa63e6c6f67219a490', 'e7517be667bf0081e88403632e3c94d6', '475880946e2be5c2539a6c51746d2a27', '12700e53ced122977a6705435f8dc433', '99199284fc83817a51844b35e12b9a18', '41dede88fec05de213462698b04ce27f', '2c973cfb6559bc0369cefdbb75d5cbb7', 'c6a4f0c449e315424289978d8e3f05f7', '1701c221c9719dcc25ebe117759c06b3', '98b6f608bcb1a1714f7d14ec97397dad', '14cc3c5d685cd6f93fc178d8f2c2632f', 'c33e3da3ec3b8e611625db85fb8ea360', 'd68ba7cadc2ee0459db73a3552e734da', '70ef7ff3f4a3b26f833fbcbd1c03051f', '27ea1b3c8a253ea83a2fe37dc284e68e', '7de5eee54214f4193593f8f3135082b2', 'cd0f53b4792b963e9d0a2330d2bba74b', '23126441f9d70e4b3a09d6b02b88f4db', 'dc7d2164919b5432676b4a8315d8f8b3', 'f98471c9220848e8fa3ad8ea31c86225', '3da3384851b7b0d98d23ef5c9b363efc', '1edfd0dbb4f14549ead50fb19dc0dae3', '440aa49c72a868f991c4ab05226d3250', 'b848e09658da067adc08221282fe8cce', '54377e9fe52cdffec1cf9f94d961dbf0', '5706974cb7a333f2aa6344182fa9e24c', '3886d9870710210bbae36ea174116b46', '3d034db5510fb4577acea1bb7853285f', '771fc5bce51efef06174c5aa78fa896c', '31a3dcfa596e1b8904e7eb3234154f12', 'a2f9f142f0a65082b5b288ca674ab068', 'd47c091970b7ebe7eceb45f6db5bf377', '8d40480a584859232cf9db44895307c8', '77e24da2dd86794d0233b45f9122dd6a', 'f2da58a0f3b534620e8ca7d070be1457', 'e0a008174fbb2f2c1923e7ca2d7ae0ba', '711326a9ce06c555903b43e5d0a8f64e', '160ca3c436693fcdc1165149c04d26c6', 'db5aed4cc13b8c33d4a409948ba8b677', '6b73e7069c58abfa77d72af913c75601', 'b8f86957a52616badf8897c94c3705d6', 'fb3ecd7a225441bcdf0f82a153976c51', '959c67bd75dce25e3913ddbe7831013c', '563c76e23b0f1c8fb34fc4b2016192a2', '01d9a4ee761a44ab1f80d4554cc10301', '0ec7f88b7fa70feb1badea37cc5748d6', '94fa96e1fc5ed700901c37a2a03966c0', 'ea8303df864b6fbe25a73fc6c02fe4e9', '98ac6a1ed1cea0cd7dd86da4ad548983', '9e42fb4166611ce207b8bfcf8e76193d', 'f8448f180e37a6157b2fa6728929c858', '300d027cc70fd71efa2dc4e1661bd053', '28e5067ca59aefefe8a5716a4c257019', '3a3ad8e66b4a328280aeb8def7e4526c', '7a35f4c1fe2909ee619f881438757502', 'cfd0cea0924da90ef2d7e413f4d1b618', '3c639274b33f920b4e2509382a26e737', '62ce3b7afc11cc60503d57c50d46eb4a', '5fdd7957547d882ca1e3c5b3d33420e1', '13de4a9b03153f3d415746951871cab1', '114f488327fe3f9e0cb7e5d0c93e18da', '759fca154d2a4e1f801842e3a79f6766', '0b6ad9305fbea569f7c5d4b9d17cbdc9', 'd176247e0d0e5991755527960c9bac6e', 'f1b2fee1dd90c445fd9c91de64b3bdbb', '7b7230e76e67e6d467aa6c6e33694b23', 'd7f340e143dbb4eab73dd8f675d20b97', '7013e9767ad43770d1a86cdd45b880e5', '4505ccb48f0a6a2541e34caaefac8840', 'e56d4e0c3f4034f9d6aada115759169c', 'c33a0ef15486debe17f4a38fc4bcb1b0', 'cc961ebfa09ba689786484f07b9b932c', 'f80b8abf5291f2d958ca9bbc8285eb8a', 'e370e7e1b0a0010360282d131c2d0613', '63ab5a670d8d6a9fbd14f7d3fd0b30da', 'f699c60e0671ac8cf07b47b98876e750', '8c77d0106c0249ad50fdccdcea3ab888', '7c67d00d73751c447972067da77b9c08', 'ba0cb1b483e91b176e0a9e8991d24d29', 'bc4d7382e95f3b9fa79d9164dac426e6', '2675c0445217ed43acaa90e9835d3801', '6f968388b83d7ff2e19659c527b1ad08'
            ])
            }
        self.ses.cookies.update(cookies)
        device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
        device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
        regions = ["AE", "IQ", "US", "FR", "DE"]
        languages = ["en"]
        paramss = {
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
        'openudid': str(binascii.hexlify(urandom(8)).decode()),
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
        'cront_version': "1c651b66_2024-08-30",
        'ttnet_version': "4.2.195.8-tiktok",
        'use_store_region_cookie': "1",
        'ab_version':'37.8.5'
        }
        
        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",    'cdid': str(uuid.uuid4()),'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),    'iid': str(random.randint(1, 10**19)),    'device_id': str(random.randint(1, 10**19)),    'openudid': str(binascii.hexlify(urandom(8)).decode())}
        _rticket = params["_rticket"]
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params={'_rticket':_rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','fixed_mix_mode':'1','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','mix_mode':'1','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','region':'IQ','request_tag_from':'h5','resolution':'720%2A1280','rrb':'%7B%7D','scene':'4','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163105','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
        device_type = params["device_type"]
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

        m=self. signn(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        headers = {
        'User-Agent': user_agent,
        'x-tt-passport-csrf-token': self. secret,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-argus': m["x-argus"],
        'x-gorgon': m["x-gorgon"],
        'x-khronos': m["x-khronos"],
        'x-ladon': m["x-ladon"]
        }
        try:
            url="https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
            #url='https://api31-normal-useast1a.tiktokv.com/passport/email/bind'
            res = requests. post(url, params=params, headers=headers,data={"email":email},cookies=cookies).text
            #  print (res)

            if 'Email is linked to another account. Unlink or try another email.'in res:
                if "@gmail.com"in email:
                    self. check_email(email)
                #  system ('clear')            
                    self.gt+=1
                    sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                    sys.stdout.flush()    
                # print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")    
                elif "@hotmail.com"in email:
                    self.check_hotmai(email)
                    self.gt+=1
                    sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                    sys.stdout.flush()
            else:
                if "@gmail.com"in email:          
                    self.bt+=1
                    sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                    sys.stdout.flush()    
                elif "@hotmail.com"in email:
                    self.bt+=1
                    sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                    sys.stdout.flush()
        except:
            pass
    def country_code_to_flag(self , code):
        if len(code) != 2:
            return "N/L"
        return chr(ord(code[0].upper()) + 127397) + chr(ord(code[1].upper()) + 127397)
    def check_email(self,email):
        if '@' in email:email=email.split('@')[0]
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://accounts.google.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-browser-channel': 'stable',
                'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
                'x-browser-year': '2024',
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

            r = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
            tl=r.url.split('TL=')[1]
            s1= r.text.split('"Qzxixc":"')[1].split('"')[0]
            at = r.text.split('"SNlM0e":"')[1].split('"')[0]
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }

            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)

            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text



            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }
            params = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text
            if 'steps/signup/password'in r:
                self.ge+=1
                email=email+"@gmail.com"
                self.domin =email.split("@")[1]
                self.info(email)
                #system ('clear')
                sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                sys.stdout.flush()       
                #print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")
            else:
              #  system ('clear')
                self.be+=1
                sys.stdout.write(f"\r{F}• True : {M}{self.ge} {Z} • False : {M}{self.bt} {X}• Not : {M}{self.be}")
                sys.stdout.flush()
              #  print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")
        except Exception as e:
            ''
    def serch_gm(self):
        while True:
            keyword=''.join((random.choice(self.keyword) for i in range(random.randrange(4,9))))
            url = "https://search19-normal-alisg.tiktokv.com/aweme/v1/general/search/single/"
            params = {
                'cursor': '10',
                'enable_lite_workflow': '0',
                'enter_from': 'homepage_hot',
                'enable_lite_cut': '1',
                'backtrace': 'ad_cursor%253D12%253Bcs_next_img_group%253D1%253Bcurrent_page%253D1%253Brs_card_next_index%253D0%253Brs_next_a%253D1%253Brs_next_index%253D4%253Brs_word_next_index%253D0',
                'count': '20',
                'last_search_id': '202505031730279957F33446D550A9EB88',
                'end_to_end_search_session_id': '',
                'keyword':keyword ,
                'query_correct_type': '0',
                'search_source': 'normal_search',
                'search_id': '20250503173028ABF760554790F9B05684',
                'request_tag_from': 'h5',
                'manifest_version_code': '350302',
                '_rticket': '1746293432361',
                'app_language': 'ar',
                'app_type': 'normal',
                'iid': '7496924689664935687',
                'channel': 'googleplay',
                'device_type': 'RMX3941',
                'language': 'ar',
                'host_abi': 'arm64-v8a',
                'locale': 'ar',
                'resolution': '1080*2290',
                'openudid': '4a4760153b7de268',
                'update_version_code': '350302',
                'ac2': 'wifi5g',
                'cdid': 'e1e7a0b5-26b0-4052-becb-723516452cbd',
                'sys_region': 'IQ',
                'os_api': '34',
                'timezone_name': 'Asia%2FBaghdad',
                'dpi': '480',
                'carrier_region': 'IQ',
                'ac': 'wifi',
                'device_id': '7458734982867355141',
                'os_version': '12',
                'timezone_offset': '10800',
                'version_code': '350302',
                'app_name': 'musically_go',
                'ab_version': '35.3.2',
                'version_name': '35.3.2',
                'device_brand': 'realme',
                'op_region': 'IQ',
                'ssmix': 'a',
                'device_platform': 'android',
                'build_number': '35.3.2',
                'region': 'IQ',
                'aid': '1340',
                'ts': '1746290524'
            }
            signed_params = get(params=params)
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 12; ar_IQ; RMX3941; Build/UKQ1.231108.001;tt-ok/3.12.13.21-ul)",    
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-tt-req-timeout': "90000",
                'sdk-version': "2",
                'passport-sdk-version': "30990",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.2.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "did",
            }
            signature = sign(params=signed_params)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })
            try:
                response = requests.get(url, params=signed_params, headers=headers)
                data=response.json()
                if 'data' in data and isinstance(data['data'], list):
                    for item in data['data']:
                        aweme = item.get('aweme_info')
                        if aweme and 'author' in aweme:
                            author = aweme['author']
                            username = author.get('unique_id') 
                            followers = author.get('follower_count') 
                            email=username+"@gmail.com"    
                            
                            self.API_CH(email)
            except:""
    def Serch_hotmail(self):
        while True:
            keyword=''.join((random.choice(self.keyword) for i in range(random.randrange(4,9))))
            url = "https://search19-normal-alisg.tiktokv.com/aweme/v1/general/search/single/"
            params = {
                'cursor': '10',
                'enable_lite_workflow': '0',
                'enter_from': 'homepage_hot',
                'enable_lite_cut': '1',
                'backtrace': 'ad_cursor%253D12%253Bcs_next_img_group%253D1%253Bcurrent_page%253D1%253Brs_card_next_index%253D0%253Brs_next_a%253D1%253Brs_next_index%253D4%253Brs_word_next_index%253D0',
                'count': '20',
                'last_search_id': '202505031730279957F33446D550A9EB88',
                'end_to_end_search_session_id': '',
                'keyword':keyword ,
                'query_correct_type': '0',
                'search_source': 'normal_search',
                'search_id': '20250503173028ABF760554790F9B05684',
                'request_tag_from': 'h5',
                'manifest_version_code': '350302',
                '_rticket': '1746293432361',
                'app_language': 'ar',
                'app_type': 'normal',
                'iid': '7496924689664935687',
                'channel': 'googleplay',
                'device_type': 'RMX3941',
                'language': 'ar',
                'host_abi': 'arm64-v8a',
                'locale': 'ar',
                'resolution': '1080*2290',
                'openudid': '4a4760153b7de268',
                'update_version_code': '350302',
                'ac2': 'wifi5g',
                'cdid': 'e1e7a0b5-26b0-4052-becb-723516452cbd',
                'sys_region': 'IQ',
                'os_api': '34',
                'timezone_name': 'Asia%2FBaghdad',
                'dpi': '480',
                'carrier_region': 'IQ',
                'ac': 'wifi',
                'device_id': '7458734982867355141',
                'os_version': '12',
                'timezone_offset': '10800',
                'version_code': '350302',
                'app_name': 'musically_go',
                'ab_version': '35.3.2',
                'version_name': '35.3.2',
                'device_brand': 'realme',
                'op_region': 'IQ',
                'ssmix': 'a',
                'device_platform': 'android',
                'build_number': '35.3.2',
                'region': 'IQ',
                'aid': '1340',
                'ts': '1746290524'
            }
            signed_params = get(params=params)
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 12; ar_IQ; RMX3941; Build/UKQ1.231108.001;tt-ok/3.12.13.21-ul)",    
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-tt-req-timeout': "90000",
                'sdk-version': "2",
                'passport-sdk-version': "30990",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.2.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "did",
            }
            signature = sign(params=signed_params)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })
            try:
                response = requests.get(url, params=signed_params, headers=headers)
                data=response.json()
                if 'data' in data and isinstance(data['data'], list):
                    for item in data['data']:
                        aweme = item.get('aweme_info')
                        if aweme and 'author' in aweme:
                            author = aweme['author']
                            username = author.get('unique_id') 
                            followers = author.get('follower_count') 
                            email=username+"@hotmail.com"    
                            
                            self.API_CH(email)
            except:""
    def admin_hotmail(self):
        try:
            file = open(self.file,'r').read().splitlines()
        except:
            os.system('cls')
            print(S+"السته غير موجوده  ! " )
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user+"@hotmail.com") for user in file]
            for future in futures:
                future.result()
    def admin_gmail(self):
        try:
            file = open(self.file,'r').read().splitlines()
        except:
            os.system('cls')
            print(S+"السته غير موجوده  ! " )
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user+"@gmail.com") for user in file]
            for future in futures:
                future.result()
HSO()