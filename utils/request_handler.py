import requests
from termcolor import colored
import time

def send_request(url, headers, payload, request_num, email, wallet_address):
    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            print(colored(f"Request {request_num}: Success - Email: {email}, Wallet: {wallet_address}", "green"))
            return True
        else:
            print(colored(f"Request {request_num}: Failed - Status Code: {response.status_code}", "red"))
            return False
    except Exception as e:
        print(colored(f"Request {request_num}: Error - {str(e)}", "red"))
        return False
    finally:
        time.sleep(1)
