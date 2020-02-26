import asyncio
import aiohttp
import time
from aiohttp import *
import os
from datetime import datetime
from threading import Timer


domain_name = ""

'''
#uncomment this section and change the seconds as per your requirement
#  this exit function is for terminating the program if it takes more than 80 seconds
#  you can change the termination time according to your requirements
def exitfunc():
    print("\n\u001b[31;1mProgram Exited  \u001b[0m")
    print("\u001b[31;1mExit Time : ", datetime.now())
    print("\u001b[0m")
    os._exit(0)

Timer(80, exitfunc).start()  # exits the program after 80 seconds
'''

# writing urls with 200 OK status in domain-200.txt file 
def collector_alive(uri , domain_name):
    with open(domain_name+'-200.txt', 'a') as f1:
        f1.write(uri+"\n")

# writing urls with response code other than 200 in domain-other.txt file
def collector_alive_but_404(uri,domain_name):
    with open(domain_name+'-other.txt', 'a') as f2:
        f2.write(uri+"\n")



async def fetch_html(domain , url: str, session: ClientSession, **kwargs) -> tuple:
    # making request to the server , I know the error handling is dirty
    try:
        resp = await session.request(method="GET", url=url, **kwargs)
    except ClientConnectorError:
        return (url, 500) 
    except ClientOSError:
        return (url, 500)
    except ServerDisconnectedError:
        return (url,500)
    except asyncio.TimeoutError:
        return (url, 500)
    except UnicodeDecodeError:
        return (url, 500)
    except TooManyRedirects:
        return (url, 500)
    except ServerTimeoutError:
        return (url, 500)
    except ServerConnectionError:
        return (url, 500)
    except RuntimeError:
        return (url, 500)
    except KeyboardInterrupt:
        print("\u001b[31;1m[!] KeyboardInterrupt Occured \u001b[0m")
    
    # if response is 200
    if resp.status ==200:
        collector_alive(url , domain)
        print(f'\u001b[32;1m[{resp.status}]  {url}')

    # if response is other than 200
    else:
        collector_alive_but_404(url ,domain)
        print(f'\u001b[31;1m[{resp.status}]  {url}')
    

# make_requests function 

async def make_requests(domain , urls: set , **kwargs) -> None:
    domain_name = domain
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch_html(domain ,url=url, session=session, **kwargs)
            )
        time.sleep(0.5)
        print("\n \u001b[32;1m[+]\u001b[35;1m  Loading URLS  \u001b[0m  ")
        time.sleep(0.5)
        print(" \u001b[32;1m[+]\u001b[35;1m  Checking on both http and https \u001b[0m  ")
        time.sleep(0.5)
        print(" \u001b[32;1m[+]\u001b[35;1m  Hang on there , This might take some time \u001b[0m")
        time.sleep(0.5)
        print(" \u001b[32;1m[+]\u001b[35;1m  Creating files domain-200.txt , domain.txt , domain-other.txt \u001b[0m")
        print(" \u001b[32;1m[+]\u001b[35;1m  domain.txt contains     : all domains  \u001b[0m")
        print(" \u001b[32;1m[+]\u001b[35;1m  domain-200.txt contains : domains with 200 response code  \u001b[0m")
        print(" \u001b[32;1m[+]\u001b[35;1m  domain.txt contains     : domains with code other than 200  \u001b[0m\n")
        
        results = await asyncio.gather(*tasks) # gathering tasks 