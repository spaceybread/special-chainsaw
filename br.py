import itertools
import string
import base64
import pyotp

keyspace = string.digits + string.ascii_lowercase
for combination in itertools.product(*[keyspace] * 4):
    raw_key = ''.join(combination)
    hotp_key = base64.b32encode(bytearray(raw_key, 'ascii')).decode('utf-8')
    hotp = pyotp.HOTP(hotp_key)
    print(raw_key)
    for i in range(100):
        if hotp.at(i) == '896331' and hotp.at(i + 1) == '402643':
            print(raw_key, i)
            quit()
