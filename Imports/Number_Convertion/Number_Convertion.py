def run():
    number = input("Please input the number you would like to convert: ")
    to_what = input("What would you like this number converted into:(In lower case) ")
    print("\n If you are confused type (list_options) for the conversion type")

    if to_what == "list_options":
        options = ["decimal", "binary", "hex"]
        print(options)

    if to_what == "decimal":
        print(to_decimal(number))
    if to_what == "binary":
        print(to_binary(number))
    if to_what == "hex":
        print(to_hex(number))


def to_decimal(num):
    From = input("Is this a binary number or a hex number?: ")
    if From == "binary":
        return int(num, 2)
    if From == "hex":
        return int(num, 16)


def decimalToBinary(n):
    return bin(n).replace("0b", " ")


def to_binary(num):
    From = input("Is this a decimal number or a hex number?: ")
    if From == "decimal":
        return decimalToBinary(int(num, 10))
    if From == "hex":
        return decimalToBinary(int(num, 16))


def to_hex(num):
    return hex(int(num, 10))


run()
