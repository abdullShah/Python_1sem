import os
import struct as s

f = open('test.bin', "rb+")
f.write(s.pack(f'>i', 50))
# f.write(s.pack(f'>i', 46))
f.close()



print(os.path.getsize('test.bin'))