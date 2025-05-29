URL = "https://gadus.xyz/api/index.php/waitlist_signupp"

def HEADERS(referral_code):
    return {
        "accept": "*/*",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryPqmBbWQsPAeBT9yB",
        "origin": "https://gadus.xyz",
        "referer": f"https://gadus.xyz/referral/{referral_code}",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
    }