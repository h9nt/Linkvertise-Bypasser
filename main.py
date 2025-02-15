from requests       import get
from os             import system
from colorama       import Fore, Style, init

init(convert=True, autoreset=True)
system("cls")

# Low ass api lmao

def bypass(url: str) -> str:
    try:
        response = get(
            "https://iwoozie.baby/api/free/bypass?url={}".format(url)
            .lower()
            .replace(" ", ""),
            headers={
                "User-Agent"    : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                "Connection"    : "keep-alive",
                "Referer"       : "https://thebypasser.com/",
                "Origin"        : "https://thebypasser.com",
                "Accept"        : "*/*",
                "Host"          : "iwoozie.baby",
            },
        ).json()
        if not response["result"] or response['success'] != True:
            raise Exception("Failed to bypass link")
        return response["result"]
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "[!] Error: {}".format(str(e)))
        return ""


if __name__ == "__main__":
    link = input(Fore.YELLOW + Style.BRIGHT + "Enter the link to bypass: ")
    print(Fore.GREEN + Style.BRIGHT + "Bypassing...")
    print(bypass(link))
