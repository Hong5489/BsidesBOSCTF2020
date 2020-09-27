# Fancy Caesar Cipher
```
We RSA encrypted the flag, but forgot to save the private key. Is it possible to recover the flag without it?

Download the file below.
```
[fancy_caesar_cipher.py](fancy_caesar_cipher.py) [fancy_caesar_cipher.out](fancy_caesar_cipher.out)

We are given the Python source code and the output

It is a typical RSA decryption challenge:
```py
from Crypto.Util.number import getStrongPrime
from fractions import gcd
from secret import flag

def get_key(e=65537, bit_length=2048):
    while True:
        p = getStrongPrime(bit_length, e=e)
        q = getStrongPrime(bit_length, e=e)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            return e, p * q

def encrypt(e, n, m):
    return [((ord(c) ** e) % n) for c in m]

e, n = get_key()

print("Generated key:")
print(e)
print(n)

print("Encrypted flag:")
print(encrypt(e, n, flag))
```
Notice the encrypt function, it **encrypts the flag characters one by one**

Means we can just find the plaintext by just **brute forcing the ciphertext:**
```py
flag = ""
for o in out:
	# Brute force every printable character
	for i in range(32,127):
		# If the ciphertext are equal then the plaintext found
		if pow(i,e,n) == o:
			flag += chr(i)
			break
print flag 
```
Result:
```
flag{phwd_iodj_lv_phwd}
```
Notice the flag is encrypted by Caesar Cipher, simply shift it by 23 become `meta_flag_is_meta`

[Python script](solve.py)

## Flag
```
flag{meta_flag_is_meta}
```