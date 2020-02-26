import requests
import sys

'''
This function is solely for error handling 
'''
def error_handler(url):
    # This error handling might be ugly , but yes it does work :) 
    try:
        res = requests.get(url,timeout=30)
    except requests.ConnectionError as e:
        print("\u001b[31;1mOOPS!! Connection Error. Make sure you are connected to Internet.\u001b[0m")
        print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : [todo]\u001b[0m")
        print("\u001b[0m")
        sys.exit()
    except requests.Timeout as e:
        print("\u001b[31;1mOOPS!! Timeout Error\u001b[0m")
        print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : [todo]\u001b[0m")
        print("\u001b[0m")
        sys.exit()
    except requests.RequestException as e:
        print("\u001b[31;1mOOPS!! General Error\u001b[0m")
        print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : [todo]\u001b[0m")
        print("\u001b[0m")
        sys.exit()
    except KeyboardInterrupt:
        print("\u001b[31;1mSomeone closed the program\u001b[0m")
        print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : [todo]\u001b[0m")
        print("\u001b[0m")
        sys.exit()
