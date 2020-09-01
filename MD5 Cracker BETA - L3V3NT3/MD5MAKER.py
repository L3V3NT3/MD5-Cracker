import hashlib
import md5

hash_this = raw_input("String to MD5 >>> ")

print(hashlib.md5(str(hash_this).encode("utf")).hexdigest())

