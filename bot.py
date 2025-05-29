import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from termcolor import colored
from utils.config import URL, HEADERS
from utils.generator import generate_form_data
from utils.request_handler import send_request
from utils.data_saver import save_to_json

def main():
    print(colored("╔══════════════════════════════════════════════╗", "cyan"))
    print(colored("║       🌟 GADUS BOT - Waitlist Signup         ║", "cyan"))
    print(colored("║   Automate your Gadus waitlist signups!      ║", "cyan"))
    print(colored("║  Developed by: https://t.me/sentineldiscus   ║", "cyan"))
    print(colored("╚══════════════════════════════════════════════╝", "cyan"))
    
    referral_code = input(colored("Masukkan kode referral: ", "yellow"))
    num_requests = int(input(colored("Masukkan jumlah request: ", "yellow")))
    
    for i in range(num_requests):
        email, twitter, telegram, wallet_address, private_key, payload = generate_form_data(referral_code)
        headers = HEADERS(referral_code)
        
        success = send_request(URL, headers, payload, i + 1, email, wallet_address)
        if success:
            data_entry = {
                "email": email,
                "twitter": twitter,
                "telegram": telegram,
                "wallet_address": wallet_address,
                "private_key": private_key,
                "referral_code": referral_code
            }
            save_to_json(data_entry)
            print(colored(f"Data saved to data.json for request {i+1}", "yellow"))

if __name__ == "__main__":
    main()
