import requests
from Crypto.Hash import keccak

def check_password(password):
    password_bytes = password.encode('utf-8') 
    keccak_512 = keccak.new(digest_bits=512)
    hash_object = keccak_512.update(password_bytes)
    hex_dig = hash_object.hexdigest()
    base_link = "https://passwords.xposedornot.com/api/v1/pass/anon"
    with requests.Session() as session:
        response = session.get(f"{base_link}/{hex_dig[:10]}")
        message = response.json()
        if message.get("SearchPassAnon"):
            count = message.get('SearchPassAnon').get('count')
            wordlist = message.get('SearchPassAnon').get('wordlist')
            return count, wordlist 
        else:
            return 0, 0

