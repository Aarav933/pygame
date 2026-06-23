import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN} Welcome to Sentiments{Style.RESET_ALL}")
username= input(f"{Fore.BLUE} Enter your name:{Style.RESET_ALL}").strip()
if not username:
    username="Mystery"
conversationhistory=[]
print(f"{Fore.GREEN} Hello agent{username}")
print(f"Type a scentence and i will analyze it with textblob")
print(f"Type{Fore.YELLOW} reset{Fore.RED}, history{Fore.BLACK}, or{Fore.MAGENTA} exit{Fore.BLACK} to quit{Fore.LIGHTGREEN_EX}")
while True:
    userinput=input(f"{Fore.CYAN}:{Style.RESET_ALL}").strip()
    if not userinput:
        print(f"{Fore.LIGHTGREEN_EX} Please enter a valid text{Style.RESET_ALL}")
        continue
    if userinput.lower() == "exit":
        print(f"{Fore.MAGENTA} EXiting Sentiment SPY{Style.RESET_ALL}")
        break
    elif userinput.lower() == "reset":
        conversationhistory.clear()
        print(f"{Fore.RED} Conversation history cleared. {Style.RESET_ALL}")
    elif userinput.lower()=="history":
        if not conversationhistory:
            print(f"{Fore.GREEN}NO conversation history yet{Style.RESET_ALL} ")
        else:
            print(f"{Fore.BLUE} Conversation history:{Style.RESET_ALL}")
            for idx,(text, polarity, sentimenttype) in enumerate(conversationhistory, start=1):
                if sentimenttype =="Positive":
                    color = Fore.GREEN
                elif sentimenttype =="Negative":
                    color = Fore.RED
                else:
                    color=Fore.YELLOW
                print(f"{idx}, {color} {text}")