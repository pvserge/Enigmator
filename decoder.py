__author__ = 'Serge Perepelov'
'''
The module has Decryptor class, that incapsulates the decryption logic of Enigma IV
designed and build by Dave Janelle and Bob Nolet as Cretive Crafthouse

The class has methods:
- decode(set1, set2, source_string)
- setup_disks(d1, d2, clue, rev)
'''


class Decryptor():

    def decode(self, set1, set2, source_string):

        source_list = list(source_string)

        result = ""

        i = 0

        while i < len(source_list):
            letter = source_list[i]
            if i % 2 != 0:
                for key, value in set2.items():
                    if key == letter:
                        result += value
            else:
                for key, value in set1.items():
                    if key == letter:
                        result += value
            i += 1

        return result

    def setup_disks(self, d1, d2, clue, rev):

        disk_1 = d1
        disk_2 = d2
        key = clue
        key_pos_disk1 = key[0]
        key_pos_disk2 = key[2]
        disks_set = {}

        if rev == 1:
            disk_2 = d2[::-1]
            key_pos_disk1 = key[1]

        start_pos_disk1 = disk_1.index(key_pos_disk1)
        start_pos_disk2 = disk_2.index(key_pos_disk2)

        user_disk_1 = disk_1[start_pos_disk1:] + disk_1[:start_pos_disk1]
        user_disk_2 = disk_2[start_pos_disk2:] + disk_2[:start_pos_disk2]

        i = 0

        while i < len(user_disk_1):

            key = user_disk_1[i]
            value = user_disk_2[i]

            disks_set[key] = value
            i += 1

        return disks_set


