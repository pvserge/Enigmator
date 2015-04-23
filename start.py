__author__ = 'Serge Perepelov'

'''
The Module to start decoding
'''

import data
import decoder

decryptor = decoder.Decryptor()
setter = data.DataStore()

# Strings to decode

sourceString = "UIKHEYGGPCVLNIBQKRDYUYPEFRWT" \
               "YUSAZEKWENUNXSOIKGKBLGTITRJCYIDRXGKY" \
               "RZGPYSRRBWBMEXMLELDAASQKXUEWODEZ" \
               "KJFCEKGDNKFZUGHZBBJBIKBYEKKJBTRAHEAM" \
               "EOXWXAYFMWBTJVAFVIABGAAAVIFWWZKXBVRR" \
               "AZAYKBIODJYVGDQRXTDWIHHEVQDDLJRJYDFD" \
               "TNZUPIDBEIVXIIVQCRCFPYEOIPYOPEQPSGDQ" \
               "UYSUZGAUABFDGBZIOLSUKAKBOYBBXYXSYZPT" \
               "XWIONWXLAPLALXW"

# Simple decryption test
# Decode testString = "QJYZOVQFFJAI" to result string "COMEBACKSOON"
# The KEY fraze is HOT
# The disk set is 60-70-50

print("Just a test")
set1 = decryptor.setup_disks(setter.disk60, setter.disk50, "HOT", 0)
set2 = decryptor.setup_disks(setter.disk70, setter.disk50, "HOT", 1)
decodedString = decryptor.decode(set1, set2, setter.testString)
print(decodedString)


# ###################RED#####################

# first 20 symbols in sourceString
print("Result of first 20 symbols in source string with disks set A and key RED:")
set1 = decryptor.setup_disks(setter.disk51, setter.disk72, "RED", 0)
set2 = decryptor.setup_disks(setter.disk60, setter.disk72, "RED", 1)
decodedString = decryptor.decode(set1, set2, sourceString[:20])
print(decodedString)