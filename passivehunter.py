'''
Author : Devansh Batham
Note   : I initially made this script for my personal use , Now making it public.
I did not cared much about best coding practices as it was just a personal script
'''

from status_check import make_requests
from error_handling import error_handler
from collections import Counter
import os
import requests
import time
import re
import sys
import pathlib
import asyncio

def main(url , domain):

    # a small try and except block for error handling

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(0)

    # filtering out the domain/subdomains using my ugly regex skills 

    pattern = r',.*.'+domain+'",' # an example of ugly regex 
    raw_domains = re.findall(pattern,r.text) 
    temp_domains = []
    for i in raw_domains:
        temp_domains.append(i[1:-2])

    # using Counter for removing the duplicate entries of domains if any.
   
    cnt = Counter(temp_domains)
    print("\u001b[32m[!] Total No of unique domains/subdomains found : " + str(len(cnt)) + "\n\u001b[0m")
    urls = [] 
    
    # for storing https and http urls
    print("\u001b[34;1m")
    for i,j in cnt.items():
        print(i)
        urls.append("https://"+i) #appending https
        urls.append("http://"+i)  #appending http
    print("\n\n")
    print("\u001b[0m")

    '''
     if file already exists empty the file , it happens when you run the script againts same domain
     multiple times 
    '''
    with open(domain+'-200.txt', 'w') as empty:
        empty.write('')
    with open(domain+'-other.txt', 'w') as empty:
        empty.write('')
    with open(domain+'.txt', 'w') as empty:
        empty.write('')
    for i in urls:
            with open(domain+'.txt', 'a') as f:
                f.write(i+"\n")
    
    # if no subdomains found , then exit the program and delete the empty files
    if len(cnt)==0:
        os.remove(domain+'.txt')
        os.remove(domain+'-other.txt')
        os.remove(domain+'-200.txt')
        sys.exit()
   
    
    

if __name__ == "__main__":
    if os.name =='nt':
        os.system("cls") #clear screen
    num_lines = 0  

    # banner below  
    banner = """
    \u001b[35;1m
                             _         _           _           
            ___ ___ ___ _ __|_|_ _ ___| |_ _ _ ___| |_ ___ ___ 
            | . | .'|_ -|_ -| | | | -_|   | | |   |  _| -_|  _|
            |  _|__,|___|___|_|\_/|___|_|_|___|_|_|_| |___|_|
            |_|\u001b[0m                                                
                                  \u001b[42;1m-coded with <3 by Devansh Batham\u001b[0m
            """
 
    print(banner)

    # checks if the supplied command argument is valid
    if len(sys.argv)!=2:
        print("\u001b[31;1m[!] Usage : python3 passivehunter.py domainname.tld\u001b[0m")
        sys.exit(1) 
    
    domain = sys.argv[1]
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    url = "https://dns.bufferover.run/dns?q=." + domain

    # a request is made to the host , that will check for errors (error handling)
    error_handler(url) #function imported from error_handling.py 
    main(url , domain) 
    print("\u001b[0m")
    print("\u001b[32;1m[!] Want to filter out the alive domains ? (Y/N)")
    ch = input()
    if ch.lower() == 'y' or ch.lower() == 'yes':
        here = pathlib.Path(__file__).parent
        with open(here.joinpath(domain+'.txt')) as infile:
            urls = set(map(str.strip, infile))
        #calling make_requests function for making asynchronous requests 
        asyncio.run(make_requests( domain ,urls=urls)) # function imported from status_check.py
        print("\u001b[0m")
    else:
        quit()