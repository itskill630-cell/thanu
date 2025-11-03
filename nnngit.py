msg, s = "hello", 3
enc = ''.join(chr((ord(c)-97+s)%26+97) for c in msg)
dec = ''.join(chr((ord(c)-97-s)%26+97) for c in msg)
print("enc:", enc, "dec:", dec