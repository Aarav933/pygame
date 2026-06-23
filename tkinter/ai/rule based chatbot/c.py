import re, random
from colorama import Fore, init
init(autoreset=True)
destination = {
    "beach":["Hawai", "Bali", "Maldieves"],
    "city":["New York", "Paris", "Tokyo"],
    "mountain":["Swiss Alps","Himalayas","Mount Everest"]
}
jokes=[
    "Why dont programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? it had a virus!",
    "Why do travellers feel warm? Because of their hotspots!"
]
def normalize(text):
    return re.sub(r"\s+","", text.strip().lower())
def recommendation():
    print(Fore.LIGHTBLUE_EX+"Travelbot: Mountains, beach or city")
    pref = input(Fore.GREEN+"you:")
    pref = normalize(pref)
    if pref in destination:
        suggestion = random.choice(destination[pref])
        print(Fore.BLUE+"Travelbot: how about{suggestion}")
        print(Fore.BLUE+"Travelbot: Do you like it? (yes or no)")
        ans = input(Fore.GREEN+"You:".lower)
        if ans == "yes":
            print(Fore.RED+"Great! {suggestion}")
        elif ans == "no":
            print(Fore.RED+"Oh ok lets try a nother one!")
            recommendation()
        else:
            print(Fore.RED+"i will suggest a nother one")
            recommendation()
    else:
        print(Fore.RED+"Im sorry i dont have that destination Try again")
        recommendation()
def packingtips():
    print(Fore.LIGHTBLUE_EX+"Travelbot: Where to?")
    location = normalize(input(Fore.Green+"You:"))
    print(Fore.LIGHTBLUE_EX+"Travelbot: How many days?")
    days = input(Fore.GREEN+"You:")
    print(Fore.LIGHTCYAN_EX+"Travelbot: OK Packingtips for {days}in {location}.")
    print(Fore.BLUE+"Pack versataile clothes")
    print(Fore.LIGHTCYAN_EX+"Bring chargers")
    print(Fore.YELLOW+"Pack rainclothes")