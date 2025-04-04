import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open("top-10000-passwords.txt", "r") as file:
        passwords = file.read().splitlines()

    if use_salts:
        with open("known-salts.txt", "r") as file:
            salts = file.read().splitlines()
    
    for password in passwords:
        if use_salts:
            for salt in salts:
                # Check salt prepended to password
                salted_hash = hashlib.sha1((salt + password).encode()).hexdigest()
                if salted_hash == hash:
                    return password
                
                # Check salt appended to password
                salted_hash = hashlib.sha1((password + salt).encode()).hexdigest()
                if salted_hash == hash:
                    return password
        else:
            salted_hash = hashlib.sha1(password.encode()).hexdigest()
            if salted_hash == hash:
                return password

    return "PASSWORD NOT IN DATABASE"