#name is tools [ Create random emails  ] 
#hi pro how are you? 
#Luffy is here f**k you 
#luffy is king pro
#luffy user [ @DDDBB4 ]
#Luffy chaneel [ t.me/Tools_Watan ]
# Last Update [ 2025 | 07 | 04 ]
#see you pro
#----------------------------------------------

import random
import string
import sys
from time import sleep

def display_banner():
    print("""
    ██╗     ██╗   ██╗███████╗███████╗██╗   ██╗
    ██║     ██║   ██║██╔════╝██╔════╝╚██╗ ██╔╝
    ██║     ██║   ██║█████╗  █████╗   ╚████╔╝ 
    ██║     ██║   ██║██╔══╝  ██╔══╝    ╚██╔╝  
    ███████╗╚██████╔╝██║     ██║        ██║   
    ╚══════╝ ╚═════╝ ╚═╝     ╚═╝        ╚═╝   
    """)
    
def generate_random_password(length=8):

    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_email(domain=None, length=8):
    """إنشاء إيميل عشوائي"""
    if domain is None:
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'protonmail.com']
        domain = random.choice(domains)
    
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return f"{username}@{domain}"

def generate_combos(emails=None, passwords=None, num_random=0, num_random_emails=0):
    """إنشاء كومبو من الإيميلات وكلمات المرور"""
    combos = []
    
    if emails is None:
        emails = []
    
    if passwords is None:
        passwords = []
    
    
    random_emails = [generate_random_email() for _ in range(num_random_emails)]
    all_emails = emails + random_emails
    
    for email in all_emails:
    
        for pwd in passwords:
            combos.append(f"{email}:{pwd}")
        
   
        for _ in range(num_random):
            password = generate_random_password()
            combos.append(f"{email}:{password}")
    
    return combos

def save_to_file(combos, filename):
    """حفظ النتائج في ملف"""
    with open(filename, 'w') as f:
        for combo in combos:
            f.write(f"{combo}\n")
    print(f"\nتم حفظ النتائج في ملف {filename}")

def main():
    display_banner()
    
    print(" [1]Enter emails manually -  إدخال الإيميلات يدوياً")
    print(" [2]Download emails from a file  - تحميل الإيميلات من ملف")
    print(" [3]Create random emails -  إنشاء إيميلات عشوائية")
    choice = input("[+]choose [اختار] = ")
    
    emails = []
    num_random_emails = 0
    
    if choice == '1':
        emails_input = input("Enter emails [ادخل الايميلات] ")
        emails = [e.strip() for e in emails_input.replace(',', ' ').split()]
    elif choice == '2':
        filename = input("Enter the name of the email combo [ادخل اسم كومبو الايميلات]")
        try:
            with open(filename, 'r') as f:
                emails = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("File not found [الملف غير موجود]")
            sys.exit(1)
    elif choice == '3':
        num_random_emails = int(input("How many random emails do you want? [كم عدد الايميلات العشوائية تريد]: "))
    else:
        print("Incorrect choice [اختيار خاطئ]")
        sys.exit(1)
    
    print("[1]Use specific passwords - استخدام كلمة سر محددة")
    print("[2]Generate only random passwords -  إنشاء كلمات سر عشوائي")
    print("[3]Use of the word random and specific  -  استخدام كلمات سر عشوائي ومحدد")
    pass_choice = input("[+]choose [اختار] ")
    
    passwords = []
    num_random = 0
    
    if pass_choice == '1':
        passwords_input = input("Enter your password [ادخل كلمة المرور ]")
        passwords = [p.strip() for p in passwords_input.replace(',', ' ').split()]
    elif pass_choice == '2':
        num_random = int(input("Number of random passwords [عدد كلمات المرور العشوائية]"))
    elif pass_choice == '3':
        passwords_input = input("Enter the specified password [ادخل كلمة المرور المحددة] ")
        passwords = [p.strip() for p in passwords_input.replace(',', ' ').split()]
        num_random = int(input("How many random passwords do you want [كم عدد كلمات المرور العشوائية تريد] "))
    else:
        print("Incorrect choice [اختيار خاطئ]")
        sys.exit(1)
    
    print("\nجارٍ إنشاء الكومبو...")
    sleep(1)
    
    combos = generate_combos(emails if choice in ['1', '2'] else None, 
                           passwords if pass_choice in ['1', '3'] else None, 
                           num_random, 
                           num_random_emails)
    
    
    
    for i, combo in enumerate(combos[:10], 1):  # 
        print(f"{i}. {combo}")
    if len(combos) > 10:
        print(f"... وعرض {len(combos)-10} نتيجة إضافية")
    
    save = input("\nهل تريد حفظ النتائج في ملف؟ (نعم/لا): ").lower()
    if save in ['y', 'yes', 'نعم', 'y']:
        filename = input("أدخل اسم الملف للحفظ (مثال: combos.txt): ")
        save_to_file(combos, filename)
    
    

if __name__ == "__main__":
    main()