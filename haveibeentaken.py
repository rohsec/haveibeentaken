import requests as req
import argparse
import os

bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'

def logo():
    print(f"""{blue}
------------------------------------------------------------------------------------------
'                                                                                         '
' {green}.       _  _ ____ _  _ ____    _    ___  ____ ____ _  _    ___ ____ _  _ ____ _  _ __.  '
'  .__ __ |__| |__| |  | |___    |    |__] |___ |___ |\ |     |  |__| |_/  |___ |\ |  _]  '
' {yellow} ,      |  | |  |  \/  |___    |    |__] |___ |___ | \|     |  |  | | \_ |___ | \|  .   '
'                                                                                         '
'                       {blue}<------- {yellow}Developed By: {bred}🐦 @marcos-iaf{blue} ------->{blue}                    '
------------------------------------------------------------------------------------------
{reset}
""")

def check_username(username):
    print(f"{green}[*]{red} Server: {blue}infosec.exchange{reset}")
    print(f"{yellow}[+] {blue}Checking if {bblue}@{username}{blue} is taken or not{reset}")
    resp=req.get(f"https://infosec.exchange/@{username}")
    if(resp.status_code==404):
        print(f"{bgreen}[✓] {bblue}@{username}{bgreen} is available for registration!{reset}")
    elif(resp.status_code==200):
        print(f"{bred}[X] {bblue}@{username}{bred} is taken!{reset}")
    else:
        print(f"{yellow}[!] Technical Exception Occured!!{reset}")



def check_usernames(filename):
    if(os.path.isfile(filename)):
        print(f"{green}[*]{red} Server: {blue}infosec.exchange{reset}")
        print(f"{yellow}[+] {blue}Running multiple checks...{reset}")
        f=open(filename,'r')
        for i in f.readlines():
            # username=f.readline()
            resp=req.get(f"https://infosec.exchange/@{i.strip()}")
            if(resp.status_code==404):
                print(f"{bgreen}[✓] {bblue}@{i.strip()}{bgreen} is available for registration!{reset}")
            elif(resp.status_code==200):
                print(f"{bred}[X] {bblue}@{i.strip()}{bred} is taken!{reset}")
            else:
                print("[!] Technical Exception Occured!!")
        f.close()
    else:
        print(f"{yellow}[!] No file named {bblue}{filename}{reset}")

def main():
    logo()
    parser=argparse.ArgumentParser()
    parser.add_argument('-u', help="Username to Check",required=False)
    parser.add_argument("-l", help="File containing list of usernames",required=False)
    args=parser.parse_args()
    if(args.u):
        check_username(args.u)
    elif(args.l):
        check_usernames(args.l)
    else:
        print("""\nusage: haveibeentaken.py [-h] [-u U] [-l L]

options:
  -h, --help  show this help message and exit
  -u U        Username to Check
  -l L        File containing list of usernames""")


if __name__=="__main__":
    main()

