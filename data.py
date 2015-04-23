__author__ = 'Serge Perepelov'

'''
Data set and source strings for Enigma IV decoder
'''

class DataStore():

    # Set of disks

    disk50 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]
    disk51 = ["A", "D", "C", "B", "E", "H", "F", "G", "I", "L",
              "J", "K", "M", "P", "N", "O", "Q", "T", "R", "S",
              "U", "X", "V", "W", "Z", "Y"]
    disk52 = ["A", "Y", "Z", "W", "V", "X", "U", "S", "R", "T",
              "Q", "O", "N", "P", "M", "K", "J", "L", "I", "G",
              "F", "H", "E", "B", "C", "D"]
    disk53 = ["A", "D", "C", "B", "E", "H", "G", "F", "I", "L",
              "K", "J", "M", "P", "O", "N", "Q", "T", "S", "R",
              "U", "X", "W", "V", "Z", "Y"]
    disk60 = ["A", "C", "E", "D", "F", "H", "G", "I", "K", "J",
              "L", "N", "M", "O", "Q", "P", "R", "T", "S", "U",
              "W", "V", "X", "Z", "Y", "B"]
    disk61 = ["A", "Z", "X", "V", "T", "R", "P", "N", "D", "J",
              "H", "F", "L", "B", "Y", "W", "U", "S", "Q", "O",
              "M", "K", "I", "G", "E", "C"]
    disk62 = ["A", "C", "E", "G", "I", "K", "M", "O", "Q", "S",
              "U", "W", "Y", "B", "L", "F", "H", "J", "D", "N",
              "P", "R", "T", "V", "X", "Z"]
    disk63 = ["A", "D", "E", "C", "F", "I", "G", "H", "K", "N",
              "L", "J", "M", "P", "Q", "O", "R", "U", "S", "T",
              "W", "Z", "X", "V", "B", "Y"]
    disk70 = ["A", "Z", "Y", "X", "W", "V", "U", "T", "S", "R",
              "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H",
              "G", "F", "E", "D", "C", "B"]
    disk71 = ["A", "E", "B", "C", "D", "F", "J", "G", "H", "I",
              "K", "O", "L", "M", "N", "P", "T", "Q", "R", "S",
              "U", "Y", "V", "W", "X", "Z"]
    disk72 = ["A", "Z", "X", "W", "V", "Y", "U", "S", "R", "Q",
              "T", "P", "N", "M", "L", "O", "K", "I", "H", "G",
              "J", "F", "D", "C", "B", "E"]
    disk73 = ["A", "X", "Y", "Z", "W", "T", "U", "V", "S", "P",
              "Q", "R", "O", "L", "M", "N", "K", "H", "I", "J",
              "G", "D", "E", "F", "B", "C"]

    # Just a test string to check the code
    testString = "QJYZOVQFFJAI"
