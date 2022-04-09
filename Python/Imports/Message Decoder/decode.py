fromEncodedMessage = ""
fromEncryptedMessage = ""


def decode(message):
    global fromEncodedMessage
    lowerLetterLib = [["a", "61"], ["b", "62"], ["c", "63"], ["d", "64"], ["e", "65"], ["f", "66"], ["g", "67"],
                      ["h", "68"], ["i", "69"], ["j", "6A"], ["k", "6B"], ["l", "6C"], ["m", "6D"], ["n", "6E"],
                      ["o", "6F"], ["p", "70"], ["q", "71"], ["r", "72"], ["s", "73"], ["t", "74"], ["u", "75"],
                      ["v", "76"], ["w", "77"], ["x", "78"], ["y", "79"], ["z", "7A"]]
    upperLetterLib = [["A", "41"], ["B", "42"], ["C", "43"], ["D", "44"], ["E", "45"], ["F", "46"], ["G", "47"],
                      ["H", "48"], ["I", "49"], ["J", "4A"], ["K", "4B"], ["L", "4C"], ["M", "4D"], ["N", "4E"],
                      ["O", "4F"], ["P", "50"], ["Q", "51"], ["R", "52"], ["S", "53"], ["T", "54"], ["U", "55"],
                      ["V", "56"], ["W", "57"], ["X", "58"], ["Y", "59"], ["Z", "5A"]]

    symbolLib = [["{", "7B"], ["}", "7D"], ["|", "7C"], ["~", "7E"], ["_", "5F"], ["`", "60"], ["^", "5E"], ["]", "5D"],
                 ["\\", "5C"], ["[", "5B"], ["@", "40"], ["?", "3F"], [">", "3E"], ["=", "3D"], ["<", "3C"],
                 [";", "3B"],
                 [":", "3A"], ["/", "2F"], [".", "2E"], ["-", "2D"], [",", "2C"], ["+", "2B"], ["*", "2A"], [")", "29"],
                 ["(", "28"], ["'", "27"], ["&", "26"], ["%", "25"], ["$", "24"], ["#", "23"], ['"', "22"], ["!", "21"],
                 [" ", "20"]]

    def lowerCheck(letter):
        global fromEncodedMessage
        for i in range(len(lowerLetterLib)):
            if letter == lowerLetterLib[i][1]:
                fromEncodedMessage += lowerLetterLib[i][0]

    def upperCheck(letter):
        global fromEncodedMessage
        for i in range(len(upperLetterLib)):
            if letter == upperLetterLib[i][1]:
                fromEncodedMessage += upperLetterLib[i][0]

    def symbolCheck(letter):
        global fromEncodedMessage
        for i in range(len(symbolLib)):
            if letter == symbolLib[i][1]:
                fromEncodedMessage += symbolLib[i][0]

    for t in range(len(message)):
        lowerCheck(message[t:t + 2])
        upperCheck(message[t:t + 2])
        symbolCheck(message[t:t + 2])

    return fromEncodedMessage


def decrypt(text):
    global fromEncryptedMessage
    lowerLetterLib = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
    upperLetterLib = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]
    symbolLib = [["{"], ["}", "7D"], ["|", "7C"], ["~", "7E"], ["_", "5F"], ["`", "60"], ["^", "5E"], ["]", "5D"],
                 ["\\", "5C"], ["[", "5B"], ["@", "40"], ["?", "3F"], [">", "3E"], ["=", "3D"], ["<", "3C"],
                 [";", "3B"],
                 [":", "3A"], ["/", "2F"], [".", "2E"], ["-", "2D"], [",", "2C"], ["+", "2B"], ["*", "2A"], [")", "29"],
                 ["(", "28"], ["'", "27"], ["&", "26"], ["%", "25"], ["$", "24"], ["#", "23"], ['"', "22"], ["!", "21"],
                 [" ", "20"]]

    def lowerCheck(letter):
        global fromEncryptedMessage
        for i in range(len(lowerLetterLib)):
            if letter == lowerLetterLib[i]:
                if i - 3 << len(lowerLetterLib) and i - 3 != 0:
                    fromEncryptedMessage += str(lowerLetterLib[i - 3])
                else:
                    over = i - 3 - len(lowerLetterLib)
                    fromEncryptedMessage += str(lowerLetterLib[over])

    def upperCheck(letter):
        global fromEncryptedMessage
        for i in range(len(upperLetterLib)):
            if letter == upperLetterLib[i]:
                if i - 3 << len(upperLetterLib) and i - 3 != 0:
                    fromEncryptedMessage += str(upperLetterLib[i - 3])
                else:
                    over = i - 3 - len(upperLetterLib)
                    fromEncryptedMessage += str(upperLetterLib[over])

    def symbolCheck(letter):
        global fromEncryptedMessage
        for i in range(len(symbolLib)):
            if letter == symbolLib[i][0]:
                fromEncryptedMessage += symbolLib[i][0]

    for t in text:
        symbolCheck(t)
        lowerCheck(t)
        upperCheck(t)

    return fromEncryptedMessage


newMessage = ""
decodedMessage = decode(newMessage)
decryptedMessage = decrypt(decodedMessage)

print(decodedMessage)
print(decryptedMessage)
