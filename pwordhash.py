# some code taken from https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
import hashlib
import os

# declarations
users = {}

username = 'rad_dude420'
password = 'p455w0rd'

salt = os.urandom(32)

# generate hash
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

#storage
users[username] = { 'salt': salt, 'key': key}

#retrieval
#salt_from_storage = storage[:32]
#key_from_storage = storage[32:]

# Verification attempt 1 (incorrect password)
username = 'rad_dude420'
password = '1nc0rr3ctp455w0rd'

salt = users[username]['salt'] # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key != new_key # The keys are not the same thus the passwords were not the same


# Verification attempt 2 (correct password)
username = 'rad_dude420'
password = 'p455w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key # The keys are the same thus the passwords were the same

# Adding a different user
username = 'hella_jeff'
password = 'p@$$w0rd'

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

# Checking the other users password
username = 'hella_jeff'
password = 'p@$$w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key # The keys are the same thus the passwords were the same for this user also