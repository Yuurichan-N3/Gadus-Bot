import secrets
import string
import random
from eth_account import Account

def generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_wallet():
    priv_key = "0x" + secrets.token_hex(32)
    account = Account.from_key(priv_key)
    return account.address, priv_key

def generate_form_data(referral_code):
    email = f"{generate_random_string(8)}@gmail.com"
    twitter = f"{generate_random_string(6)}_{random.randint(10, 99)}"
    telegram = f"{generate_random_string(6)}{random.randint(10, 99)}"
    wallet_address, private_key = generate_wallet()
    
    payload = (
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="email"\r\n\r\n'
        f"{email}\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="twitter"\r\n\r\n'
        f"{twitter}\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="retweet"\r\n\r\n'
        f"https://x.com\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="telegram"\r\n\r\n'
        f"{telegram}\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="wallet"\r\n\r\n'
        f"{wallet_address}\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="terms"\r\n\r\n'
        f"false\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB\r\n"
        f'Content-Disposition: form-data; name="referralCode"\r\n\r\n'
        f"{referral_code}\r\n"
        f"------WebKitFormBoundaryPqmBbWQsPAeBT9yB--\r\n"
    )
    
    return email, twitter, telegram, wallet_address, private_key, payload