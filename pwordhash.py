# some code taken from https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
import hashlib
import pymysql.cursors
import uuid

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='hp1617wy',
                             password='Arp182019',
                             db='hp1617wy',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# declarations
username = 'rad_dude420'
password = '0th3rp455w0rdzz'

salt = uuid.uuid4()
salt = repr(salt.hex)

# generate hash
hashpass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

print(username)
print(salt)
print(password)
print(hashpass)

sql = "INSERT INTO salt (hash, username, salt) VALUES (%s, %s,%s)"
to_sql = (hashpass, username, salt)
connection.commit()









'''#following code for test purposes only
#users = {}

#storage
#users[username] = { 'salt': salt, 'hashpass': hashpass}

#retrieval
salt_from_storage = storage[:32]
key_from_storage = storage[32:]

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

assert key == new_key # The keys are the same thus the passwords were the same for this user also'''