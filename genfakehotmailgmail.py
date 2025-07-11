import random
import string
import os
from colorama import Fore, Style, init

init(autoreset=True)

# أسماء أساسية
base_names = [
    "alex", "sara", "nora", "john", "moh", "adam", "bella", "lily",
    "tito", "leo", "sam", "zozo", "noor", "huda", "omar", "jessy", "maria", "mike", "ali", "aya"
]

# رموز شائعة ومقاطع مستخدمة في السوشيال
modifiers = [
    "", ".", "_", "__", "x", "xo", "xx", "xX", "Xx", "the", "real", "pro", "dev", "gamer", "boss", "life", "tv", "official", "lover"
]

# سنوات أو أرقام
years = [str(y) for y in range(1980, 2005)] + [str(random.randint(10, 99)) for _ in range(50)]

def generate_realistic_username():
    # اختر اسم أو اسمين
    name1 = random.choice(base_names)
    name2 = random.choice(base_names)
    while name2 == name1:
        name2 = random.choice(base_names)

    # دمج الأسماء
    base = random.choice([
        name1,
        name1 + name2,
        name1 + random.choice(modifiers) + name2,
        name1 + random.choice(modifiers)
    ])

    # إضافة النهاية (رقم، سنة، أو رمز)
    end = random.choice([
        "", random.choice(modifiers),
        str(random.randint(1, 999)),
        random.choice(years),
        "_" + random.choice(years),
        random.choice(modifiers) + str(random.randint(10, 99))
    ])

    return (base + end).lower()

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.MAGENTA + Style.BRIGHT + "     🔥 مولّد إيميلات واقعية وذكية 🔥")
    print(Fore.CYAN + Style.BRIGHT + "="*50 + "\n")

def main():
    print_banner()

    # اختيار نوع الإيميل
    while True:
        provider_input = input(Fore.YELLOW + "📧 اختر نوع البريد [1] Gmail  [2] Hotmail: ").strip()
        if provider_input == "1":
            provider = "gmail.com"
            break
        elif provider_input == "2":
            provider = "hotmail.com"
            break
        else:
            print(Fore.RED + "❌ إدخال غير صالح، اختر 1 أو 2.")

    # عدد الحسابات
    try:
        count = int(input(Fore.YELLOW + "🔢 كم عدد الحسابات التي تريد توليدها؟ "))
    except ValueError:
        print(Fore.RED + "❌ يرجى إدخال رقم صحيح.")
        return

    filename = f"smart_emails_{provider.split('.')[0]}.txt"

    with open(filename, "w") as f:
        for _ in range(count):
            email = generate_realistic_username() + "@" + provider
            f.write(email + "\n")

    print(Fore.GREEN + f"\n✅ تم توليد {count} بريد ({provider}) وحفظها في: {filename}\n")

if name == "main":
    main()
